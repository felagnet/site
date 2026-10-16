"""Checks felag.net before it ships. Runs on dist/ after build_site.py and make_dist.py, prints a table of
checks and exits non-zero on any failure.

  python3 check.py                everything, as the workflow runs it
  python3 check.py --no-browser   skip the Playwright pass
  python3 check.py --no-links     skip the external link pass

The static checks need only the standard library, the browser pass needs Playwright with Chromium, and the
link pass needs network access."""

import argparse
import concurrent.futures
import os
import pathlib
import re
import struct
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import felagsite  # noqa: E402  the copy constants: PEOPLE and STATEMENT are read from here

DIST = os.path.join(HERE, "dist")
INDEX = os.path.join(DIST, "index.html")
SITE = "https://felag.net/"
MAILTO = "mailto:info@felag.net"
HERO_LINE = "Senior engineers who own the architecture and ship to production."
BANNED = ["passionate", "cutting-edge", "seamless", "empower", "world-class", "AI-first", "Andrei", "Georgia",
          "four people", "Talk to a founder", "sold to"]
# which links each People card carries; the addresses come from felagsite.PEOPLE
PEOPLE_LINKS = {
    "Andrew Skurlatov": ["LinkedIn", "GitHub", "X"],
    "Mikhail Manko": ["LinkedIn"],
    "Pavel Dodonov": ["LinkedIn", "GitHub"],
    "Andrey Solovov": ["LinkedIn", "GitHub"],
}
DIST_FILES = ["index.html", "CNAME", ".nojekyll", "robots.txt", "sitemap.xml", "favicon.svg",
              "apple-touch-icon.png", "og.png", "404.html"] + [
              f"people/{n}.{ext}" for n in ("andrew", "mike", "pavel", "andrey") for ext in ("jpg", "webp")]
VIEWPORTS = [(1440, 900), (1728, 1117), (390, 844)]
GL_NOISE = re.compile(r"GL Driver Message|GPU stall|GroupMarkerNotSet|swiftshader|ANGLE|WebGL", re.I)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/141.0.0.0 Safari/537.36")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
TEXT_ATTRS = ("alt", "aria-label", "title", "placeholder")
EM_DASH = chr(0x2014)  # spelled as a code point so this file carries no em dash itself

ROWS = []


def row(name, ok, note=""):
    ROWS.append((name, {True: "PASS", False: "FAIL", None: "SKIP"}[ok], note))


# ---------------------------------------------------------------------------------------------- parsing

class Page(HTMLParser):
    """One pass over the page: visible text, head tags, anchors and the People cards."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # open elements as (tag, attrs)
        self.body_text = []      # text nodes outside script and style, template content included
        self.extra_text = []     # title, user-facing attributes and meta content
        self.title = ""
        self.metas = []
        self.links = []
        self.anchors = []        # (href, text)
        self.people_depth = None
        self.people_jpegs = 0
        self.cards = []
        self.card_depth = None
        self._anchor = None

    def _in(self, tag):
        return any(t == tag for t, _ in self.stack)

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        self._element(tag, a)
        if tag not in VOID:
            self.stack.append((tag, a))
            if a.get("id") == "people":
                self.people_depth = len(self.stack)
            if tag == "article" and "person" in a.get("class", "").split() and self.people_depth:
                self.card_depth = len(self.stack)
                self.cards.append({"name": "", "links": [], "jpegs": 0, "_h3": False})
            if tag == "h3" and self.card_depth:
                self.cards[-1]["_h3"] = True
            if tag == "a":
                self._anchor = [a.get("href", ""), []]

    def handle_startendtag(self, tag, attrs):
        self._element(tag, {k: (v or "") for k, v in attrs})

    def _element(self, tag, a):
        for k in TEXT_ATTRS:
            if a.get(k):
                self.extra_text.append(a[k])
        if tag == "meta":
            self.metas.append(a)
            if a.get("content") and (a.get("name") in ("description", "twitter:title", "twitter:description")
                                     or a.get("property", "").startswith("og:")):
                self.extra_text.append(a["content"])
        if tag == "link":
            self.links.append(a)
        if self.people_depth:
            n = 1 if tag == "img" and a.get("src", "").startswith("people/") and a.get("src", "").endswith(".jpg") else 0
            self.people_jpegs += n
            if self.card_depth:
                self.cards[-1]["jpegs"] += n

    def handle_endtag(self, tag):
        if tag == "a" and self._anchor is not None:
            href, parts = self._anchor
            text = " ".join("".join(parts).split())
            self.anchors.append((href, text))
            if self.card_depth:
                self.cards[-1]["links"].append((text, href))
            self._anchor = None
        if tag == "h3" and self.card_depth:
            self.cards[-1]["_h3"] = False
        if not any(t == tag for t, _ in self.stack):
            return
        while self.stack:
            t, _ = self.stack.pop()
            if self.card_depth and len(self.stack) < self.card_depth:
                self.card_depth = None
            if self.people_depth and len(self.stack) < self.people_depth:
                self.people_depth = None
            if t == tag:
                break

    def handle_data(self, data):
        if self._in("script") or self._in("style"):
            return
        if self._in("title"):
            self.title += data
            self.extra_text.append(data)
            return
        if self._in("head"):
            return
        self.body_text.append(data)
        if self._anchor is not None:
            self._anchor[1].append(data)
        if self.card_depth and self.cards[-1]["_h3"]:
            self.cards[-1]["name"] += data

    def meta(self, key):
        for m in self.metas:
            if m.get("name") == key or m.get("property") == key:
                return m.get("content")
        return None

    def link(self, rel):
        return [l for l in self.links if rel in l.get("rel", "").split()]


def norm(s):
    return " ".join(s.split())


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


# ---------------------------------------------------------------------------------------------- static checks

def static_checks(html, page):
    text = norm(" ".join(page.body_text))
    corpus = text + " " + norm(" ".join(page.extra_text))

    row("No em dash in visible text", EM_DASH not in corpus, f"{corpus.count(EM_DASH)} found")
    bangs = [m.start() for m in re.finditer("!", corpus)]
    row("No exclamation mark in visible text", not bangs,
        f"{len(bangs)} found, first near: {corpus[max(0, bangs[0] - 40):bangs[0] + 10]!r}" if bangs else "")
    found = [w for w in BANNED if w.lower() in corpus.lower()]
    row("No banned words in visible text", not found, ", ".join(found))

    n = text.count(HERO_LINE)
    row("Hero line appears exactly once", n == 1, f"found {n} times")

    desc = page.meta("description")
    row("Description meta is DESCRIPTION and under 160 characters", desc == felagsite.DESCRIPTION and len(desc or "") <= 160,
        f"description meta is {len(desc or '')} characters")
    row("Statement appears in visible text", felagsite.STATEMENT in text, "STATEMENT not found in the page text")

    stale = re.findall(r"href\s*=\s*[\"']?#book\b", html)
    row("No href to #book", not stale, f"{len(stale)} left")
    mails = re.findall(r"mailto:[^\"'\s<>]*", html)
    other = sorted({m for m in mails if m != MAILTO})
    row("Every mailto is info@felag.net", bool(mails) and not other,
        ", ".join(other) if other else "no mailto found")

    row("Four portraits in #people", page.people_jpegs == 4, f"{page.people_jpegs} portrait files inside #people")
    no_photo = [c["name"].strip() for c in page.cards if c["jpegs"] != 1]
    if no_photo:
        row("Each People card has its portrait", False, ", ".join(no_photo))

    problems = []
    source = {p["name"]: list(p["links"]) for p in felagsite.PEOPLE}
    for name, labels in PEOPLE_LINKS.items():
        if name not in source:
            problems.append(f"{name} missing from PEOPLE")
        elif [l for l, _ in source[name]] != labels:
            problems.append(f"{name} in PEOPLE has {[l for l, _ in source[name]]}, expected {labels}")
    extra = sorted(set(source) - set(PEOPLE_LINKS))
    if extra:
        problems.append("unexpected in PEOPLE: " + ", ".join(extra))
    rendered = {norm(c["name"]): c["links"] for c in page.cards}
    if sorted(rendered) != sorted(source):
        problems.append(f"cards on the page: {sorted(rendered)}")
    for name, links in source.items():
        if name in rendered and rendered[name] != links:
            problems.append(f"{name} card shows {rendered[name]}")
    row("People cards carry exactly the PEOPLE links", not problems, "; ".join(problems))

    canon = [l.get("href") for l in page.link("canonical")]
    row("Head: canonical", canon == [SITE], f"canonical is {canon}")
    row("Head: og:image", page.meta("og:image") == SITE + "og.png", f"og:image is {page.meta('og:image')!r}")
    icons = [l.get("href") for l in page.link("icon")]
    row("Head: favicon", "/favicon.svg" in icons, f"icon links {icons}")
    row("Head: theme-color", (page.meta("theme-color") or "").upper() == "#0E1114",
        f"theme-color is {page.meta('theme-color')!r}")
    want = {"og:type": "website", "og:site_name": "Felag", "og:title": norm(page.title), "og:description": desc,
            "og:url": SITE, "og:image:width": "1200", "og:image:height": "630",
            "twitter:card": "summary_large_image", "twitter:site": "@Felagnet"}
    bad = [k for k, v in want.items() if page.meta(k) != v]
    touch = [l.get("href") for l in page.link("apple-touch-icon")]
    if touch != ["/apple-touch-icon.png"]:
        bad.append("apple-touch-icon")
    row("Head: Open Graph, Twitter and touch icon", not bad, ", ".join(bad))


def dist_checks():
    missing = [n for n in DIST_FILES if not os.path.isfile(os.path.join(DIST, n))]
    if os.path.exists(os.path.join(DIST, "felag-harvest.html")):
        missing.append("(harvest page must not ship)")
    row("dist/ holds every file", not missing, "missing: " + ", ".join(missing))

    def read(name):
        p = os.path.join(DIST, name)
        return open(p, encoding="utf-8").read() if os.path.isfile(p) else None

    cname = read("CNAME")
    row("CNAME is exactly felag.net", cname is not None and cname.rstrip("\n") == "felag.net"
        and "\n" not in cname.rstrip("\n"), f"CNAME reads {cname!r}")
    sizes = {}
    for name, want in (("og.png", (1200, 630)), ("apple-touch-icon.png", (180, 180))):
        p = os.path.join(DIST, name)
        sizes[name] = png_size(p) if os.path.isfile(p) else None
    bad = [f"{n} is {s}" for n, s in sizes.items() if s != {"og.png": (1200, 630), "apple-touch-icon.png": (180, 180)}[n]]
    row("og.png 1200x630, touch icon 180x180", not bad, "; ".join(bad))

    note = ""
    try:
        root = ET.fromstring(read("sitemap.xml") or "")
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [e.text for e in root.findall("s:url/s:loc", ns)]
        ok = locs == [SITE] and root.find("s:url/s:lastmod", ns) is not None
        note = f"locs {locs}"
    except ET.ParseError as e:
        ok, note = False, f"sitemap.xml does not parse: {e}"
    robots = read("robots.txt") or ""
    if f"Sitemap: {SITE}sitemap.xml" not in robots:
        ok, note = False, "robots.txt lacks the Sitemap line"
    row("robots.txt and sitemap.xml", ok, note)

    fav = read("favicon.svg") or ""
    row("favicon.svg is the copper mark", 'viewBox="0 0 104 104"' in fav and "#DF8E63" in fav
        and felagsite.MARK_PATH in fav, "favicon.svg does not carry the mark path")

    p404 = read("404.html") or ""
    bad = []
    if "That page is not here." not in p404:
        bad.append("line missing")
    if f'href="{SITE}"' not in p404:
        bad.append("no link back")
    if "<script" in p404.lower():
        bad.append("has a script")
    if EM_DASH in p404 or "!" in re.sub(r"<!doctype html>", "", p404, flags=re.I):
        bad.append("em dash or exclamation mark")
    row("404.html", not bad, ", ".join(bad))


# ---------------------------------------------------------------------------------------------- browser pass

CANVAS_STATS = """sel => {
  const c = document.querySelector(sel);
  if (!c || !c.width || !c.height) return {ink: 0, copper: 0, hash: 0};
  const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
  let ink = 0, copper = 0, hash = 0;
  for (let i = 0; i < d.length; i += 4) {
    if (d[i + 3] > 0) ink++;
    if (d[i + 3] === 255 && Math.abs(d[i] - 223) <= 3 && Math.abs(d[i + 1] - 142) <= 3 && Math.abs(d[i + 2] - 99) <= 3) copper++;
    hash = (hash * 31 + d[i] + 3 * d[i + 1] + 7 * d[i + 2] + 11 * d[i + 3]) % 2147483647;
  }
  return {ink, copper, hash};
}"""

SCROLL_STEP = """r => {
  window.scrollTo({top: window.scrollY + Math.round(window.innerHeight * r), behavior: 'instant'});
  return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2;
}"""


def watch(page):
    errors = []
    page.on("pageerror", lambda e: errors.append(f"page error: {e}"))
    page.on("console", lambda m: errors.append(f"console: {m.text}")
            if m.type == "error" and not GL_NOISE.search(m.text) else None)
    return errors


def scroll_to_bottom(page):
    widths = []
    for _ in range(600):
        done = page.evaluate(SCROLL_STEP, 0.8)
        page.wait_for_timeout(100)
        widths.append(page.evaluate("document.documentElement.scrollWidth"))
        if done:
            break
    return widths


def browser_pass():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        row("Browser pass", False, "Playwright is not installed, see README.md")
        return
    url = pathlib.Path(INDEX).as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            for w, h in VIEWPORTS:
                ctx = browser.new_context(viewport={"width": w, "height": h})
                page = ctx.new_page()
                errors = watch(page)
                page.goto(url, wait_until="load")
                page.wait_for_timeout(3000)
                widths = [page.evaluate("document.documentElement.scrollWidth")] + scroll_to_bottom(page)
                page.wait_for_timeout(500)
                row(f"{w}x{h}: load, scroll, no errors", not errors,
                    f"{len(errors)} error(s), first: {errors[0][:160]}" if errors else "")
                if (w, h) == (1440, 900):
                    row("1440x900: no horizontal scroll", max(widths) == 1440, f"scrollWidth reached {max(widths)}")
                ctx.close()

            ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
            page = ctx.new_page()
            errors = watch(page)
            page.goto(url, wait_until="load")
            page.wait_for_timeout(400)
            h1 = page.evaluate(CANVAS_STATS, "#scene")
            arrived = page.evaluate("document.getElementById('root').classList.contains('mark-arrived')")
            page.wait_for_timeout(2500)
            h2 = page.evaluate(CANVAS_STATS, "#scene")
            ok = h1["ink"] > 5000 and h1 == h2 and arrived
            row("Reduced motion: hero finished at once", ok,
                f"ink {h1['ink']}, unchanged {h1 == h2}, header mark shown {arrived}")
            hero_h = page.evaluate("document.getElementById('top').offsetHeight")
            states = []
            for frac in (0.0, 0.6):
                page.evaluate(f"window.scrollTo(0, {int(hero_h * frac)})")
                page.wait_for_timeout(300)
                states.append(page.evaluate(
                    "[parseFloat(getComputedStyle(document.querySelector('.hero-inner')).opacity),"
                    " parseFloat(getComputedStyle(document.getElementById('hero-statement')).opacity)]"))
            ok = states[0][0] > 0.95 and states[0][1] < 0.05 and states[1][0] < 0.05 and states[1][1] > 0.95
            row("Reduced motion: hero text and statement never overlap", ok,
                f"at top hero {states[0][0]:.2f}, statement {states[0][1]:.2f}; at 60% hero {states[1][0]:.2f}, statement {states[1][1]:.2f}")
            page.evaluate("document.getElementById('book').scrollIntoView({block: 'start'})")
            page.wait_for_timeout(400)
            b1 = page.evaluate(CANVAS_STATS, "#book-art")
            page.wait_for_timeout(2500)
            b2 = page.evaluate(CANVAS_STATS, "#book-art")
            ok = b1["copper"] > 5000 and b1["copper"] == b2["copper"]
            row("Reduced motion: closing mark finished at once", ok,
                f"copper pixels {b1['copper']} then {b2['copper']}")
            row("Reduced motion: no errors", not errors,
                f"{len(errors)} error(s), first: {errors[0][:160]}" if errors else "")
            ctx.close()
        finally:
            browser.close()


# ---------------------------------------------------------------------------------------------- links

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = urllib.request.build_opener(_NoRedirect)


def fetch(url, method):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8", "Accept-Language": "en"})
    try:
        with OPENER.open(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def probe(url):
    linkedin = urllib.parse.urlsplit(url).hostname.endswith("linkedin.com")
    last = "no answer"
    for attempt in range(2):
        for method in ("HEAD", "GET"):
            try:
                code = fetch(url, method)
            except Exception as e:  # network errors: one retry after a pause
                last = f"{method}: {type(e).__name__}: {e}"
                continue
            if 200 <= code < 400:
                return True, f"{code} on {method}"
            if code == 999 and linkedin:
                return True, f"999 on {method}, LinkedIn bot answer, accepted"
            last = f"{code} on {method}"
        time.sleep(2)
    return False, last


def link_pass(page):
    urls = []
    for href, _ in page.anchors:
        if href.startswith(("http://", "https://")) and href not in urls:
            urls.append(href)
    for l in page.link("stylesheet"):
        if l.get("href", "").startswith("https://") and l["href"] not in urls:
            urls.append(l["href"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(probe, urls))
    for url, (ok, note) in zip(urls, results):
        row(f"Link {url}", ok, note)


# ---------------------------------------------------------------------------------------------- main

def print_table():
    w1 = max(len(r[0]) for r in ROWS)
    print(f"{'Check'.ljust(w1)}  Result  Note")
    print(f"{'-' * w1}  ------  ----")
    for name, result, note in ROWS:
        show = note if (result != "PASS" or name.startswith("Link ")) else ""
        print(f"{name.ljust(w1)}  {result.ljust(6)}  {show}".rstrip())
    fails = sum(1 for r in ROWS if r[1] == "FAIL")
    print(f"\n{len(ROWS)} checks, {fails} failed, {sum(1 for r in ROWS if r[1] == 'SKIP')} skipped")
    return fails


def main():
    ap = argparse.ArgumentParser(description="Checks dist/ before it ships.")
    ap.add_argument("--no-browser", action="store_true", help="skip the Playwright pass")
    ap.add_argument("--no-links", action="store_true", help="skip the external link pass")
    args = ap.parse_args()

    if not os.path.isfile(INDEX):
        sys.exit("dist/index.html is missing; run python3 build_site.py and python3 make_dist.py first")
    html = open(INDEX, encoding="utf-8").read()
    page = Page()
    page.feed(html)
    page.close()

    static_checks(html, page)
    dist_checks()
    if args.no_browser:
        row("Browser pass", None, "skipped with --no-browser")
    else:
        browser_pass()
    if args.no_links:
        row("External links", None, "skipped with --no-links")
    else:
        link_pass(page)
    sys.exit(1 if print_table() else 0)


if __name__ == "__main__":
    main()

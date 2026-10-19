"""Assemble dist/, the folder GitHub Pages serves: the rune page as index.html, plus CNAME, .nojekyll,
robots.txt, sitemap.xml, llms.txt, favicon.svg, apple-touch-icon.png, og.png, 404.html, the fonts under fonts/ and the portraits under people/.
Standard library only. Run after build_site.py. The harvest page is a kept prototype and is not copied."""

import datetime
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from felagsite import CAPS, FAQ, HOW, LINEAGE, MARK_PATH, OFFERS, PEOPLE, PEOPLE_NOTE, STATEMENT, TURN_DOWN  # noqa: E402
from shared import FONT_FACE, FONT_LINKS, LOCKUP  # noqa: E402

DOMAIN = "felag.net"
SITE = f"https://{DOMAIN}/"
OUT = os.path.join(HERE, "out")
STATIC = os.path.join(HERE, "static")
DIST = os.path.join(HERE, "dist")
FONTS = FONT_LINKS

FAVICON = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 104 104"><path fill="#DF8E63" d="{MARK_PATH}"/></svg>\n'

ROBOTS = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{site}</loc>
    <lastmod>{date}</lastmod>
  </url>
</urlset>
"""

PAGE_404 = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Felag, page not found</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="theme-color" content="#0E1114">
{FONTS}
<style>
{FONT_FACE}
:root{{--bg:#0E1114;--line:#262C31;--text:#E9ECEE;--accent:#DF8E63;--accent-hover:#EFA37C;
  --sans:"Schibsted Grotesk","Helvetica Neue",Helvetica,Arial,sans-serif;--side:clamp(16px,6vw,120px);color-scheme:dark}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:var(--bg);color:var(--text)}}
body{{min-height:100vh;display:flex;flex-direction:column;font-family:var(--sans);font-size:16px;line-height:26px;-webkit-font-smoothing:antialiased}}
header{{height:72px;display:flex;align-items:center;padding:0 var(--side);border-bottom:1px solid var(--line)}}
.lockup{{display:inline-flex}}
.lockup svg{{display:block;height:38px;width:auto}}
.mark-fill{{fill:var(--accent)}}.word-fill{{fill:var(--text)}}
main{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px;padding:96px var(--side)}}
h1{{margin:0;font-size:clamp(40px,5.4vw,80px);line-height:1;font-weight:600;letter-spacing:-0.03em}}
p{{margin:0;font-size:clamp(18px,1.6vw,22px);line-height:1.45}}
a{{color:var(--accent);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}}
a:hover{{color:var(--accent-hover)}}
a:focus-visible{{outline:2px solid var(--accent);outline-offset:3px}}
</style>
</head>
<body>
<header><a class="lockup" href="{SITE}" aria-label="Felag, home">{LOCKUP}</a></header>
<main>
<h1>That page is not here.</h1>
<p><a href="{SITE}">Back to felag.net</a></p>
</main>
</body>
</html>
"""


def last_change():
    """The sitemap's lastmod: the commit date of the last change to the page sources, today if git is unavailable."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", "felagsite.py", "shared.py", "build_site.py",
                              "hero8-rune.js", "static", "photo/people"], cwd=HERE, capture_output=True, text=True, timeout=10)
        d = out.stdout.strip()
        return d if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) else datetime.date.today().isoformat()
    except Exception:
        return datetime.date.today().isoformat()


def llms_txt():
    """A plain-text summary for answer engines, built from the page constants so it cannot drift from the page."""
    lines = ["# Felag", "", f"> {STATEMENT}", "",
             "Senior engineers who own the architecture and ship to production. A principal-led studio for technology companies, "
             "priced on outcomes rather than hours.", "", PEOPLE_NOTE, "",
             "## What we build", ""]
    lines += [f"- {c['name']}: {c['line']}" for c in CAPS]
    lines += ["", "## Where the team comes from", ""]
    lines += [f"- {y}: {tx}" for y, tx in LINEAGE]
    lines += ["", "## What it costs", "", "Prices in USD, excluding VAT.", ""]
    for o in OFFERS:
        note = f", {o['note']}" if o["note"] else ""
        lines.append(f"- {o['name']}: {o['price']}{note}. {o['body']}")
    lines += ["", "## How an engagement runs", ""]
    for name, output, line in HOW:
        lines.append(f"- {name}: {output} {line}")
    lines += ["", "## What we turn down", "", TURN_DOWN, "", "## The people who lead the work", ""]
    for p in PEOPLE:
        where = f", {p['where'][0].lower() + p['where'][1:]}" if p["where"] else ""
        lines.append(f"- {p['name']}, {p['role']}{where}. {p['bio']}")
    lines += ["", "## Questions", ""]
    for q, a in FAQ:
        lines.append(f"- {q} {a}")
    lines += ["", "## Contact", "",
              "- Email: info@felag.net (start with a free technical workshop with a founder)",
              f"- Site: {SITE}",
              "- LinkedIn: https://www.linkedin.com/company/felagnet/",
              "- GitHub: https://github.com/felagnet",
              "- X: https://x.com/felagnet", ""]
    return "\n".join(lines)


def write(name, text):
    with open(os.path.join(DIST, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    page = os.path.join(OUT, "felag-rune.html")
    if not os.path.exists(page):
        sys.exit("out/felag-rune.html is missing; run python3 build_site.py first")
    images = [os.path.join(STATIC, n) for n in ("apple-touch-icon.png", "og.png")]
    for img in images:
        if not os.path.exists(img):
            sys.exit(f"{os.path.relpath(img, HERE)} is missing; run python3 make_images.py first")

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copyfile(page, os.path.join(DIST, "index.html"))
    for img in images:
        shutil.copyfile(img, os.path.join(DIST, os.path.basename(img)))
    people = os.path.join(OUT, "people")
    if not os.path.isdir(people):
        sys.exit("out/people is missing; run python3 build_site.py first")
    shutil.copytree(people, os.path.join(DIST, "people"))
    shutil.copytree(os.path.join(STATIC, "fonts"), os.path.join(DIST, "fonts"))
    write("CNAME", DOMAIN)
    write(".nojekyll", "")
    write("robots.txt", ROBOTS)
    write("sitemap.xml", SITEMAP.format(site=SITE, date=last_change()))
    write("llms.txt", llms_txt())
    write("favicon.svg", FAVICON)
    write("404.html", PAGE_404)
    for root, _, files in sorted(os.walk(DIST)):
        for name in sorted(files):
            p = os.path.join(root, name)
            print(os.path.relpath(p, HERE), os.path.getsize(p))


if __name__ == "__main__":
    main()

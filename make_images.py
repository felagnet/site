"""Render the two raster images the site needs into static/: og.png (1200 by 630, the link preview) and
apple-touch-icon.png (180 by 180). Each is a small HTML page drawn by Chromium through Playwright at device
scale 1. Run it again when the mark, the lockup or the hero line changes; make_dist.py copies the results
into dist/. Needs Playwright with Chromium, see README.md."""

import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from felagsite import MARK_PATH  # noqa: E402
from shared import LOCKUP  # noqa: E402

STATIC = os.path.join(HERE, "static")
HERO_LINE = "Senior engineers who own the architecture and ship to production."
BG, COPPER, TEXT = "#0E1114", "#DF8E63", "#E9ECEE"
FONT_CSS = "https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@600&display=block"

# The lockup top left, the hero line across the lower half, and the mark large on the right, cut by the
# right edge, on the soft copper light the closing scene uses.
OG_HTML = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="{FONT_CSS}">
<style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:{BG}}}
body{{position:relative}}
.halo{{position:absolute;left:520px;top:-150px;width:1100px;height:930px;background:radial-gradient(closest-side,rgba(223,142,99,.12),rgba(223,142,99,0))}}
.lockup{{position:absolute;left:72px;top:64px}}
.lockup svg{{display:block;height:48px;width:auto;overflow:visible}}
.mark-fill{{fill:{COPPER}}}.word-fill{{fill:{TEXT}}}
h1{{position:absolute;left:72px;bottom:68px;width:700px;margin:0;color:{TEXT};font-family:"Schibsted Grotesk",sans-serif;
   font-weight:600;font-size:56px;line-height:1.05;letter-spacing:-0.03em;text-wrap:balance}}
.mark{{position:absolute;left:838px;top:60px;width:510px;height:510px}}
</style></head>
<body>
<div class="halo"></div>
<div class="lockup">{LOCKUP}</div>
<h1>{HERO_LINE}</h1>
<svg class="mark" viewBox="0 0 104 104" aria-hidden="true"><path fill="{COPPER}" d="{MARK_PATH}"></path></svg>
</body></html>"""

TOUCH_HTML = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<style>html,body{{margin:0;width:180px;height:180px;overflow:hidden;background:{BG}}}
svg{{position:absolute;left:36px;top:36px;width:108px;height:108px}}</style></head>
<body><svg viewBox="0 0 104 104" aria-hidden="true"><path fill="{COPPER}" d="{MARK_PATH}"></path></svg></body></html>"""


def render(browser, html, width, height, out, needs_font=False):
    ctx = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=1)
    page = ctx.new_page()
    page.set_content(html, wait_until="networkidle")
    if needs_font:
        page.evaluate("document.fonts.ready")
        if not page.evaluate("document.fonts.check('600 56px \"Schibsted Grotesk\"')"):
            sys.exit("Schibsted Grotesk did not load from Google Fonts; og.png not written")
    page.screenshot(path=out, clip={"x": 0, "y": 0, "width": width, "height": height})
    ctx.close()
    print(os.path.relpath(out, HERE), width, "by", height)


def main():
    os.makedirs(STATIC, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        render(browser, OG_HTML, 1200, 630, os.path.join(STATIC, "og.png"), needs_font=True)
        render(browser, TOUCH_HTML, 180, 180, os.path.join(STATIC, "apple-touch-icon.png"))
        browser.close()


if __name__ == "__main__":
    main()

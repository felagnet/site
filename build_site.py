import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from felagsite import full_page

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
local = "--local" in sys.argv
THREE_CDN = '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
THREE_LOCAL = '<script src="../lib/three.min.js"></script>'
three = THREE_LOCAL if local else THREE_CDN

def js(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()

pages = {
  "felag-rune.html": full_page(
    theme="rune",
    title="Felag | Backend, payments and identity engineering, priced on outcomes",
    description_line="A single rune. It draws itself, then ignites. Then scroll.",
    headline="Senior engineers who own the architecture and ship to production.",
    sub="A principal-led studio for technology companies, priced on outcomes rather than hours.",
    scene_markup='<canvas id="scene" class="scene" aria-hidden="true"></canvas><div class="vignette" aria-hidden="true"></div>',
    scene_script=js("hero8-rune.js"),
    extra_css=".vignette{position:absolute;inset:0;pointer-events:none;background:radial-gradient(120% 100% at 72% 50%,rgba(var(--iron-rgb),0) 45%,rgba(var(--iron-rgb),.7) 100%)}"),
  "felag-harvest.html": full_page(
    theme="harvest",
    title="Felag, the work is measured at the harvest, not by the hour",
    description_line="The field and the cut. The mouse is the wind. Then scroll.",
    headline="The work is measured at the harvest, not by the hour.",
    sub="Senior engineers who own the architecture and ship it to production, for technology companies.",
    scene_markup='<canvas id="scene" class="scene" aria-hidden="true"></canvas><div class="veil-left" aria-hidden="true"></div>',
    scene_script=js("hero6-field.js"),
    extra_css=".veil-left{position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(14,17,20,.86) 0%,rgba(14,17,20,.55) 34%,rgba(14,17,20,0) 60%)}@media (max-width:900px){.veil-left{background:linear-gradient(180deg,rgba(14,17,20,.82) 0%,rgba(14,17,20,.45) 45%,rgba(14,17,20,0) 70%)}}",
    scripts_before=three),
}
# the portraits, as files next to the page
PEOPLE_DIR = os.path.join(OUT, "people"); os.makedirs(PEOPLE_DIR, exist_ok=True)
for fn in sorted(os.listdir(os.path.join(HERE, "photo", "people"))):
    if fn.endswith((".jpg", ".webp")) and not fn.endswith("-src.jpg"):
        with open(os.path.join(HERE, "photo", "people", fn), "rb") as src, open(os.path.join(PEOPLE_DIR, fn), "wb") as dst:
            dst.write(src.read())
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(name, os.path.getsize(os.path.join(OUT, name)))

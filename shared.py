"""Shared page chrome for the three Felag hero prototypes. Each hero supplies its title, headline,
sub-line, scene markup and scene script; this file supplies header, strip, proof, closing and CSS."""

LOCKUP = '''<svg viewBox="0 0 451.76 143.17" role="img" aria-label="Felag" focusable="false"><g transform="translate(0 10.400)"><path class="mark-fill" d="M0 0H32V104H0Z M44 0H66L44 22Z M44 38L82 0H104L44 60Z M44 76L104 16V104H44Z"></path><g transform="translate(136 104) scale(0.069333 -0.069333)"><path class="word-fill" d="M150 0V1254Q150 1384 213.5 1442.0Q277 1500 422 1500H606V1312H451Q421 1312 409.5 1299.5Q398 1287 398 1256V0ZM0 892V1080H615V892Z M1213.04 -25Q1056.04 -25 935.04 44.0Q814.04 113 745.04 240.0Q676.04 367 676.04 540Q676.04 713 744.04 840.0Q812.04 967 932.04 1036.0Q1052.04 1105 1209.04 1105Q1297.04 1105 1386.54 1078.0Q1476.04 1051 1550.54 982.5Q1625.04 914 1671.04 793.5Q1717.04 673 1717.04 488H835.04V645H1497.04L1459.04 588Q1453.04 709 1417.54 782.5Q1382.04 856 1326.54 889.5Q1271.04 923 1203.04 923Q1117.04 923 1058.04 876.5Q999.04 830 968.54 743.5Q938.04 657 938.04 539Q938.04 363 1007.04 263.5Q1076.04 164 1211.04 164Q1303.04 164 1368.04 211.0Q1433.04 258 1465.04 351L1695.04 287Q1656.04 182 1584.04 113.0Q1512.04 44 1416.04 9.5Q1320.04 -25 1213.04 -25ZM1244.04 1201 1102.04 1282 1288.04 1650 1493.04 1524Z M2115.08 0Q2016.08 0 1958.08 52.5Q1900.08 105 1900.08 197V1500H2148.08V244Q2148.08 210 2157.58 199.0Q2167.08 188 2198.08 188H2289.08V0Z M2744.12 -25Q2639.12 -25 2555.12 13.0Q2471.12 51 2422.12 123.5Q2373.12 196 2373.12 297Q2373.12 406 2436.62 487.5Q2500.12 569 2624.62 614.0Q2749.12 659 2933.12 659H3095.12L3077.12 635V696Q3077.12 812 3033.12 871.0Q2989.12 930 2887.12 930Q2790.12 930 2738.12 879.0Q2686.12 828 2678.12 738L2419.12 787Q2432.12 876 2491.62 948.0Q2551.12 1020 2654.12 1063.0Q2757.12 1106 2902.12 1106Q3040.12 1106 3133.12 1059.0Q3226.12 1012 3272.62 913.5Q3319.12 815 3319.12 659V244Q3319.12 210 3328.62 199.0Q3338.12 188 3369.12 188H3423.12V0H3294.12Q3196.12 0 3141.12 52.5Q3086.12 105 3086.12 197V258L3128.12 246Q3114.12 203 3087.12 156.0Q3060.12 109 3015.12 68.0Q2970.12 27 2903.62 1.0Q2837.12 -25 2744.12 -25ZM2812.12 154Q2887.12 154 2947.62 189.5Q3008.12 225 3043.62 298.5Q3079.12 372 3079.12 484V502H2937.12Q2820.12 502 2754.12 471.5Q2688.12 441 2661.12 396.5Q2634.12 352 2634.12 308Q2634.12 270 2651.62 234.5Q2669.12 199 2708.12 176.5Q2747.12 154 2812.12 154Z M4000.16 -415Q3746.16 -415 3624.66 -346.5Q3503.16 -278 3503.16 -135Q3503.16 -50 3546.66 8.0Q3590.16 66 3677.16 95Q3640.16 120 3617.66 159.0Q3595.16 198 3595.16 244Q3595.16 303 3632.16 348.5Q3669.16 394 3737.16 414Q3658.16 462 3613.66 541.5Q3569.16 621 3569.16 725Q3569.16 840 3624.66 925.5Q3680.16 1011 3780.66 1058.0Q3881.16 1105 4017.16 1105Q4153.16 1105 4254.16 1058.0Q4355.16 1011 4411.16 925.5Q4467.16 840 4467.16 723Q4467.16 609 4411.66 524.0Q4356.16 439 4254.16 392.0Q4152.16 345 4015.16 345H3934.16Q3825.16 345 3825.16 284Q3825.16 225 3933.16 225H4151.16Q4268.16 225 4346.16 197.0Q4424.16 169 4469.66 123.0Q4515.16 77 4534.66 20.0Q4554.16 -37 4554.16 -95Q4554.16 -258 4430.16 -336.5Q4306.16 -415 4047.16 -415ZM4004.16 -247H4050.16Q4302.16 -247 4302.16 -96Q4302.16 -36 4257.66 3.5Q4213.16 43 4099.16 43H3941.16Q3864.16 43 3807.66 9.5Q3751.16 -24 3751.16 -102Q3751.16 -175 3813.16 -211.0Q3875.16 -247 4004.16 -247ZM4017.16 505Q4120.16 505 4175.16 562.0Q4230.16 619 4230.16 723Q4230.16 827 4175.16 885.5Q4120.16 944 4017.16 944Q3915.16 944 3860.16 886.0Q3805.16 828 3805.16 723Q3805.16 619 3860.16 562.0Q3915.16 505 4017.16 505ZM4184.16 966V1075Q4184.16 1167 4242.16 1219.5Q4300.16 1272 4399.16 1272H4513.16V1084H4398.16Q4367.16 1084 4357.66 1073.0Q4348.16 1062 4348.16 1028V966Z"></path></g></g></svg>'''

CSS = '''
:root{
  --bg:#0E1114;--surface:#151A1E;--line:#262C31;--line-strong:#616A71;--text:#E9ECEE;--text-secondary:#98A1A8;
  --accent:#DF8E63;--accent-hover:#EFA37C;--on-accent:#0E1114;--copper-deep:#8C4E2C;--steel:#7C93A6;
  --sans:"Schibsted Grotesk","Helvetica Neue",Helvetica,Arial,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  --side:clamp(16px,6vw,120px);--head:72px;
  color-scheme:dark;
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);font-size:16px;line-height:26px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,p{margin:0}
a{color:var(--accent);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px;transition:color .15s,background-color .15s}
a:hover{color:var(--accent-hover)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.wrap{padding:0 var(--side);max-width:1440px;margin:0 auto}
.skip{position:absolute;left:16px;top:-80px;padding:8px 12px;background:var(--surface);border:1px solid var(--line-strong);border-radius:2px;color:var(--text);z-index:30}
.skip:focus{top:16px}
.btn{display:inline-flex;align-items:center;justify-content:center;height:52px;padding:0 28px;background:var(--accent);color:var(--on-accent);border-radius:2px;font-size:16px;font-weight:500;letter-spacing:-0.005em;text-decoration:none;white-space:nowrap}
.btn:hover{background:var(--accent-hover);color:var(--on-accent)}
.btn-sm{height:44px;padding:0 20px;font-size:15px}
.textlink{font-size:16px;font-weight:500}
.site-header{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--bg);border-bottom:1px solid var(--line);transition:background-color .4s,border-color .4s}
.over-hero .site-header{background:linear-gradient(180deg,rgba(14,17,20,.92) 0%,rgba(14,17,20,.55) 70%,rgba(14,17,20,0) 100%);border-color:transparent}
.mark-pending .site-header .mark-fill{opacity:0;transition:opacity .5s}
.mark-arrived .site-header .mark-fill{opacity:1}
.site-header .wrap{display:flex;align-items:center;justify-content:space-between;height:var(--head)}
.lockup{display:inline-flex;color:var(--text)}
.lockup svg{display:block;height:38px;width:auto}
.mark-fill{fill:var(--accent)}.word-fill{fill:var(--text)}
.nav{display:flex;align-items:center;gap:36px}
.nav a{font-size:15px;font-weight:500;color:var(--text-secondary);text-decoration:none}
.nav a:hover{color:var(--text)}
.nav a.btn,.nav a.btn:hover{color:var(--on-accent)}

/* Hero: a pinned scene with a scroll runway under it */
.hero{position:relative;height:230vh;min-height:1800px}
.hero-pin{position:sticky;top:0;height:100vh;min-height:700px;overflow:hidden;margin-top:calc(-1 * var(--head))}
.hero-pin .hero-inner{padding-top:var(--head)}
.scene{position:absolute;inset:0;width:100%;height:100%;display:block}
.hero-inner{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;gap:28px;padding-bottom:110px;pointer-events:none;will-change:opacity,transform}
.hero-inner > *{pointer-events:auto}
.hero h1{font-size:clamp(40px,5.4vw,80px);line-height:1;font-weight:600;letter-spacing:-0.03em;max-width:13ch;text-wrap:balance}
.hero .sub{font-size:clamp(18px,1.6vw,22px);line-height:1.45;color:var(--text-secondary);max-width:27em}
.cta{display:flex;align-items:center;gap:36px;flex-wrap:wrap}
.strip{position:absolute;left:0;right:0;bottom:0;z-index:2;border-top:1px solid var(--line);background:var(--bg);padding:14px var(--side);display:flex;flex-direction:column;gap:4px;font-size:15px;line-height:22px}
.strip div{display:flex;flex-wrap:wrap;gap:4px 28px}
.strip .role{color:var(--text-secondary)}
.strip .stances{font-weight:500}
.story{position:absolute;left:var(--side);bottom:120px;z-index:2;display:flex;flex-direction:column;gap:10px;font-family:var(--mono);font-size:13px;line-height:18px;color:var(--text-secondary);opacity:0;transform:translateY(12px);transition:opacity .4s,transform .4s}
.story.on{opacity:1;transform:none}
.story b{font-weight:400;color:var(--text)}
.story .k{display:inline-block;width:7px;height:7px;background:var(--accent);margin-right:12px;vertical-align:1px}
.phases{position:absolute;left:var(--side);bottom:120px;z-index:2;display:flex;gap:28px;font-family:var(--mono);font-size:13px;color:var(--text-secondary)}
.phases span{transition:color .3s}.phases span.on{color:var(--accent)}
.hint{position:absolute;right:var(--side);bottom:96px;z-index:2;font-family:var(--mono);font-size:12px;color:var(--text-secondary);letter-spacing:.02em}

/* load choreography */
.rise{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}
.rise.r1{animation-delay:1.1s}.rise.r2{animation-delay:1.35s}.rise.r3{animation-delay:1.55s}.rise.r4{animation-delay:1.8s}
@keyframes rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}

/* sections */
.section{padding:96px 0;border-top:1px solid var(--line)}
.eyebrow{font-family:var(--mono);font-size:12px;color:var(--text-secondary);letter-spacing:.04em;margin-bottom:24px}
.section h2{font-size:clamp(32px,4vw,56px);line-height:1.05;font-weight:600;letter-spacing:-0.025em;max-width:16ch;text-wrap:balance}
.proof-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin-top:56px}
.metric{padding:32px 0 0;border-top:1px solid var(--line-strong);display:flex;flex-direction:column;gap:16px}
.metric .big{font-size:clamp(56px,7vw,112px);line-height:.95;font-weight:600;letter-spacing:-0.035em;font-variant-numeric:tabular-nums lining-nums;color:var(--text);min-height:1em}
.metric .big em{font-style:normal;color:var(--accent)}
.metric .label{font-family:var(--mono);font-size:13px;color:var(--text-secondary)}
.metric p{color:var(--text);max-width:34em}
.metric .wordmark{font-size:20px;font-weight:600;letter-spacing:-0.02em;color:var(--text-secondary)}
.reveal{opacity:1;transform:none;transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.js .reveal:not(.in){opacity:0;transform:translateY(28px)}
.closing{padding:120px 0;border-top:1px solid var(--line)}
.closing .inner{display:grid;grid-template-columns:200px minmax(0,1fr);gap:48px;align-items:start}
.closing .bigmark{width:136px;height:136px}
.closing p{margin-top:20px;font-size:18px}
.closing .cta{margin-top:32px}
.foot{border-top:1px solid var(--line);padding:32px var(--side);font-size:14px;color:var(--text-secondary);display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}
@media (max-width:900px){
  .story,.phases{display:none}
  .proof-grid{grid-template-columns:minmax(0,1fr)}
  .closing .inner{grid-template-columns:minmax(0,1fr)}
  .nav .links{display:none}
  .hero{height:200vh;min-height:1400px}
  .hero-inner{padding-bottom:150px;justify-content:flex-start;padding-top:36px}
  .hero h1{max-width:none}
  .strip div{gap:2px 16px}
  .hint{display:none}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .rise{animation:none}
  .js .reveal:not(.in){opacity:1;transform:none}
  .reveal{transition:none}
}
'''

def header():
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="lockup" href="#top" aria-label="Felag, home">{LOCKUP}</a>
    <nav class="nav" aria-label="Page sections">
      <div class="links nav"><a href="#proof">Proof</a><a href="#offer">Offer</a><a href="#people">People</a><a href="#contracting">Contracting</a></div>
      <a class="btn btn-sm" href="#book">Book a call</a>
    </nav>
  </div>
</header>'''

STRIP = '''<div class="strip" aria-label="At a glance">
  <div><span>Andrew Skurlatov<span class="role">, CTO</span></span><span>Mikhail Manko<span class="role">, CEO</span></span><span>Pavel Dodonov<span class="role">, Principal Engineer</span></span><span>Andrey Solovov<span class="role">, Principal Engineer</span></span></div>
  <div class="stances"><span>Architecture Sprint from $7.5k</span><span>Fractional CTO from $4k a month</span><span>We do not bill hours</span></div>
</div>'''

PROOF = '''<section class="section" id="proof">
  <div class="wrap">
    <p class="eyebrow reveal">Proof</p>
    <h2 class="reveal">What we shipped, dated and measured.</h2>
    <div class="proof-grid">
      <article class="metric reveal">
        <div class="big" data-count="140" data-suffix="k+" data-prefix="">140<em>k+</em></div>
        <div class="label">requests per second, in production</div>
        <p>We designed the RPC proxy that served 140k+ requests per second in production for a major browser wallet and a leading DEX aggregator.</p>
      </article>
      <article class="metric reveal">
        <div class="big" data-count="2024" data-prefix="" data-suffix="">2024</div>
        <div class="label">Wirex Pay, launched August 2024</div>
        <p>We delivered, end to end, the Wirex Pay platform: a Polygon CDK validium chain listed on L2BEAT, with the application layer behind a non-custodial debit card programme, built for MiCA alignment.</p>
        <div class="wordmark">Wirex Pay</div>
      </article>
      <article class="metric reveal">
        <div class="big" data-type="XIP-9">XIP-9</div>
        <div class="label">approved governance proposal, December 2023</div>
        <p>We built the event infrastructure and backend for Infinex, the Synthetix front-end, under governance proposal XIP-9.</p>
        <div class="wordmark">Infinex</div>
      </article>
    </div>
  </div>
</section>'''

CLOSING = '''<section class="closing" id="book">
  <div class="wrap">
    <div class="inner">
      <svg class="bigmark" viewBox="0 0 104 104" aria-hidden="true"><path class="mark-fill" d="M0 0H32V104H0Z M44 0H66L44 22Z M44 38L82 0H104L44 60Z M44 76L104 16V104H44Z"></path></svg>
      <div>
        <h2 class="reveal">Talk to a founder</h2>
        <p class="reveal">Book a call, or write to andskur@felag.net or ms@felag.net.</p>
        <div class="cta reveal"><a class="btn" href="#book">Book a call</a></div>
      </div>
    </div>
  </div>
</section>
<footer class="foot"><span>Felag, hero prototype, 24 September 2026</span><span>Proof, offer, people, contracting: sections to follow the chosen hero.</span></footer>'''

COMMON_JS = '''
document.documentElement.classList.add('js');
var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
// reveal on scroll
(function(){
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || reduce) { els.forEach(function(e){ e.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){ if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, {threshold: 0.2});
  els.forEach(function(e){ io.observe(e); });
})();
// count-up metrics
(function(){
  var ms = document.querySelectorAll('.metric .big[data-count]');
  if (reduce || !('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (!en.isIntersecting) return; io.unobserve(en.target);
      var el = en.target, end = parseInt(el.getAttribute('data-count'),10), suf = el.getAttribute('data-suffix')||'', t0 = null;
      var start = end > 1000 ? end - 40 : 0, dur = 1400;
      function step(ts){ if(!t0) t0=ts; var p=Math.min(1,(ts-t0)/dur); var e=1-Math.pow(1-p,3); var v=Math.round(start+(end-start)*e);
        el.innerHTML = v + (suf ? '<em>'+suf+'</em>' : ''); if(p<1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    });
  }, {threshold: 0.6});
  ms.forEach(function(m){ io.observe(m); });
})();
var heroInner = document.querySelector('.hero-inner');
function fadeText(p){
  var o = 1 - Math.max(0, Math.min(1, (p-0.12)/0.3));
  heroInner.style.opacity = o; heroInner.style.transform = 'translateY(' + (-40*(1-o)).toFixed(1) + 'px)';
  heroInner.style.pointerEvents = o < 0.3 ? 'none' : '';
}
// scroll progress inside the hero runway, 0 to 1
var rootEl = document.getElementById('root');
function headerOver(p){ rootEl.classList.toggle('over-hero', p < 0.06); }
function heroProgress(){
  var hero = document.getElementById('top');
  var r = hero.getBoundingClientRect();
  var head = 72;
  var runway = hero.offsetHeight - window.innerHeight;
  var p = -r.top / Math.max(1, runway);
  p = Math.max(0, Math.min(1, p)); headerOver(p);
  return p;
}
'''

def page(title, description_line, headline, sub, scene_markup, scene_script, extra_css="", scripts_before="", body_class=""):
    return f'''<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&family=Schibsted+Grotesk:wght@400;500;600&display=swap">
<style>{CSS}{extra_css}</style>
<div class="{body_class}" id="root">
{header()}
<main id="main">
<section class="hero" id="top">
  <div class="hero-pin">
    {scene_markup}
    <div class="wrap hero-inner">
      <h1 class="rise r1">{headline}</h1>
      <p class="sub rise r2">{sub}</p>
      <div class="cta rise r3"><a class="btn" href="#book">Book a call</a><a class="textlink" href="#offer">See prices</a></div>
    </div>
    <div class="hint rise r4">{description_line}</div>
    {STRIP}
  </div>
</section>
{PROOF}
{CLOSING}
</main>
</div>
{scripts_before}
<script>
{COMMON_JS}
{scene_script}
</script>
'''

// Hero H, third cut: the rune draws itself stroke by stroke, ignites once, then holds a calm light.
// On scroll it shrinks and flies into the header, where it becomes the mark. No particles, only thin ember streaks at the tip.
(function(){
  var canvas = document.getElementById('scene'), ctx = canvas.getContext('2d');
  var pin = canvas.parentElement, W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
  // the bloom is drawn and blurred at half the CSS resolution, then laid over the full-resolution rune: a blur hides the
  // lost detail, and a full-viewport blur at device resolution was most of the page's main-thread work on a phone
  var GQ = 0.5, glowC = document.createElement('canvas'), gctx = glowC.getContext('2d'), blurC = document.createElement('canvas'), bctx = blurC.getContext('2d');
  var hasFilter = ('filter' in ctx) && (function(){ try { ctx.filter = 'blur(1px)'; var ok = ctx.filter === 'blur(1px)'; ctx.filter = 'none'; return ok; } catch(e){ return false; } })();
  try { ctx.imageSmoothingQuality = 'high'; gctx.imageSmoothingQuality = 'high'; } catch(e){}
  // Safari has no canvas filter, so there the glow is blurred with a canvas shadow instead, on a canvas at CSS resolution
  var softC = document.createElement('canvas'), sctx = softC.getContext('2d');
  var root = document.getElementById('root');
  var lockup = document.querySelector('.site-header .lockup svg');

  // the rune, centred: stem and two branches rising to the right. In mark units the point (x, y) is (x + 30, y + 49).
  var strokes = [
    {a: [-14, 55], b: [-14, -49]},
    {a: [-14, 21], b: [30, -23]},
    {a: [-14, -11], b: [30, -55]}
  ];
  strokes.forEach(function(s){ s.len = Math.hypot(s.b[0]-s.a[0], s.b[1]-s.a[1]); });
  var total = strokes.reduce(function(a, s){ return a + s.len; }, 0);
  var SCHED = [{t0: 0.7, d: 1.05}, {t0: 2.25, d: 0.7}, {t0: 3.4, d: 0.7}];
  var T_IGNITE = SCHED[2].t0 + SCHED[2].d + 0.35, IGNITE_D = 0.75;
  function clamp(x){ return Math.max(0, Math.min(1, x)); }
  function easeIO(x){ return x < 0.5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3)/2; }
  function progress(t){
    var upto = 0, active = -1;
    for (var i = 0; i < strokes.length; i++){
      var f = clamp((t - SCHED[i].t0)/SCHED[i].d);
      if (f > 0 && f < 1) active = i;
      upto += strokes[i].len*easeIO(f);
    }
    return {upto: upto, active: active};
  }
  function runePoint(d){
    for (var i = 0; i < strokes.length; i++){ var s = strokes[i]; if (d <= s.len){ var f = d/s.len; return {x: s.a[0] + (s.b[0]-s.a[0])*f, y: s.a[1] + (s.b[1]-s.a[1])*f, dx: (s.b[0]-s.a[0])/s.len, dy: (s.b[1]-s.a[1])/s.len}; } d -= s.len; }
    var l = strokes[strokes.length-1]; return {x: l.b[0], y: l.b[1], dx: 0, dy: -1};
  }
  function tracePath(c, upto){
    var d = upto;
    for (var i = 0; i < strokes.length; i++){
      var s = strokes[i]; if (d <= 0) break;
      var f = Math.min(1, d/s.len);
      c.moveTo(s.a[0], s.a[1]); c.lineTo(s.a[0] + (s.b[0]-s.a[0])*f, s.a[1] + (s.b[1]-s.a[1])*f);
      d -= s.len;
    }
  }
  function drawRune(c, upto, width, color, alpha, comp){
    c.save(); c.globalCompositeOperation = comp || 'source-over'; c.globalAlpha = clamp(alpha);
    c.lineCap = 'round'; c.lineJoin = 'round'; c.lineWidth = width; c.strokeStyle = color;
    c.beginPath(); tracePath(c, upto); c.stroke(); c.restore();
  }

  // ember streaks: short lines that leave the tip while a stroke is drawn
  var NS = 120, sx = new Float32Array(NS), sy = new Float32Array(NS), svx = new Float32Array(NS), svy = new Float32Array(NS), sl = new Float32Array(NS), sm = new Float32Array(NS), sw = new Float32Array(NS), sh = 0;
  function streak(x, y, dx, dy){
    var i = sh; sh = (sh+1)%NS;
    var a = Math.atan2(dy, dx) + Math.PI + (Math.random()-0.5)*1.4, sp = 90 + Math.random()*220;
    sx[i] = x; sy[i] = y; svx[i] = Math.cos(a)*sp; svy[i] = Math.sin(a)*sp - 30; sm[i] = 0.22 + Math.random()*0.3; sl[i] = sm[i]; sw[i] = 0.8 + Math.random()*0.8;
  }

  // the same two glow strokes as the filter path, drawn off canvas so only their blurred shadow lands, then added on top
  function softGlow(blur, alpha, ox, oy, scale, tiltX, skew, tiltY, upto, wBase, glowA){
    var off = softC.width + 400;
    sctx.setTransform(1, 0, 0, 1, 0, 0); sctx.globalCompositeOperation = 'source-over'; sctx.clearRect(0, 0, softC.width, softC.height);
    sctx.globalCompositeOperation = 'lighter'; sctx.shadowBlur = blur*2; sctx.shadowOffsetX = off; sctx.shadowOffsetY = 0;
    sctx.lineCap = 'round'; sctx.lineJoin = 'round'; sctx.strokeStyle = '#000';
    [[3.0, '223,142,99', 0.5], [1.3, '239,163,124', 0.55]].forEach(function(g){
      sctx.setTransform(1, 0, 0, 1, -off, 0); sctx.translate(ox, oy); sctx.transform(tiltX, skew*0.3, skew, tiltY, 0, 0); sctx.scale(scale, scale);
      sctx.shadowColor = 'rgba(' + g[1] + ',' + clamp(g[2]*glowA).toFixed(3) + ')';
      sctx.lineWidth = wBase*g[0]; sctx.beginPath(); tracePath(sctx, upto); sctx.stroke();
    });
    ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.globalAlpha = alpha; ctx.drawImage(softC, 0, 0, softC.width, softC.height, 0, 0, W, H); ctx.restore();
  }

  var cx = 0, cy = 0, S = 1, narrow = false;
  function layout(){
    // laid out as a plain section (heroFlow), the canvas covers the hero text only, not the statement under it
    var inner = pin.querySelector('.hero-inner');
    canvas.style.height = heroFlow && inner ? inner.offsetHeight + 'px' : '';
    W = pin.clientWidth; H = heroFlow && inner ? inner.offsetHeight : pin.clientHeight;
    canvas.width = Math.round(W*dpr); canvas.height = Math.round(H*dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    glowC.width = Math.max(1, Math.round(W*GQ)); glowC.height = Math.max(1, Math.round(H*GQ)); gctx.setTransform(GQ, 0, 0, GQ, 0, 0);
    blurC.width = glowC.width; blurC.height = glowC.height;
    softC.width = Math.max(1, Math.round(W)); softC.height = Math.max(1, Math.round(H));
    narrow = W < 900;
    S = narrow ? Math.min(W*0.62, H*0.30)/110 : Math.min(H*0.62, W*0.30)/110;
    cx = narrow ? W*0.5 : W*0.72; cy = narrow ? H*0.71 : H*0.52;
    if (narrow){
      // on a phone the rune sits under the text block, never on it: measured from where the buttons end
      var cta = pin.querySelector('.hero-inner .cta'), pr = pin.getBoundingClientRect();
      var ib = cta ? cta.getBoundingClientRect().bottom - pr.top : H*0.55;
      if (heroFlow){
        // sized by the screen, not the section, and set in the room the section keeps for it under the buttons
        S = Math.min(W*0.62, window.innerHeight*0.30)/110; S = Math.min(S, Math.max(0.6, (H - 48 - ib)/110)); cy = ib + 24 + 55*S;
      } else {
        S = Math.min(S, Math.max(0.6, (H - 48 - ib)/110));
        cy = Math.max(H*0.71, ib + 24 + 55*S);
      }
    } else if (heroFlow){
      S = Math.min(window.innerHeight*0.62, W*0.30)/110;
    }
  }
  window.addEventListener('resize', layout); layout();
  window.addEventListener('heroflow', function(){ layout(); schedule(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ layout(); schedule(); });

  // where the rune lands: the mark inside the header lockup, in canvas coordinates
  function landing(){
    if (!lockup) return {ox: 40, oy: 40, S: 0.36};
    var r = lockup.getBoundingClientRect(), c = canvas.getBoundingClientRect();
    var St = r.height/143.17;
    return {ox: r.left - c.left + 30*St, oy: r.top - c.top + (10.4 + 49)*St, S: St};
  }

  var t0 = performance.now(), last = t0, mouse = {x:0, y:0}, target = {x:0, y:0}, arrived = false;
  function setArrived(v){ if (v === arrived) return; arrived = v; root.classList.toggle('mark-arrived', v); root.classList.toggle('mark-pending', !v); }
  root.classList.add('mark-pending');
  if (reduce) setArrived(true);

  // frames run only while the hero is on screen and the rune is alive; the clock pauses in between
  var running = false, pausedAt = 0;
  function schedule(){ if (running) return; running = true; if (pausedAt){ t0 += performance.now() - pausedAt; pausedAt = 0; } last = performance.now(); requestAnimationFrame(frame); }
  function landed(sp){ return heroFlow ? canvas.getBoundingClientRect().top + cy + 55*S < (siteHeader ? siteHeader.clientHeight : 72) : sp >= (narrow ? 0.11 : 0.29); }
  function onScroll(){ if (!reduce){ var pp = heroProgress(); setArrived(landed(pp)); root.classList.toggle('over-hero', pp < 0.3); } schedule(); }
  window.addEventListener('scroll', onScroll, {passive: true}); window.addEventListener('resize', schedule); document.addEventListener('visibilitychange', schedule);
  function frame(now){
    running = false;
    var dt = Math.min(0.05, (now - last)/1000); last = now;
    // in flow the canvas covers only the hero text, and the statement below it keeps the taller pin on screen: test the canvas itself.
    // The header arrival keeps following the scroll through onScroll while the frames are paused
    var pr = (heroFlow ? canvas : pin).getBoundingClientRect();
    if (pr.bottom <= 0 || pr.top >= window.innerHeight || document.hidden){ pausedAt = now; return; }
    // sp drives the text fade and the header; p drives the flight, and is held at 0 under reduced motion
    var t = reduce ? 30 : (now - t0)/1000, sp = heroProgress(), p = reduce || heroFlow ? 0 : sp;
    root.classList.toggle('over-hero', sp < 0.3);
    swapText(sp);
    mouse.x += (target.x - mouse.x)*0.05; mouse.y += (target.y - mouse.y)*0.05;
    var pg = progress(t), upto = pg.upto;
    // ignition: one pulse along the strokes, then a calm light
    var ig = t > T_IGNITE ? clamp((t - T_IGNITE)/IGNITE_D) : 0;
    var lit = t > T_IGNITE ? clamp((t - T_IGNITE - 0.25)/0.9) : 0;
    var flare = t > T_IGNITE ? Math.exp(-(t - T_IGNITE)*2.2) : 0;
    // the forge at rest: after the ignition the light settles over 1.6 s to a resting copper and the breathing stops
    var rest = t > T_IGNITE ? clamp((t - T_IGNITE - 1.3)/1.6) : 0;
    var glow = lit*(1 - 0.88*rest);
    var breathe = 1 + 0.05*Math.sin(t*1.2)*(1 - rest) - 0.05*(1 - rest);
    // flight: on a desktop the rune rises at the right while it shrinks, glides left in the band under the header, above both text
    // blocks, and settles into the header mark. On a phone the text fills the width and any way up crosses it, so the rune shrinks and
    // fades where it stands and the header mark lights in its place
    var fl = narrow ? 0 : clamp((p - 0.04)/0.22), land = landing(), fade = narrow ? easeIO(clamp((p - 0.075)/0.035)) : 0;
    var up = easeIO(clamp(fl/0.5)), across = easeIO(clamp((fl - 0.5)/0.35)), settle = easeIO(clamp((fl - 0.85)/0.15));
    var band = (siteHeader ? siteHeader.getBoundingClientRect().bottom - canvas.getBoundingClientRect().top : 72) + 16 + 55*land.S;
    var vanish = narrow ? fade : clamp((p - 0.27)/0.03);
    var alive = 1 - vanish;
    var scale = narrow ? S*(1 - 0.6*fade) : S*(1 - up) + land.S*up;
    var ox = cx*(1 - across) + land.ox*across;
    var oy = (cy + Math.sin(t*0.9)*3*lit*(1 - rest)*(1 - up))*(1 - up) + (band*(1 - settle) + land.oy*settle)*up;
    fl = up;
    var wBase = 6.5*(1 - fl) + 24*fl;
    var tiltX = 1 - Math.abs(mouse.x)*0.06*(1 - fl), skew = -mouse.x*0.05*(1 - fl), tiltY = 1 - Math.abs(mouse.y)*0.04*(1 - fl);
    if (!reduce) setArrived(landed(sp));

    ctx.clearRect(0, 0, W, H);
    if (alive <= 0) return; // the rune has landed in the header; scrolling back up schedules the next frame
    // halo behind the lit rune
    if (lit > 0 || ig > 0){
      var hr = 320*Math.min(S, 3.2)*(1 - fl*0.85);
      var halo = ctx.createRadialGradient(ox, oy, 6, ox, oy, hr);
      halo.addColorStop(0, 'rgba(223,142,99,' + ((0.16*glow*breathe + 0.32*flare)*alive).toFixed(3) + ')');
      halo.addColorStop(0.45, 'rgba(223,142,99,' + (0.05*glow*alive).toFixed(3) + ')');
      halo.addColorStop(1, 'rgba(223,142,99,0)');
      ctx.fillStyle = halo; ctx.fillRect(0, 0, W, H);
    }
    // bloom: the rune drawn wide on a separate canvas, blurred twice
    var k = scale/S;
    var glowA = ((0.35 + 0.65*lit)*(1 - 0.78*rest)*breathe + flare*0.8)*alive*(1 - fl*0.6);
    if (hasFilter){
      gctx.clearRect(0, 0, W, H);
      gctx.save(); gctx.translate(ox, oy); gctx.transform(tiltX, skew*0.3, skew, tiltY, 0, 0); gctx.scale(scale, scale);
      drawRune(gctx, upto, wBase*3.0, '#DF8E63', 0.5*glowA, 'lighter');
      drawRune(gctx, upto, wBase*1.3, '#EFA37C', 0.55*glowA, 'lighter');
      gctx.restore();
      // the radii are device pixels at full resolution, as before; GQ/dpr turns them into pixels of the half-size canvas
      bctx.setTransform(1, 0, 0, 1, 0, 0); bctx.globalCompositeOperation = 'source-over'; bctx.clearRect(0, 0, blurC.width, blurC.height);
      bctx.globalCompositeOperation = 'lighter';
      bctx.filter = 'blur(' + (Math.max(2, Math.round(22*Math.min(1.2, k)))*GQ/dpr).toFixed(2) + 'px)'; bctx.globalAlpha = 0.9; bctx.drawImage(glowC, 0, 0);
      bctx.filter = 'blur(' + (Math.max(1, Math.round(7*Math.min(1.2, k)))*GQ/dpr).toFixed(2) + 'px)'; bctx.globalAlpha = 0.7; bctx.drawImage(glowC, 0, 0);
      bctx.filter = 'none';
      ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.drawImage(blurC, 0, 0, blurC.width, blurC.height, 0, 0, W, H); ctx.restore();
    } else {
      softGlow(Math.max(2, 22*Math.min(1.2, k))/dpr, 0.9, ox, oy, scale, tiltX, skew, tiltY, upto, wBase, glowA);
      softGlow(Math.max(1, 7*Math.min(1.2, k))/dpr, 0.7, ox, oy, scale, tiltX, skew, tiltY, upto, wBase, glowA);
    }
    // the rune itself: a deep copper underlay, the copper stroke, a warm inner light while it is hot.
    // At rest the inner line has faded out and the underlay has thinned, so the rune reads as cooled metal, not a lit tube.
    ctx.save(); ctx.translate(ox, oy); ctx.transform(tiltX, skew*0.3, skew, tiltY, 0, 0); ctx.scale(scale, scale);
    drawRune(ctx, upto, wBase*1.3, '#8C4E2C', (0.95 - 0.35*rest)*alive*(1 - fl*0.8));
    drawRune(ctx, upto, wBase, rest >= 1 ? '#DF8E63' : (lit > 0 ? '#E8996D' : '#DF8E63'), (0.9 + 0.1*lit)*alive);
    drawRune(ctx, upto, wBase*0.45, '#FFD9B4', (0.12*(1 - rest) + 0.2*glow*breathe + flare*0.6)*alive, 'lighter');
    // the ignition pulse: one bright segment runs the length of the rune
    if (ig > 0 && ig < 1){
      var seg = total*0.16, head = ig*(total + seg);
      ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.lineCap = 'round'; ctx.lineWidth = wBase*0.7; ctx.strokeStyle = '#FFF1E0'; ctx.globalAlpha = 0.85*Math.sin(ig*Math.PI)*alive;
      ctx.setLineDash([seg, total*4]); ctx.lineDashOffset = -(head - seg); ctx.beginPath(); tracePath(ctx, total); ctx.stroke();
      ctx.restore();
    }
    ctx.restore();
    // the hot tip while a line is being drawn, and the streaks that leave it
    if (pg.active >= 0){
      var tp = runePoint(upto), tx = ox + (tp.x*tiltX + tp.y*skew)*scale, ty = oy + (tp.x*skew*0.3 + tp.y*tiltY)*scale;
      var g = ctx.createRadialGradient(tx, ty, 0, tx, ty, 26); g.addColorStop(0, 'rgba(255,241,224,0.95)'); g.addColorStop(0.3, 'rgba(239,163,124,0.5)'); g.addColorStop(1, 'rgba(239,163,124,0)');
      ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.fillStyle = g; ctx.beginPath(); ctx.arc(tx, ty, 26, 0, 6.283); ctx.fill(); ctx.restore();
      if (Math.random() < 0.7) streak(tx, ty, tp.dx, tp.dy);
    }
    ctx.save(); ctx.globalCompositeOperation = 'lighter'; ctx.lineCap = 'round';
    for (var i = 0; i < NS; i++){
      if (sl[i] <= 0) continue;
      sl[i] -= dt; svy[i] += 140*dt; svx[i] *= 0.97;
      var x0 = sx[i], y0 = sy[i]; sx[i] += svx[i]*dt; sy[i] += svy[i]*dt;
      var a = Math.max(0, sl[i]/sm[i]);
      ctx.globalAlpha = 0.9*a*alive; ctx.lineWidth = sw[i]*(0.4 + a); ctx.strokeStyle = a > 0.5 ? '#FFE1C2' : '#EFA37C';
      ctx.beginPath(); ctx.moveTo(x0 - svx[i]*dt*2.2, y0 - svy[i]*dt*2.2); ctx.lineTo(sx[i], sy[i]); ctx.stroke();
    }
    ctx.restore();
    // a rune at rest is still: once the light has settled, no more frames until the scroll asks
    var settling = Math.abs(target.x - mouse.x) + Math.abs(target.y - mouse.y) > 0.002;
    var atRest = reduce || (rest >= 1 && pg.active < 0 && fl === 0);
    if (!atRest || settling){ running = true; requestAnimationFrame(frame); }
  }
  schedule();
})();

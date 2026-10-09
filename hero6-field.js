// Hero F, highest quality: the field and the cut. Textured ears with awns, a dusk sky with a sun, bloom and light shafts through the grain, filmic grading.
(function(){
  if (!window.THREE) return;
  var canvas = document.getElementById('scene');
  var pin = canvas.parentElement;
  var renderer = new THREE.WebGLRenderer({canvas: canvas, antialias: false, alpha: false, powerPreference: 'high-performance'});
  var CFG = window.FIELD_CFG || {};
  var PR = CFG.lite ? 1 : Math.min(window.devicePixelRatio || 1, 1.5);
  renderer.setPixelRatio(PR);
  renderer.outputEncoding = THREE.LinearEncoding;
  renderer.setClearColor(0x0e1114, 1);
  var isGL2 = renderer.capabilities.isWebGL2;
  var scene = new THREE.Scene();
  var FOG = 0x8a5a38;
  scene.fog = new THREE.Fog(FOG, 140, 420);
  var camera = new THREE.PerspectiveCamera(36, 1, 1, 3000);

  // light: a low sun behind the field, warm sky, cool fill from the front
  scene.add(new THREE.HemisphereLight(0xb07a55, 0x1a120c, 0.65));
  var SUN = new THREE.Vector3(150, 26, -690);
  var sun = new THREE.DirectionalLight(0xffc79a, 1.25); sun.position.copy(SUN); scene.add(sun);
  var fill = new THREE.DirectionalLight(0x7c93a6, 0.35); fill.position.set(140, 120, 180); scene.add(fill);
  var warm = new THREE.DirectionalLight(0xdf8e63, 0.25); warm.position.set(-160, 60, 120); scene.add(warm);

  // sky backdrop and sun
  (function(){
    var sc = document.createElement('canvas'); sc.width = 1024; sc.height = 512; var g = sc.getContext('2d');
    var gr = g.createLinearGradient(0, 0, 0, 512);
    gr.addColorStop(0, '#0e1114'); gr.addColorStop(0.42, '#1a120e'); gr.addColorStop(0.58, '#4a2a17'); gr.addColorStop(0.655, '#c98a55'); gr.addColorStop(0.69, '#8a5a38'); gr.addColorStop(0.8, '#3a2416'); gr.addColorStop(1, '#1a120e');
    g.fillStyle = gr; g.fillRect(0, 0, 1024, 512);
    // cloud streaks: dark bands high up, sunlit edges near the horizon
    for (var cl = 0; cl < 34; cl++){
      var cy0 = 200 + Math.pow(Math.random(), 0.7)*130, cxx = Math.random()*1024, cw = 120 + Math.random()*320, chh = 4 + Math.random()*11;
      var near = (cy0 - 200)/130;
      var lit = 'rgba(255,' + Math.round(170 + near*40) + ',' + Math.round(110 + near*30) + ',' + (0.05 + near*0.16).toFixed(3) + ')';
      var dark = 'rgba(20,14,12,' + (0.12 - near*0.06).toFixed(3) + ')';
      g.save(); g.translate(cxx, cy0); g.scale(1, 1);
      var cg = g.createRadialGradient(0, 0, 0, 0, 0, cw); cg.addColorStop(0, near > 0.45 ? lit : dark); cg.addColorStop(1, 'rgba(0,0,0,0)');
      g.fillStyle = cg; g.beginPath(); g.ellipse(0, 0, cw, chh, 0, 0, 6.283); g.fill();
      if (near > 0.45){ var eg = g.createRadialGradient(0, -chh*0.6, 0, 0, -chh*0.6, cw*0.9); eg.addColorStop(0, 'rgba(255,225,190,' + (near*0.18).toFixed(3) + ')'); eg.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = eg; g.beginPath(); g.ellipse(0, -chh*0.6, cw*0.9, chh*0.5, 0, 0, 6.283); g.fill(); }
      g.restore();
    }
    var skyT = new THREE.CanvasTexture(sc); skyT.encoding = THREE.sRGBEncoding;
    var sky = new THREE.Mesh(new THREE.PlaneGeometry(3400, 1200), new THREE.MeshBasicMaterial({map: skyT, fog: false, depthWrite: false}));
    sky.position.set(0, 250, -720); scene.add(sky);
    function disc(stops){ var c = document.createElement('canvas'); c.width = c.height = 256; var x = c.getContext('2d'); var r = x.createRadialGradient(128,128,0,128,128,128); stops.forEach(function(s){ r.addColorStop(s[0], s[1]); }); x.fillStyle = r; x.fillRect(0,0,256,256); var t = new THREE.CanvasTexture(c); t.encoding = THREE.sRGBEncoding; return t; }
    var sunT = disc([[0,'rgba(255,244,226,1)'],[0.18,'rgba(255,232,200,1)'],[0.24,'rgba(255,200,150,0.55)'],[0.5,'rgba(239,163,124,0.12)'],[1,'rgba(223,142,99,0)']]);
    var sunS = new THREE.Sprite(new THREE.SpriteMaterial({map: sunT, fog: false, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending}));
    sunS.position.copy(SUN); sunS.scale.set(150, 150, 1); scene.add(sunS);
    var hazeT = disc([[0,'rgba(255,190,140,0.55)'],[0.4,'rgba(223,142,99,0.16)'],[1,'rgba(223,142,99,0)']]);
    var haze = new THREE.Sprite(new THREE.SpriteMaterial({map: hazeT, fog: false, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending}));
    haze.position.set(SUN.x, SUN.y + 20, SUN.z + 4); haze.scale.set(720, 520, 1); scene.add(haze);
  })();

  // soil
  var soilC = document.createElement('canvas'); soilC.width = soilC.height = 256; var sctx = soilC.getContext('2d'), sim = sctx.createImageData(256, 256);
  for (var si = 0; si < 256*256; si++){ var sg = 34 + Math.random()*26; sim.data[si*4] = sg + 14; sim.data[si*4+1] = sg + 6; sim.data[si*4+2] = sg; sim.data[si*4+3] = 255; }
  sctx.putImageData(sim, 0, 0);
  var soilT = new THREE.CanvasTexture(soilC); soilT.wrapS = soilT.wrapT = THREE.RepeatWrapping; soilT.repeat.set(70, 70); soilT.encoding = THREE.sRGBEncoding;
  var ground = new THREE.Mesh(new THREE.PlaneGeometry(1800, 1800), new THREE.MeshStandardMaterial({map: soilT, color: 0xa88868, roughness: 1}));
  ground.rotation.x = -Math.PI/2; ground.position.z = -300; scene.add(ground);

  // rune patch on the ground; the top of the rune is the far edge
  var S = 104, CX = 28, CZ = -14;
  var channels = [
    {a: [38, 0], b: [38, 104], w: 12, t0: 1.6, dur: 2.5},
    {a: [44, 30], b: [80, -4], w: 11.3, t0: 4.3, dur: 1.0},
    {a: [44, 68], b: [108, 2], w: 11.3, t0: 5.4, dur: 1.3}
  ];
  function channelOf(u, v){
    for (var i = 0; i < channels.length; i++){
      var c = channels[i], ax = c.a[0], ay = c.a[1], bx = c.b[0], by = c.b[1];
      var dx = bx-ax, dy = by-ay, l2 = dx*dx+dy*dy, tt = ((u-ax)*dx + (v-ay)*dy)/l2;
      if (tt < -0.02 || tt > 1.02) continue;
      var px = ax + dx*tt, py = ay + dy*tt, dist = Math.hypot(u-px, v-py);
      if (dist < c.w/2) return {i: i, t: tt};
    }
    return null;
  }

  // the stubble: pale cut straw on the soil along the harvest path, revealed channel by channel so the rune reads from above
  var STUB_EXT = 120, STUB_OFF = 8;
  var stubC = document.createElement('canvas'); stubC.width = stubC.height = 1024; var stx = stubC.getContext('2d');
  (function(){
    function cu(v){ return (v + STUB_OFF)/STUB_EXT*1024; }
    stx.lineCap = 'round';
    if ('filter' in stx) stx.filter = 'blur(2px)';
    channels.forEach(function(c){ stx.strokeStyle = 'rgba(138,104,66,0.78)'; stx.lineWidth = c.w/STUB_EXT*1024; stx.beginPath(); stx.moveTo(cu(c.a[0]), cu(c.a[1])); stx.lineTo(cu(c.b[0]), cu(c.b[1])); stx.stroke(); });
    if ('filter' in stx) stx.filter = 'none';
    stx.globalCompositeOperation = 'source-atop';
    for (var f = 0; f < 14000; f++){
      var fx = Math.random()*1024, fy = Math.random()*1024, dk = Math.random() < 0.45;
      stx.fillStyle = dk ? 'rgba(74,46,26,' + (0.3 + Math.random()*0.45).toFixed(2) + ')' : 'rgba(228,192,132,' + (0.25 + Math.random()*0.5).toFixed(2) + ')';
      stx.beginPath(); stx.ellipse(fx, fy, 2 + Math.random()*5, 0.7 + Math.random()*1.4, Math.random()*3.1416, 0, 6.283); stx.fill();
    }
    stx.globalCompositeOperation = 'source-over';
  })();
  var stubT = new THREE.CanvasTexture(stubC); stubT.encoding = THREE.sRGBEncoding; stubT.anisotropy = Math.min(4, renderer.capabilities.getMaxAnisotropy());
  var uProg = {value: new THREE.Vector3(0, 0, 0)};
  var stubMat = new THREE.MeshStandardMaterial({map: stubT, transparent: true, depthWrite: false, roughness: 1, polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -2});
  stubMat.onBeforeCompile = function(shader){
    shader.uniforms.uProg = uProg;
    shader.vertexShader = 'varying vec2 vPatch;\n' + shader.vertexShader.replace('#include <begin_vertex>', '#include <begin_vertex>\nvPatch = vec2(position.x + 52.0, 52.0 - position.y);');
    var chan = channels.map(function(c, i){ return 'chan(vec2(' + c.a[0].toFixed(1) + ', ' + c.a[1].toFixed(1) + '), vec2(' + c.b[0].toFixed(1) + ', ' + c.b[1].toFixed(1) + '), ' + c.w.toFixed(1) + ', uProg' + ['.x', '.y', '.z'][i] + ', vPatch)'; });
    shader.fragmentShader = ['uniform vec3 uProg; varying vec2 vPatch;',
      'float chan(vec2 a, vec2 b, float w, float prog, vec2 p){ vec2 d = b - a; float tt = dot(p - a, d)/dot(d, d); vec2 q = a + d*tt; float dist = length(p - q); float inside = step(dist, w*0.5 + 2.0) * step(-0.03, tt) * step(tt, 1.03); return inside * (1.0 - smoothstep(prog - 0.06, prog + 0.02, tt)); }',
      shader.fragmentShader.replace('#include <map_fragment>', '#include <map_fragment>\ndiffuseColor.a *= max(max(' + chan[0] + ', ' + chan[1] + '), ' + chan[2] + ');')].join('\n');
  };
  var stubble = new THREE.Mesh(new THREE.PlaneGeometry(STUB_EXT, STUB_EXT), stubMat);
  stubble.rotation.x = -Math.PI/2; stubble.position.set(CX, 0.06, CZ); stubble.renderOrder = 1; scene.add(stubble);

  // the stalk texture: a blade strip on the left, a wheat ear with awns on the right
  var earC = document.createElement('canvas'); earC.width = 512; earC.height = 1024; var ec = earC.getContext('2d'); ec.scale(2, 2);
  (function(){
    var bg = ec.createLinearGradient(0, 512, 0, 0); bg.addColorStop(0, '#a8643a'); bg.addColorStop(0.6, '#d68d5f'); bg.addColorStop(1, '#e8a774');
    ec.fillStyle = bg; ec.fillRect(0, 0, 30, 512);
    ec.fillStyle = 'rgba(255,225,190,0.35)'; ec.fillRect(13, 0, 3, 512);
    ec.strokeStyle = '#b8703f'; ec.lineWidth = 5; ec.lineCap = 'round'; ec.beginPath(); ec.moveTo(150, 500); ec.lineTo(150, 70); ec.stroke();
    var n = 13;
    for (var k = 0; k < n; k++){
      var y = 470 - k*30, side = k % 2 ? 1 : -1;
      ec.strokeStyle = 'rgba(238,190,140,0.95)'; ec.lineWidth = 1.2; ec.beginPath(); ec.moveTo(150 + side*10, y - 6); ec.quadraticCurveTo(150 + side*34, y - 60, 150 + side*46, y - 150); ec.stroke();
      ec.save(); ec.translate(150 + side*11, y); ec.rotate(side*0.5);
      var kg = ec.createRadialGradient(-3, -5, 1, 0, 0, 17); kg.addColorStop(0, '#fbe0bc'); kg.addColorStop(0.35, '#eab080'); kg.addColorStop(0.75, '#c8804c'); kg.addColorStop(1, '#8e5230');
      ec.fillStyle = kg; ec.strokeStyle = '#6a3a1e'; ec.lineWidth = 0.9; ec.beginPath(); ec.ellipse(0, 0, 11, 17, 0, 0, 6.283); ec.fill(); ec.stroke();
      ec.strokeStyle = 'rgba(110,60,30,0.7)'; ec.lineWidth = 0.8; ec.beginPath(); ec.moveTo(0, -14); ec.quadraticCurveTo(1.5, 0, 0, 14); ec.stroke();
      ec.restore();
    }
    ec.save(); ec.translate(150, 62); var tg = ec.createRadialGradient(-3,-4,1,0,0,16); tg.addColorStop(0,'#f6cfa4'); tg.addColorStop(1,'#b06a3d'); ec.fillStyle = tg; ec.strokeStyle = '#7a4526'; ec.lineWidth = 1.2; ec.beginPath(); ec.ellipse(0, 0, 10, 16, 0, 0, 6.283); ec.fill(); ec.stroke(); ec.restore();
  })();
  var earT = new THREE.CanvasTexture(earC); earT.encoding = THREE.sRGBEncoding; earT.anisotropy = Math.min(4, renderer.capabilities.getMaxAnisotropy());

  var H = 7.5, EAR_H = 6.2, EAR_W = 3.6;
  function mergeGeos(list){
    var pos = [], nor = [], uv = [];
    list.forEach(function(g){ var n = g.toNonIndexed(); pos.push(n.attributes.position.array); nor.push(n.attributes.normal.array); uv.push(n.attributes.uv.array); });
    function cat(arrs){ var len = arrs.reduce(function(a, b){ return a + b.length; }, 0), out = new Float32Array(len), o = 0; arrs.forEach(function(a){ out.set(a, o); o += a.length; }); return out; }
    var g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.BufferAttribute(cat(pos), 3)); g.setAttribute('normal', new THREE.BufferAttribute(cat(nor), 3)); g.setAttribute('uv', new THREE.BufferAttribute(cat(uv), 2));
    return g;
  }
  var blade = new THREE.PlaneGeometry(0.8, H, 1, 5); blade.translate(0, H/2, 0);
  (function(){ var a = blade.attributes.position, u = blade.attributes.uv; for (var i = 0; i < a.count; i++){ var y = a.getY(i), h = y/H; a.setX(i, a.getX(i)*(1 - 0.4*h)); u.setXY(i, 0.02 + u.getX(i)*0.08, u.getY(i)); } })();
  var headA = new THREE.PlaneGeometry(EAR_W, EAR_H, 1, 3); headA.translate(0, H - 0.6 + EAR_H/2, 0);
  (function(){ var u = headA.attributes.uv; for (var i = 0; i < u.count; i++){ u.setXY(i, 0.13 + u.getX(i)*0.87, u.getY(i)); } })();
  var headB = headA.clone(); headB.rotateY(Math.PI/2);
  var stalkGeo = mergeGeos([blade, headA, headB]);
  var TOP = H - 0.6 + EAR_H;

  var narrow0 = pin.clientWidth < 900;
  var N = CFG.n || (CFG.lite ? 5000 : (narrow0 ? 9000 : 34000));
  var aPhase = new Float32Array(N), aCut = new Float32Array(N), aBoost = new Float32Array(N), aShade = new Float32Array(N), aFdir = new Float32Array(N);
  var cutT = new Float32Array(N), cutI = new Int8Array(N), sx = new Float32Array(N), sz = new Float32Array(N);
  var M = new THREE.Matrix4(), P = new THREE.Vector3(), Q = new THREE.Quaternion(), SV = new THREE.Vector3(), E = new THREE.Euler();
  var uTime = {value: 0}, uWind = {value: new THREE.Vector2(0.12, 0.0)}, uGust = {value: 0.16};
  var stalkMat = new THREE.MeshStandardMaterial({map: earT, alphaTest: 0.45, color: 0xffffff, roughness: 0.68, metalness: 0.05, side: THREE.DoubleSide});
  stalkMat.onBeforeCompile = function(shader){
    shader.uniforms.uTime = uTime; shader.uniforms.uWind = uWind; shader.uniforms.uGust = uGust;
    shader.vertexShader = 'attribute float aPhase; attribute float aCut; attribute float aBoost; attribute float aShade; attribute float aFdir; uniform float uTime; uniform vec2 uWind; uniform float uGust; varying float vCut; varying float vH; varying float vShade; varying float vBoost;\n' + shader.vertexShader;
    shader.vertexShader = shader.vertexShader.replace('#include <begin_vertex>', [
      'vec3 transformed = vec3(position);',
      'vec4 ip = instanceMatrix * vec4(0.0, 0.0, 0.0, 1.0);',
      'float h = clamp(position.y / ' + TOP.toFixed(2) + ', 0.0, 1.0);',
      'float g1 = sin(uTime*1.25 + ip.x*0.055 + ip.z*0.04 + aPhase*0.4);',
      'float g2 = sin(uTime*2.0 - ip.x*0.1 + ip.z*0.075 + aPhase);',
      'float g3 = sin(uTime*0.6 + ip.x*0.02 - ip.z*0.03);',
      'float gust = g1*uGust + g2*0.05 + g3*0.06;',
      'float bend = h*h;',
      'float e = 1.0 - pow(1.0 - aCut, 3.0);',
      'float lean = (2.3 + aFdir) * e;',
      'float wx = (uWind.x + gust + aBoost*1.1) * bend * 4.2;',
      'float wz = (uWind.y + gust*0.35 + aBoost*0.3) * bend * 4.2;',
      'transformed.y *= (1.0 - 0.72*e);',
      'transformed.x += wx*(1.0 - e) + lean*h*' + (TOP*0.42).toFixed(2) + ';',
      'transformed.z += wz*(1.0 - e) + (0.35*aFdir)*h*' + (TOP*0.42).toFixed(2) + '*e;',
      'vCut = e; vH = h; vShade = aShade; vBoost = aBoost;'
    ].join('\n'));
    shader.fragmentShader = 'varying float vCut; varying float vH; varying float vShade; varying float vBoost;\n' + shader.fragmentShader;
    shader.fragmentShader = shader.fragmentShader.replace('#include <color_fragment>', [
      '#include <color_fragment>',
      'diffuseColor.rgb *= vShade * mix(0.35, 1.0, vH) * (1.0 - 0.72*vCut);'
    ].join('\n'));
    shader.fragmentShader = shader.fragmentShader.replace('#include <emissivemap_fragment>', [
      '#include <emissivemap_fragment>',
      'totalEmissiveRadiance += vec3(0.95, 0.5, 0.2) * pow(vH, 3.0) * (0.22 + 0.6*vBoost) * (1.0 - vCut) * vShade;'
    ].join('\n'));
  };
  var stalks = new THREE.InstancedMesh(stalkGeo, stalkMat, N); stalks.frustumCulled = false; scene.add(stalks);
  for (var i = 0; i < N; i++){
    var x = (Math.random()-0.5)*420, z = -470 + Math.random()*590;
    var r = Math.random();
    if (r < 0.44){ x = CX + (Math.random()-0.5)*150; z = CZ + (Math.random()-0.5)*150; }
    else if (r < 0.66){ x = (Math.random()-0.5)*300; z = 20 + Math.random()*100; }
    sx[i] = x; sz[i] = z; aPhase[i] = Math.random()*6.283; aShade[i] = 0.62 + Math.random()*0.48; aFdir[i] = (Math.random()-0.5)*0.9; cutI[i] = -1;
    var u = (x - (CX - S/2))/S*104, v = (z - (CZ - S/2))/S*104;
    if (u >= -2 && u <= 108 && v >= -2 && v <= 106){ var ch = channelOf(u, v); if (ch){ cutI[i] = ch.i; cutT[i] = ch.t; } }
    E.set(0, Math.random()*6.283, 0); Q.setFromEuler(E); P.set(x, 0, z); SV.set(1, 0.72 + Math.random()*0.5, 1);
    M.compose(P, Q, SV); stalks.setMatrixAt(i, M);
  }
  stalkGeo.setAttribute('aPhase', new THREE.InstancedBufferAttribute(aPhase, 1));
  stalkGeo.setAttribute('aCut', new THREE.InstancedBufferAttribute(aCut, 1));
  stalkGeo.setAttribute('aBoost', new THREE.InstancedBufferAttribute(aBoost, 1));
  stalkGeo.setAttribute('aShade', new THREE.InstancedBufferAttribute(aShade, 1));
  stalkGeo.setAttribute('aFdir', new THREE.InstancedBufferAttribute(aFdir, 1));
  var cutIdx = []; for (var c0 = 0; c0 < N; c0++) if (cutI[c0] >= 0) cutIdx.push(c0);

  // chaff and dust
  function softDot(){ var c = document.createElement('canvas'); c.width = c.height = 32; var g = c.getContext('2d'); var rr = g.createRadialGradient(16,16,0,16,16,16); rr.addColorStop(0,'rgba(255,255,255,1)'); rr.addColorStop(1,'rgba(255,255,255,0)'); g.fillStyle = rr; g.fillRect(0,0,32,32); return new THREE.CanvasTexture(c); }
  var NP = 900, pPos = new Float32Array(NP*3), pVel = new Float32Array(NP*3), pLife = new Float32Array(NP), pHead = 0;
  for (var q = 0; q < NP; q++) pPos[q*3+1] = -9999;
  var pGeo = new THREE.BufferGeometry(); pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  var chaff = new THREE.Points(pGeo, new THREE.PointsMaterial({color: 0xe08a58, size: 2.2, map: softDot(), transparent: true, opacity: 0.45, depthWrite: false, blending: THREE.AdditiveBlending, sizeAttenuation: true}));
  scene.add(chaff);
  function spawnChaff(x, z, ambient){ var k = pHead; pHead = (pHead+1)%NP; pPos[k*3] = x; pPos[k*3+1] = ambient ? 3 + Math.random()*18 : 4 + Math.random()*6; pPos[k*3+2] = z; pVel[k*3] = ambient ? 1 + Math.random()*3 : 6 + Math.random()*10; pVel[k*3+1] = ambient ? (Math.random()-0.5)*1.5 : 4 + Math.random()*6; pVel[k*3+2] = (Math.random()-0.5)*(ambient ? 2 : 6); pLife[k] = ambient ? 6 + Math.random()*8 : 1.5 + Math.random()*2; }
  for (var a0 = 0; a0 < 320; a0++) spawnChaff((Math.random()-0.5)*300, -280 + Math.random()*380, true);

  // post-processing: bright pass, blur, light shafts, composite with filmic grading
  var VS = 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }';
  var quadScene = new THREE.Scene(), quadCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  var quad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), null); quad.frustumCulled = false; quadScene.add(quad);
  function rt(w, h, msaa){
    var opts = {minFilter: THREE.LinearFilter, magFilter: THREE.LinearFilter, format: THREE.RGBAFormat, depthBuffer: !!msaa, stencilBuffer: false};
    var t = (msaa && isGL2 && THREE.WebGLMultisampleRenderTarget) ? new THREE.WebGLMultisampleRenderTarget(w, h, opts) : new THREE.WebGLRenderTarget(w, h, opts);
    t.texture.encoding = THREE.sRGBEncoding; return t;
  }
  var rtScene, rtBright, rtBlurA, rtBlurB, rtRays, rtSoftA, rtSoftB;
  var brightMat = new THREE.ShaderMaterial({uniforms: {tex: {value: null}, threshold: {value: 0.62}}, vertexShader: VS, fragmentShader: 'uniform sampler2D tex; uniform float threshold; varying vec2 vUv; void main(){ vec3 c = texture2D(tex, vUv).rgb; float l = dot(c, vec3(0.299,0.587,0.114)); float m = smoothstep(threshold, threshold + 0.3, l); gl_FragColor = vec4(c*m, 1.0); }', depthTest: false, depthWrite: false});
  var blurMat = new THREE.ShaderMaterial({uniforms: {tex: {value: null}, dir: {value: new THREE.Vector2(1, 0)}, texel: {value: new THREE.Vector2(1/512, 1/512)}}, vertexShader: VS, fragmentShader: 'uniform sampler2D tex; uniform vec2 dir; uniform vec2 texel; varying vec2 vUv; void main(){ float w0 = 0.227, w1 = 0.194, w2 = 0.121, w3 = 0.054, w4 = 0.016; vec3 s = texture2D(tex, vUv).rgb*w0; vec2 o1 = dir*texel*1.5, o2 = dir*texel*3.0, o3 = dir*texel*4.5, o4 = dir*texel*6.0; s += (texture2D(tex, vUv+o1).rgb + texture2D(tex, vUv-o1).rgb)*w1; s += (texture2D(tex, vUv+o2).rgb + texture2D(tex, vUv-o2).rgb)*w2; s += (texture2D(tex, vUv+o3).rgb + texture2D(tex, vUv-o3).rgb)*w3; s += (texture2D(tex, vUv+o4).rgb + texture2D(tex, vUv-o4).rgb)*w4; gl_FragColor = vec4(s, 1.0); }', depthTest: false, depthWrite: false});
  var raysMat = new THREE.ShaderMaterial({uniforms: {tex: {value: null}, sunPos: {value: new THREE.Vector2(0.5, 0.7)}, density: {value: 0.9}, decay: {value: 0.965}, weight: {value: 0.06}}, vertexShader: VS, fragmentShader: 'uniform sampler2D tex; uniform vec2 sunPos; uniform float density; uniform float decay; uniform float weight; varying vec2 vUv; void main(){ vec2 uv = vUv; vec2 delta = (uv - sunPos) * (1.0/44.0) * density; float illum = 1.0; vec3 col = vec3(0.0); for (int i = 0; i < 44; i++){ uv -= delta; col += texture2D(tex, uv).rgb * illum * weight; illum *= decay; } gl_FragColor = vec4(col, 1.0); }', depthTest: false, depthWrite: false});
  var compMat = new THREE.ShaderMaterial({uniforms: {scene: {value: null}, soft: {value: null}, bloom: {value: null}, rays: {value: null}, focus: {value: new THREE.Vector2(0.38, 0.14)}, bloomStr: {value: 0.9}, raysStr: {value: 0.85}, time: {value: 0}, grainAmt: {value: 0.022}, res: {value: new THREE.Vector2(1, 1)}, exposure: {value: 1.12}}, vertexShader: VS, fragmentShader: [
    'uniform sampler2D scene; uniform sampler2D soft; uniform sampler2D bloom; uniform sampler2D rays; uniform vec2 focus; uniform float bloomStr; uniform float raysStr; uniform float time; uniform float grainAmt; uniform vec2 res; uniform float exposure; varying vec2 vUv;',
    'vec3 aces(vec3 x){ return clamp((x*(2.51*x + 0.03))/(x*(2.43*x + 0.59) + 0.14), 0.0, 1.0); }',
    'float hash(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233)))*43758.5453); }',
    'void main(){',
    '  vec2 off = (vUv - 0.5) * 0.0035;',
    '  float coc = clamp(smoothstep(0.22, 0.0, vUv.y)*0.6 + smoothstep(0.68, 0.94, vUv.y)*0.45, 0.0, 1.0);',
    '  coc *= (1.0 - focus.y);',
    '  vec3 sharp = vec3(texture2D(scene, vUv + off).r, texture2D(scene, vUv).g, texture2D(scene, vUv - off).b);',
    '  vec3 blur = texture2D(soft, vUv).rgb;',
    '  vec3 c = pow(mix(sharp, blur, coc), vec3(2.2));',
    '  vec3 b = pow(texture2D(bloom, vUv).rgb, vec3(2.2));',
    '  vec3 r = pow(texture2D(rays, vUv).rgb, vec3(2.2));',
    '  vec3 hdr = (c + b*bloomStr + r*raysStr) * exposure;',
    '  vec3 m = aces(hdr);',
    '  m = mix(m, m*vec3(1.05, 0.97, 0.9), 0.45);',
    '  vec2 q = vUv - 0.5; float vig = 1.0 - dot(q, q)*0.85; m *= clamp(vig, 0.0, 1.0);',
    '  m += vec3(0.0035, 0.0045, 0.007) * (1.0 - m);',
    '  float g = hash(vUv*res + vec2(fract(time*7.0), fract(time*3.0))*137.0) - 0.5; m += g*grainAmt;',
    '  gl_FragColor = vec4(pow(max(m, 0.0), vec3(1.0/2.2)), 1.0);',
    '}'].join('\n'), depthTest: false, depthWrite: false});
  function pass(mat, target){ quad.material = mat; renderer.setRenderTarget(target); renderer.render(quadScene, quadCam); }
  var camLow, camHigh, lookLow, lookHigh;
  function layout(){
    var w = pin.clientWidth, h = pin.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w/h; camera.updateProjectionMatrix();
    var pw = Math.round(w*PR), ph = Math.round(h*PR);
    if (rtScene){ rtScene.dispose(); rtBright.dispose(); rtBlurA.dispose(); rtBlurB.dispose(); rtRays.dispose(); rtSoftA.dispose(); rtSoftB.dispose(); }
    rtScene = rt(pw, ph, true); rtBright = rt(pw >> 1, ph >> 1); rtBlurA = rt(pw >> 2, ph >> 2); rtBlurB = rt(pw >> 2, ph >> 2); rtRays = rt(pw >> 1, ph >> 1); rtSoftA = rt(pw >> 1, ph >> 1); rtSoftB = rt(pw >> 1, ph >> 1);
    compMat.uniforms.res.value.set(pw, ph);
    var narrow = w < 900;
    camLow = narrow ? {x: 0, y: 40, z: 150} : {x: -26, y: 30, z: 128};
    camHigh = narrow ? {x: 0, y: 70, z: 130} : {x: -20, y: 60, z: 112};
    lookLow = narrow ? {x: 0, y: 8, z: -70} : {x: 20, y: 8, z: -60};
    lookHigh = narrow ? {x: 0, y: 4, z: -80} : {x: 22, y: 4, z: -70};
  }
  var t0 = performance.now(), last = t0, mouse = {x:0, y:0}, target = {x:0, y:0};
  window.addEventListener('pointermove', function(e){ var r = pin.getBoundingClientRect(); target.x = (e.clientX - r.left)/r.width*2 - 1; target.y = (e.clientY - r.top)/r.height*2 - 1; }, {passive: true});
  window.addEventListener('resize', layout); layout();
  var look = new THREE.Vector3(), sunProj = new THREE.Vector3();
  function frame(now){
    var dt = Math.min(0.05, (now - last)/1000); last = now;
    var pr = pin.getBoundingClientRect();
    if (pr.bottom <= 0 || pr.top >= window.innerHeight || document.hidden){ t0 += dt*1000; requestAnimationFrame(frame); return; }
    var t = reduce ? 40 : (now - t0)/1000, p = reduce ? 0 : heroProgress();
    fadeText(p);
    mouse.x += (target.x - mouse.x)*0.035; mouse.y += (target.y - mouse.y)*0.035;
    uTime.value = t;
    uWind.value.set(0.14 + mouse.x*0.3, mouse.y*0.18);
    uGust.value = 0.13 + 0.07*Math.sin(t*0.45) + 0.05*Math.sin(t*0.13);
    var changed = false;
    uProg.value.set(Math.max(0, Math.min(1.15, (t - channels[0].t0)/channels[0].dur)), Math.max(0, Math.min(1.15, (t - channels[1].t0)/channels[1].dur)), Math.max(0, Math.min(1.15, (t - channels[2].t0)/channels[2].dur)));
    for (var k = 0; k < cutIdx.length; k++){
      var i = cutIdx[k], c = channels[cutI[i]];
      var prog = Math.max(0, Math.min(1.15, (t - c.t0)/c.dur));
      var ahead = cutT[i] - prog;
      var boost = ahead > 0 && ahead < 0.16 ? (1 - ahead/0.16) : 0;
      if (aBoost[i] !== boost){ aBoost[i] = boost; changed = true; }
      if (prog >= cutT[i] && aCut[i] < 1){ aCut[i] = Math.min(1, aCut[i] + dt*2.4); changed = true; if (Math.random() < 0.1) spawnChaff(sx[i], sz[i], false); }
    }
    if (changed){ stalkGeo.attributes.aCut.needsUpdate = true; stalkGeo.attributes.aBoost.needsUpdate = true; }
    for (var q2 = 0; q2 < NP; q2++){
      if (pLife[q2] <= 0) continue; pLife[q2] -= dt;
      pPos[q2*3] += (pVel[q2*3] + uWind.value.x*8)*dt; pPos[q2*3+1] += pVel[q2*3+1]*dt; pPos[q2*3+2] += (pVel[q2*3+2] + uWind.value.y*6)*dt;
      if (pLife[q2] <= 0){ if (Math.random() < 0.5){ pLife[q2] = 6 + Math.random()*8; pPos[q2*3] = (Math.random()-0.5)*300; pPos[q2*3+1] = 3 + Math.random()*18; pPos[q2*3+2] = -280 + Math.random()*380; pVel[q2*3] = 1 + Math.random()*3; pVel[q2*3+1] = (Math.random()-0.5)*1.5; pVel[q2*3+2] = (Math.random()-0.5)*2; } else pPos[q2*3+1] = -9999; }
    }
    pGeo.attributes.position.needsUpdate = true;
    // camera: opens low in the grain, rises as the rune is cut, and higher still on scroll
    var up = Math.max(0, Math.min(1, (t - 2.2)/6.0)); var eu = up*up*(3-2*up);
    var rise = Math.max(0, Math.min(1, (p - 0.08)/0.6)); var er = rise*rise*(3-2*rise);
    var drift = Math.sin(t*0.15)*4;
    var cxp = camLow.x + (camHigh.x - camLow.x)*eu, cyp = camLow.y + (camHigh.y - camLow.y)*eu, czp = camLow.z + (camHigh.z - camLow.z)*eu;
    var lx = lookLow.x + (lookHigh.x - lookLow.x)*eu, ly = lookLow.y + (lookHigh.y - lookLow.y)*eu, lz = lookLow.z + (lookHigh.z - lookLow.z)*eu;
    camera.position.set(cxp + drift + (CX - cxp - drift)*er + mouse.x*3, cyp + (178 - cyp)*er + mouse.y*2, czp + (CZ + 34 - czp)*er);
    look.set(lx + (CX - lx)*er, ly*(1-er), lz + (CZ - lz)*er);
    camera.lookAt(look);
    // render the scene, then the passes
    renderer.setRenderTarget(rtScene); renderer.render(scene, camera);
    brightMat.uniforms.tex.value = rtScene.texture; pass(brightMat, rtBright);
    sunProj.copy(SUN).project(camera);
    var behind = sunProj.z > 1 || sunProj.z < -1;
    raysMat.uniforms.sunPos.value.set(Math.max(-0.3, Math.min(1.3, sunProj.x*0.5 + 0.5)), Math.max(-0.3, Math.min(1.3, sunProj.y*0.5 + 0.5)));
    raysMat.uniforms.tex.value = rtBright.texture; pass(raysMat, rtRays);
    blurMat.uniforms.texel.value.set(1/rtBlurA.width, 1/rtBlurA.height);
    blurMat.uniforms.tex.value = rtBright.texture; blurMat.uniforms.dir.value.set(1, 0); pass(blurMat, rtBlurA);
    blurMat.uniforms.tex.value = rtBlurA.texture; blurMat.uniforms.dir.value.set(0, 1); pass(blurMat, rtBlurB);
    blurMat.uniforms.tex.value = rtBlurB.texture; blurMat.uniforms.dir.value.set(1, 0); pass(blurMat, rtBlurA);
    blurMat.uniforms.tex.value = rtBlurA.texture; blurMat.uniforms.dir.value.set(0, 1); pass(blurMat, rtBlurB);
    blurMat.uniforms.texel.value.set(1/rtSoftA.width, 1/rtSoftA.height);
    blurMat.uniforms.tex.value = rtScene.texture; blurMat.uniforms.dir.value.set(1, 0); pass(blurMat, rtSoftA);
    blurMat.uniforms.tex.value = rtSoftA.texture; blurMat.uniforms.dir.value.set(0, 1); pass(blurMat, rtSoftB);
    compMat.uniforms.focus.value.set(0.38, er);
    compMat.uniforms.scene.value = rtScene.texture; compMat.uniforms.soft.value = rtSoftB.texture; compMat.uniforms.bloom.value = rtBlurB.texture; compMat.uniforms.rays.value = rtRays.texture;
    compMat.uniforms.raysStr.value = behind ? 0 : 0.85*(1 - er*0.7); compMat.uniforms.time.value = t;
    pass(compMat, null);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();

/* TechnoForesight core runtime.
   Shared by every module: library loader, file helpers, the workbench panel and the module registry.
   Modules add themselves with TF.register({ handlerName: function (rootEl, config) {...} }). */
(function () {
  'use strict';

  var LIBS = {
    pdflib: 'https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js',
    pdfjs: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js',
    pdfjsWorker: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js',
    jszip: 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js',
    heic2any: 'https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js'
  };
  var loading = {};
  function loadLib(key) {
    if (!loading[key]) {
      loading[key] = new Promise(function (resolve, reject) {
        var s = document.createElement('script');
        s.src = LIBS[key];
        s.async = true;
        s.onload = function () { resolve(); };
        s.onerror = function () {
          delete loading[key];
          reject(new Error('A required component did not load. Check your internet connection and try again.'));
        };
        document.head.appendChild(s);
      });
    }
    return loading[key];
  }
  async function pdfjs() {
    await loadLib('pdfjs');
    window.pdfjsLib.GlobalWorkerOptions.workerSrc = LIBS.pdfjsWorker;
    return window.pdfjsLib;
  }
  async function pdflib() { await loadLib('pdflib'); return window.PDFLib; }

  /* ---------- helpers ---------- */
  function fmt(bytes) {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(bytes < 10240 ? 1 : 0) + ' KB';
    return (bytes / 1048576).toFixed(2) + ' MB';
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function baseName(name) { return name.replace(/\.[^.]+$/, '') || 'file'; }
  function rename(name, ext) { return baseName(name) + '.' + ext; }
  function isHeic(f) { return /\.(heic|heif)$/i.test(f.name || '') || /heic|heif/i.test(f.type || ''); }
  function isPdf(f) { return /\.pdf$/i.test(f.name || '') || f.type === 'application/pdf'; }
  function isImage(f) { return isHeic(f) || /^image\//.test(f.type || '') || /\.(jpe?g|png|webp|avif|gif|bmp)$/i.test(f.name || ''); }
  function tick() { return new Promise(function (r) { setTimeout(r, 0); }); }

  async function decodeImage(file) {
    var blob = file;
    if (isHeic(file)) {
      await loadLib('heic2any');
      try {
        var out = await window.heic2any({ blob: file, toType: 'image/png' });
        blob = Array.isArray(out) ? out[0] : out;
      } catch (e) {
        throw new Error(file.name + ' could not be read as a HEIC photo.');
      }
    }
    try {
      return await createImageBitmap(blob, { imageOrientation: 'from-image' });
    } catch (e) {
      return await new Promise(function (resolve, reject) {
        var url = URL.createObjectURL(blob);
        var img = new Image();
        img.onload = function () { resolve(img); };
        img.onerror = function () {
          URL.revokeObjectURL(url);
          reject(new Error(file.name + ' could not be opened. This browser may not support this image type.'));
        };
        img.src = url;
      });
    }
  }
  function dims(src) { return { w: src.naturalWidth || src.width, h: src.naturalHeight || src.height }; }
  function canvasOf(w, h, bg) {
    var c = document.createElement('canvas');
    c.width = Math.max(1, Math.round(w));
    c.height = Math.max(1, Math.round(h));
    var ctx = c.getContext('2d');
    if (bg) { ctx.fillStyle = bg; ctx.fillRect(0, 0, c.width, c.height); }
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = 'high';
    return c;
  }
  function drawScaled(src, w, h, bg) {
    var c = canvasOf(w, h, bg);
    c.getContext('2d').drawImage(src, 0, 0, c.width, c.height);
    return c;
  }
  function toBlob(c, mime, q) {
    return new Promise(function (resolve, reject) {
      c.toBlob(function (b) {
        if (!b) reject(new Error('This browser could not create the output file. The image may be too large.'));
        else resolve(b);
      }, mime, q);
    });
  }
  function extFor(mime) { return mime === 'image/jpeg' ? 'jpg' : mime.split('/')[1]; }
  function coverRect(sw, sh, tw, th, focus) {
    var ta = tw / th, sa = sw / sh, cw, ch, cx, cy;
    if (sa > ta) { ch = sh; cw = sh * ta; cx = (sw - cw) / 2; cy = 0; }
    else { cw = sw; ch = sw / ta; cx = 0; cy = focus === 'top' ? (sh - ch) * 0.18 : (sh - ch) / 2; }
    return [cx, cy, cw, ch];
  }
  function parseRanges(text, max) {
    var out = [];
    String(text || '').split(',').forEach(function (part) {
      part = part.trim();
      if (!part) return;
      var m = part.match(/^(\d+)?\s*-\s*(\d+)?$/);
      var a, b;
      if (m) { a = m[1] ? +m[1] : 1; b = m[2] ? +m[2] : max; }
      else if (/^\d+$/.test(part)) { a = b = +part; }
      else throw new Error('“' + part + '” is not a page number or range. Use a format like 1-3, 5, 8-10.');
      if (a < 1 || b > max || a > b) throw new Error('Pages must be between 1 and ' + max + '. Check “' + part + '”.');
      out.push([a, b]);
    });
    if (!out.length) throw new Error('Enter the pages you want, for example 1-3, 5.');
    return out;
  }
  function download(blob, name) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
  }

  // Encode a canvas as small as possible under maxBytes by searching JPEG/WebP quality.
  async function encodeUnder(canvas, mime, maxBytes, qMin) {
    var hi = await toBlob(canvas, mime, 0.92);
    if (hi.size <= maxBytes) return { blob: hi, q: 0.92 };
    var lo = qMin || 0.05, top = 0.92, best = null, bestQ = 0;
    for (var i = 0; i < 9; i++) {
      var q = (lo + top) / 2;
      var b = await toBlob(canvas, mime, q);
      if (b.size <= maxBytes) { best = b; bestQ = q; lo = q; } else { top = q; }
    }
    if (!best) {
      var floor = await toBlob(canvas, mime, qMin || 0.05);
      if (floor.size <= maxBytes) return { blob: floor, q: qMin || 0.05 };
      return null;
    }
    return { blob: best, q: bestQ };
  }

  /* ---------- shared panel ---------- */
  function shell(root, o) {
    root.innerHTML =
      '<div class="tool-panel">' +
      '<label class="drop"><input type="file" class="sr-only"' + (o.multiple ? ' multiple' : '') + ' accept="' + esc(o.accept) + '">' +
      '<span class="drop-title">' + esc(o.pick || (o.multiple ? 'Choose files' : 'Choose a file')) + '</span>' +
      '<span class="drop-sub">or drop ' + (o.multiple ? 'them' : 'it') + ' here</span>' +
      '<span class="drop-note">' + esc(o.note || 'Files are processed on your device and never uploaded.') + '</span></label>' +
      '<ul class="filelist" aria-label="Selected files"></ul>' +
      '<div class="options">' + (o.options || '') + '</div>' +
      '<div class="actions"><button type="button" class="btn primary run" disabled>' + esc(o.action) + '</button>' +
      '<button type="button" class="btn ghost reset" hidden>Start over</button></div>' +
      '<p class="status" role="status" aria-live="polite"></p>' +
      '<div class="results"></div></div>';
    var $ = function (s) { return root.querySelector(s); };
    var input = $('input[type=file]'), drop = $('.drop'), list = $('.filelist'), run = $('.run'),
        reset = $('.reset'), status = $('.status'), results = $('.results');
    var files = [], urls = [], busy = false, handler = null, onFiles = null;

    function setStatus(msg, kind) { status.textContent = msg || ''; status.className = 'status' + (kind ? ' ' + kind : ''); }
    function render() {
      list.innerHTML = files.map(function (f, i) {
        var ctl = '';
        if (o.reorder && files.length > 1) {
          ctl = '<button type="button" class="iconbtn" data-up="' + i + '" aria-label="Move ' + esc(f.name) + ' up"' + (i === 0 ? ' disabled' : '') + '>↑</button>' +
                '<button type="button" class="iconbtn" data-down="' + i + '" aria-label="Move ' + esc(f.name) + ' down"' + (i === files.length - 1 ? ' disabled' : '') + '>↓</button>';
        }
        return '<li><span class="fname">' + esc(f.name) + '</span><span class="fsize">' + fmt(f.size) + '</span>' + ctl +
          '<button type="button" class="iconbtn" data-rm="' + i + '" aria-label="Remove ' + esc(f.name) + '">✕</button></li>';
      }).join('');
      run.disabled = busy || files.length < (o.min || 1);
      if (files.length && files.length < (o.min || 1)) setStatus('Add at least ' + o.min + ' files.');
    }
    function add(fileList) {
      var picked = Array.prototype.slice.call(fileList || []);
      var ok = picked.filter(o.filter), bad = picked.length - ok.length;
      files = o.multiple ? files.concat(ok) : ok.slice(0, 1);
      clearResults();
      setStatus(bad ? bad + (bad === 1 ? ' file was' : ' files were') + ' skipped because ' + (bad === 1 ? 'it is' : 'they are') + ' not ' + o.kind + '.' : '', bad ? 'err' : '');
      render();
      if (onFiles) onFiles(files);
    }
    function clearResults() {
      urls.forEach(function (u) { URL.revokeObjectURL(u); });
      urls = []; results.innerHTML = ''; reset.hidden = true;
    }
    input.addEventListener('change', function () { add(input.files); input.value = ''; });
    ['dragenter', 'dragover'].forEach(function (ev) {
      drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); });
    });
    ['dragleave', 'drop'].forEach(function (ev) {
      drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); });
    });
    drop.addEventListener('drop', function (e) { add(e.dataTransfer.files); });
    list.addEventListener('click', function (e) {
      var t = e.target.closest('button'); if (!t || busy) return;
      if (t.dataset.rm != null) files.splice(+t.dataset.rm, 1);
      if (t.dataset.up != null) { var i = +t.dataset.up; files.splice(i - 1, 0, files.splice(i, 1)[0]); }
      if (t.dataset.down != null) { var j = +t.dataset.down; files.splice(j + 1, 0, files.splice(j, 1)[0]); }
      clearResults(); render(); if (onFiles) onFiles(files);
    });
    reset.addEventListener('click', function () { files = []; clearResults(); setStatus(''); render(); if (onFiles) onFiles(files); });
    run.addEventListener('click', async function () {
      if (!handler || busy) return;
      busy = true; run.disabled = true; clearResults(); setStatus('Working…');
      try {
        var out = await handler(files.slice(), function (m) { setStatus(m); });
        show(out);
        var fails = out.filter(function (r) { return r.error; }).length;
        if (fails === out.length) setStatus('Nothing was converted. See the details below.', 'err');
        else setStatus(fails ? 'Done, with ' + fails + ' problem' + (fails > 1 ? 's' : '') + ' listed below.' : 'Done. Your files are ready.', fails ? 'err' : 'ok');
      } catch (e) {
        console.error(e);
        setStatus(e && e.message ? e.message : 'Something went wrong. Try again with a different file.', 'err');
      }
      busy = false; render(); reset.hidden = false;
    });
    function show(out) {
      var html = out.map(function (r, i) {
        if (r.error) return '<div class="result"><span class="rname">' + esc(r.name) + '</span><span class="rerr">' + esc(r.error) + '</span></div>';
        var u = URL.createObjectURL(r.blob); urls.push(u);
        var meter = '';
        if (r.target) {
          var scale = Math.max(r.before || 0, r.blob.size, r.target) || 1;
          meter = '<div class="meter" aria-hidden="true"><span class="fill" style="width:' + (r.blob.size / scale * 100).toFixed(1) + '%"></span>' +
                  '<span class="target" style="left:' + (r.target / scale * 100).toFixed(1) + '%"></span></div>';
        }
        var note = (r.before ? fmt(r.before) + ' → ' : '') + fmt(r.blob.size) + (r.note ? '. ' + r.note : '');
        return '<div class="result"><span class="rname">' + esc(r.name) + '</span>' +
          '<a class="dl" href="' + u + '" download="' + esc(r.name) + '">Download</a>' +
          '<span class="rnote">' + esc(note) + '</span>' + meter + '</div>';
      }).join('');
      var good = out.filter(function (r) { return !r.error; });
      if (good.length > 1) html += '<div class="zipbar"><button type="button" class="btn ghost zip">Download all as ZIP</button></div>';
      results.innerHTML = html;
      var zb = results.querySelector('.zip');
      if (zb) zb.addEventListener('click', async function () {
        zb.disabled = true; zb.textContent = 'Preparing ZIP…';
        try {
          await loadLib('jszip');
          var z = new window.JSZip(), used = {};
          good.forEach(function (r) {
            var n = r.name, k = 1;
            while (used[n]) n = baseName(r.name) + ' (' + (k++) + ')' + r.name.slice(baseName(r.name).length);
            used[n] = 1; z.file(n, r.blob);
          });
          download(await z.generateAsync({ type: 'blob' }), o.zipName || 'technoforesight-files.zip');
          zb.textContent = 'Download all as ZIP';
        } catch (e) { zb.textContent = 'ZIP failed. Download files one by one.'; }
        zb.disabled = false;
      });
    }
    render();
    return {
      root: root,
      opt: function (s) { return root.querySelector('.options ' + s); },
      onRun: function (fn) { handler = fn; },
      onFiles: function (fn) { onFiles = fn; },
      status: setStatus
    };
  }

  function chipsHTML(name, values, current, unit) {
    return '<div class="chips" data-chips="' + name + '">' + values.map(function (v) {
      return '<button type="button" class="chip" data-v="' + v + '" aria-pressed="' + (v == current) + '">' + v + ' ' + unit + '</button>';
    }).join('') + '</div>';
  }
  function wireChips(sh, name, input) {
    var box = sh.opt('[data-chips="' + name + '"]'); if (!box) return;
    function sync() { box.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', String(c.dataset.v == input.value)); }); }
    box.addEventListener('click', function (e) { var c = e.target.closest('.chip'); if (!c) return; input.value = c.dataset.v; sync(); });
    input.addEventListener('input', sync);
  }
  var IMG_ACCEPT = 'image/*,.heic,.heif,.avif,.webp';
  function qualityHTML(v) {
    return '<label class="field">Quality <small><output>' + v + '</output>%</small><input type="range" min="40" max="100" value="' + v + '" data-q></label>';
  }
  function wireQuality(sh) {
    var r = sh.opt('[data-q]'); if (!r) return function () { return 0.9; };
    r.addEventListener('input', function () { r.parentNode.querySelector('output').textContent = r.value; });
    return function () { return Math.min(1, +r.value / 100); };
  }

  /* ---------- registry and boot ---------- */
  var handlers = {};
  function register(map) { Object.keys(map).forEach(function (k) { handlers[k] = map[k]; }); }
  function addLib(key, url) { LIBS[key] = url; }
  function boot() {
    document.querySelectorAll('[data-tool]').forEach(function (el) {
      var cfg = {};
      try { cfg = JSON.parse(el.getAttribute('data-config') || '{}'); } catch (e) {}
      var name = el.getAttribute('data-tool'), fn = handlers[name];
      if (fn) fn(el, cfg);
      else el.innerHTML = '<div class="tool-panel"><p class="status err">This tool did not load. Reload the page to try again.</p></div>';
    });
  }
  window.TF = {
    version: '2',
    register: register,
    addLib: addLib,
    fmt: fmt,
    esc: esc,
    baseName: baseName,
    rename: rename,
    isHeic: isHeic,
    isPdf: isPdf,
    isImage: isImage,
    tick: tick,
    decodeImage: decodeImage,
    dims: dims,
    canvasOf: canvasOf,
    drawScaled: drawScaled,
    toBlob: toBlob,
    extFor: extFor,
    coverRect: coverRect,
    parseRanges: parseRanges,
    download: download,
    encodeUnder: encodeUnder,
    shell: shell,
    chipsHTML: chipsHTML,
    wireChips: wireChips,
    qualityHTML: qualityHTML,
    wireQuality: wireQuality,
    IMG_ACCEPT: IMG_ACCEPT,
    loadLib: loadLib,
    pdfjs: pdfjs,
    pdflib: pdflib
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else setTimeout(boot, 0);
})();

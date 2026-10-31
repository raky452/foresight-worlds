/* TechnoForesight module: form uploads (photo and signature, passport sheet). Depends on core.js. */
(function (TF) {
  'use strict';
  var fmt = TF.fmt, esc = TF.esc, baseName = TF.baseName, rename = TF.rename, isHeic = TF.isHeic, isPdf = TF.isPdf, isImage = TF.isImage, tick = TF.tick, decodeImage = TF.decodeImage, dims = TF.dims, canvasOf = TF.canvasOf, drawScaled = TF.drawScaled, toBlob = TF.toBlob, extFor = TF.extFor, coverRect = TF.coverRect, parseRanges = TF.parseRanges, download = TF.download, encodeUnder = TF.encodeUnder, shell = TF.shell, chipsHTML = TF.chipsHTML, wireChips = TF.wireChips, qualityHTML = TF.qualityHTML, wireQuality = TF.wireQuality, IMG_ACCEPT = TF.IMG_ACCEPT, loadLib = TF.loadLib, pdfjs = TF.pdfjs, pdflib = TF.pdflib;
  var T = {};
// Generic size presets. Always confirm against the official notification for your exam.
  var FORM_PRESETS = [
    { id: 'photo-sm', label: 'Photo 200 × 230 px, 20–50 KB', w: 200, h: 230, min: 20, max: 50, fit: 'cover' },
    { id: 'photo-pp', label: 'Passport photo 3.5 × 4.5 cm (413 × 531 px), 20–100 KB', w: 413, h: 531, min: 20, max: 100, fit: 'cover' },
    { id: 'sign-sm', label: 'Signature 140 × 60 px, 10–20 KB', w: 140, h: 60, min: 10, max: 20, fit: 'contain' },
    { id: 'sign-lg', label: 'Signature 350 × 150 px, 10–40 KB', w: 350, h: 150, min: 10, max: 40, fit: 'contain' },
    { id: 'thumb', label: 'Thumb impression 240 × 240 px, 20–50 KB', w: 240, h: 240, min: 20, max: 50, fit: 'contain' },
    { id: 'custom', label: 'Custom size' }
  ];
  T.formphoto = function (root) {
    var opts = FORM_PRESETS.map(function (p) { return '<option value="' + p.id + '">' + p.label + '</option>'; }).join('');
    var sh = shell(root, { accept: IMG_ACCEPT, multiple: true, kind: 'images', filter: isImage, action: 'Prepare for upload', zipName: 'form-uploads.zip',
      options:
        '<label class="field wide">Size required by the form<select data-p>' + opts + '</select></label>' +
        '<label class="field">Width (px)<input type="number" min="20" value="200" data-w></label>' +
        '<label class="field">Height (px)<input type="number" min="20" value="230" data-h></label>' +
        '<label class="field">Minimum size (KB)<input type="number" min="0" value="20" data-min></label>' +
        '<label class="field">Maximum size (KB)<input type="number" min="3" value="50" data-max></label>' +
        '<label class="field">How to fit<select data-fit><option value="cover">Crop to fill (photos)</option><option value="contain">Fit inside with white border (signatures)</option></select></label>' +
        '<label class="field">Crop position<select data-focus><option value="top">Keep the face (upper part)</option><option value="center">Centre</option></select></label>' });
    var sel = sh.opt('[data-p]');
    function apply() {
      var p = FORM_PRESETS.filter(function (x) { return x.id === sel.value; })[0];
      if (!p || p.id === 'custom') return;
      sh.opt('[data-w]').value = p.w; sh.opt('[data-h]').value = p.h;
      sh.opt('[data-min]').value = p.min; sh.opt('[data-max]').value = p.max; sh.opt('[data-fit]').value = p.fit;
    }
    sel.addEventListener('change', apply);
    ['[data-w]', '[data-h]', '[data-min]', '[data-max]'].forEach(function (s) { sh.opt(s).addEventListener('input', function () { sel.value = 'custom'; }); });
    sh.onRun(async function (files, say) {
      var W = Math.round(+sh.opt('[data-w]').value), H = Math.round(+sh.opt('[data-h]').value);
      var minB = +sh.opt('[data-min]').value * 1024, maxB = +sh.opt('[data-max]').value * 1024;
      var fit = sh.opt('[data-fit]').value, focus = sh.opt('[data-focus]').value;
      if (!(W >= 20 && H >= 20)) throw new Error('Enter a width and height of at least 20 pixels.');
      if (!(maxB > 0) || minB > maxB) throw new Error('The maximum size must be larger than the minimum size.');
      var out = [];
      for (var i = 0; i < files.length; i++) {
        var f = files[i];
        say('Preparing ' + (i + 1) + ' of ' + files.length + '…'); await tick();
        try {
          var src = await decodeImage(f), d = dims(src), cv = canvasOf(W, H, '#ffffff'), ctx = cv.getContext('2d');
          if (fit === 'cover') {
            var r = coverRect(d.w, d.h, W, H, focus);
            ctx.drawImage(src, r[0], r[1], r[2], r[3], 0, 0, W, H);
          } else {
            var s = Math.min(W / d.w, H / d.h), dw = d.w * s, dh = d.h * s;
            ctx.drawImage(src, (W - dw) / 2, (H - dh) / 2, dw, dh);
          }
          var res = await encodeUnder(cv, 'image/jpeg', maxB, 0.05);
          if (!res) throw new Error('This image cannot fit under ' + fmt(maxB) + ' at ' + W + ' × ' + H + ' px. Check the size rules.');
          var note = W + ' × ' + H + ' px JPG';
          if (res.blob.size < minB) {
            var top = await toBlob(cv, 'image/jpeg', 1);
            if (top.size >= minB && top.size <= maxB) res = { blob: top };
            else note += '. Smaller than the ' + fmt(minB) + ' minimum: use a sharper, more detailed original or a larger size';
          }
          out.push({ name: baseName(f.name) + '-' + W + 'x' + H + '.jpg', blob: res.blob, before: f.size, target: maxB, note: note });
        } catch (e) { out.push({ name: f.name, error: e.message }); }
      }
      return out;
    });
  };

  T.passport = function (root) {
    var sh = shell(root, { accept: IMG_ACCEPT, multiple: false, kind: 'an image', filter: isImage, action: 'Make photo sheet',
      options:
        '<label class="field">Photo size<select data-size><option value="35x45">3.5 × 4.5 cm (India, UK, EU, many others)</option><option value="51x51">2 × 2 inch (USA)</option><option value="35x35">3.5 × 3.5 cm</option><option value="30x40">3 × 4 cm</option></select></label>' +
        '<label class="field">Paper<select data-paper><option value="a4">A4 (21 × 29.7 cm)</option><option value="4x6">4 × 6 inch photo paper</option><option value="letter">US Letter</option></select></label>' +
        '<label class="field">Copies <small>leave empty to fill the page</small><input type="number" min="1" data-n></label>' +
        '<label class="field">Crop position<select data-focus><option value="top">Keep the face (upper part)</option><option value="center">Centre</option></select></label>' +
        '<label class="check"><input type="checkbox" checked data-lines> Print cutting lines</label>' });
    sh.onRun(async function (files, say) {
      var f = files[0], DPI = 300, mm = function (v) { return Math.round(v / 25.4 * DPI); };
      var sz = sh.opt('[data-size]').value.split('x').map(Number);
      var paper = { a4: [210, 297], '4x6': [101.6, 152.4], letter: [215.9, 279.4] }[sh.opt('[data-paper]').value];
      var pw = mm(sz[0]), ph = mm(sz[1]), PW = mm(paper[0]), PH = mm(paper[1]), gap = mm(2.5), margin = mm(5);
      var cols = Math.floor((PW - 2 * margin + gap) / (pw + gap)), rows = Math.floor((PH - 2 * margin + gap) / (ph + gap));
      var max = cols * rows, n = Math.min(max, +sh.opt('[data-n]').value || max);
      if (max < 1) throw new Error('This photo size does not fit on the selected paper.');
      say('Laying out ' + n + ' photos…'); await tick();
      var src = await decodeImage(f), d = dims(src), r = coverRect(d.w, d.h, pw, ph, sh.opt('[data-focus]').value);
      var one = canvasOf(pw, ph, '#ffffff'); one.getContext('2d').drawImage(src, r[0], r[1], r[2], r[3], 0, 0, pw, ph);
      var sheet = canvasOf(PW, PH, '#ffffff'), ctx = sheet.getContext('2d');
      var gridW = cols * pw + (cols - 1) * gap, ox = Math.round((PW - gridW) / 2), oy = margin, lines = sh.opt('[data-lines]').checked;
      for (var i = 0; i < n; i++) {
        var x = ox + (i % cols) * (pw + gap), y = oy + Math.floor(i / cols) * (ph + gap);
        ctx.drawImage(one, x, y);
        if (lines) { ctx.strokeStyle = '#9aa3b2'; ctx.lineWidth = 2; ctx.strokeRect(x - 1, y - 1, pw + 2, ph + 2); }
      }
      var jpg = await toBlob(sheet, 'image/jpeg', 0.95);
      var L = await pdflib(), doc = await L.PDFDocument.create();
      var pg = doc.addPage([paper[0] / 25.4 * 72, paper[1] / 25.4 * 72]);
      var img = await doc.embedJpg(await jpg.arrayBuffer());
      pg.drawImage(img, { x: 0, y: 0, width: pg.getWidth(), height: pg.getHeight() });
      var pdf = new Blob([await doc.save()], { type: 'application/pdf' });
      var label = n + ' photos, ' + sz[0] / 10 + ' × ' + sz[1] / 10 + ' cm, print at 100% (no “fit to page”)';
      return [
        { name: baseName(f.name) + '-photo-sheet.pdf', blob: pdf, note: label },
        { name: baseName(f.name) + '-photo-sheet.jpg', blob: jpg, note: label }
      ];
    });
  };

  
  TF.register(T);
})(window.TF);

/* TechnoForesight module: image converters, compression, resizing. Depends on core.js. */
(function (TF) {
  'use strict';
  var fmt = TF.fmt, esc = TF.esc, baseName = TF.baseName, rename = TF.rename, isHeic = TF.isHeic, isPdf = TF.isPdf, isImage = TF.isImage, tick = TF.tick, decodeImage = TF.decodeImage, dims = TF.dims, canvasOf = TF.canvasOf, drawScaled = TF.drawScaled, toBlob = TF.toBlob, extFor = TF.extFor, coverRect = TF.coverRect, parseRanges = TF.parseRanges, download = TF.download, encodeUnder = TF.encodeUnder, shell = TF.shell, chipsHTML = TF.chipsHTML, wireChips = TF.wireChips, qualityHTML = TF.qualityHTML, wireQuality = TF.wireQuality, IMG_ACCEPT = TF.IMG_ACCEPT, loadLib = TF.loadLib, pdfjs = TF.pdfjs, pdflib = TF.pdflib;
/* ---------- image tools ---------- */
  var T = {};

  T.convert = function (root, c) {
    var mime = 'image/' + c.to, ext = extFor(mime), lossy = c.to !== 'png';
    var sh = shell(root, { accept: c.accept || IMG_ACCEPT, multiple: true, kind: 'images', filter: isImage,
      action: 'Convert to ' + ext.toUpperCase(), options: lossy ? qualityHTML(90) : '', zipName: 'converted-' + ext + '.zip' });
    var q = wireQuality(sh);
    sh.onRun(async function (files, say) {
      var out = [];
      for (var i = 0; i < files.length; i++) {
        var f = files[i];
        say('Converting ' + (i + 1) + ' of ' + files.length + '…'); await tick();
        try {
          var src = await decodeImage(f), d = dims(src);
          var cv = drawScaled(src, d.w, d.h, c.to === 'jpeg' ? '#ffffff' : null);
          var b = await toBlob(cv, mime, lossy ? q() : undefined);
          if (b.type !== mime) throw new Error('This browser cannot save ' + ext.toUpperCase() + ' files. Try Chrome, Edge or Firefox.');
          out.push({ name: rename(f.name, ext), blob: b, before: f.size, note: d.w + ' × ' + d.h + ' px' });
        } catch (e) { out.push({ name: f.name, error: e.message }); }
      }
      return out;
    });
  };

  T.compress = function (root, c) {
    var presets = c.presets || [20, 50, 100, 200, 500];
    var sh = shell(root, { accept: IMG_ACCEPT, multiple: true, kind: 'images', filter: isImage, action: 'Compress images', zipName: 'compressed-images.zip',
      options:
        '<div class="field wide">Target size <div class="inline"><input type="number" min="5" max="20000" step="1" value="' + (c.target || 100) + '" data-target aria-label="Target size in KB" style="width:110px"> <span>KB or less</span></div>' +
        chipsHTML('t', presets, c.target || 100, 'KB') + '</div>' +
        '<label class="field">Format<select data-fmt><option value="image/jpeg">JPG (works everywhere)</option><option value="image/webp">WebP (smaller, for websites)</option></select></label>' +
        '<label class="field">Maximum width <small>optional, in pixels</small><input type="number" min="50" step="1" placeholder="Keep original" data-maxw></label>' });
    var tIn = sh.opt('[data-target]'); wireChips(sh, 't', tIn);
    sh.onRun(async function (files, say) {
      var target = Math.round(+tIn.value * 1024);
      if (!(target >= 2048)) throw new Error('Enter a target of at least 2 KB.');
      var mime = sh.opt('[data-fmt]').value, maxw = +sh.opt('[data-maxw]').value || 0, out = [];
      for (var i = 0; i < files.length; i++) {
        var f = files[i];
        say('Compressing ' + (i + 1) + ' of ' + files.length + '…'); await tick();
        try {
          if (f.size <= target && /jpe?g/i.test(f.type) && !maxw && mime === 'image/jpeg') {
            out.push({ name: f.name, blob: f, before: f.size, target: target, note: 'Already under ' + fmt(target) + ', kept as is' });
            continue;
          }
          var src = await decodeImage(f), d = dims(src), scale = maxw && d.w > maxw ? maxw / d.w : 1, res = null, w, h;
          for (var k = 0; k < 14 && !res; k++) {
            w = Math.max(16, Math.round(d.w * scale)); h = Math.max(16, Math.round(d.h * scale));
            var cv = drawScaled(src, w, h, mime === 'image/jpeg' ? '#ffffff' : null);
            res = await encodeUnder(cv, mime, target, 0.3);
            if (!res) scale *= 0.82;
          }
          if (!res) throw new Error('Could not reach ' + fmt(target) + '. Try a larger target.');
          out.push({ name: rename(f.name, extFor(mime)), blob: res.blob, before: f.size, target: target,
            note: w + ' × ' + h + ' px, quality ' + Math.round(res.q * 100) + '%' });
        } catch (e) { out.push({ name: f.name, error: e.message }); }
      }
      return out;
    });
  };

  T.resize = function (root) {
    var sh = shell(root, { accept: IMG_ACCEPT, multiple: true, kind: 'images', filter: isImage, action: 'Resize images', zipName: 'resized-images.zip',
      options:
        '<label class="field">Width<input type="number" min="1" step="any" value="1200" data-w></label>' +
        '<label class="field">Height <small>leave empty to keep proportions</small><input type="number" min="1" step="any" data-h></label>' +
        '<label class="field">Unit<select data-unit><option value="px">Pixels</option><option value="cm">Centimetres</option><option value="mm">Millimetres</option><option value="in">Inches</option></select></label>' +
        '<label class="field">Print resolution<select data-dpi><option>300</option><option>200</option><option>150</option><option>96</option><option>72</option></select><small>DPI, used for cm, mm and inches</small></label>' +
        '<label class="field">Save as<select data-fmt><option value="same">Same as original</option><option value="image/jpeg">JPG</option><option value="image/png">PNG</option><option value="image/webp">WebP</option></select></label>' });
    sh.onRun(async function (files, say) {
      var unit = sh.opt('[data-unit]').value, dpi = +sh.opt('[data-dpi]').value;
      var toPx = function (v) { return unit === 'px' ? v : unit === 'in' ? v * dpi : unit === 'cm' ? v / 2.54 * dpi : v / 25.4 * dpi; };
      var W = +sh.opt('[data-w]').value, H = +sh.opt('[data-h]').value;
      if (!W && !H) throw new Error('Enter a width, a height, or both.');
      var fmtSel = sh.opt('[data-fmt]').value, out = [];
      for (var i = 0; i < files.length; i++) {
        var f = files[i];
        say('Resizing ' + (i + 1) + ' of ' + files.length + '…'); await tick();
        try {
          var src = await decodeImage(f), d = dims(src);
          var w = W ? toPx(W) : toPx(H) * d.w / d.h, h = H ? toPx(H) : toPx(W) * d.h / d.w;
          if (w > 12000 || h > 12000) throw new Error('That size is too large. Keep each side under 12,000 pixels.');
          var mime = fmtSel === 'same' ? (/png/.test(f.type) ? 'image/png' : /webp/.test(f.type) ? 'image/webp' : 'image/jpeg') : fmtSel;
          var cv = drawScaled(src, w, h, mime === 'image/jpeg' ? '#ffffff' : null);
          var b = await toBlob(cv, mime, 0.92);
          out.push({ name: baseName(f.name) + '-' + cv.width + 'x' + cv.height + '.' + extFor(b.type), blob: b, before: f.size, note: cv.width + ' × ' + cv.height + ' px' });
        } catch (e) { out.push({ name: f.name, error: e.message }); }
      }
      return out;
    });
  };

  
  TF.register(T);
})(window.TF);

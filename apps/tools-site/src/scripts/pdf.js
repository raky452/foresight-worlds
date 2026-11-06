/* TechnoForesight module: PDF tools. Depends on core.js. */
(function (TF) {
  'use strict';
  var fmt = TF.fmt, esc = TF.esc, baseName = TF.baseName, rename = TF.rename, isHeic = TF.isHeic, isPdf = TF.isPdf, isImage = TF.isImage, tick = TF.tick, decodeImage = TF.decodeImage, dims = TF.dims, canvasOf = TF.canvasOf, drawScaled = TF.drawScaled, toBlob = TF.toBlob, extFor = TF.extFor, coverRect = TF.coverRect, parseRanges = TF.parseRanges, download = TF.download, encodeUnder = TF.encodeUnder, shell = TF.shell, chipsHTML = TF.chipsHTML, wireChips = TF.wireChips, qualityHTML = TF.qualityHTML, wireQuality = TF.wireQuality, IMG_ACCEPT = TF.IMG_ACCEPT, loadLib = TF.loadLib, pdfjs = TF.pdfjs, pdflib = TF.pdflib;
  var T = {};
/* ---------- PDF tools ---------- */
  async function loadPdfLibDoc(L, f) {
    try { return await L.PDFDocument.load(await f.arrayBuffer()); }
    catch (e) {
      if (/encrypt/i.test(String(e && e.message))) throw new Error(f.name + ' is password-protected. Remove the password first, then try again.');
      throw new Error(f.name + ' could not be opened. It may be damaged or not a real PDF.');
    }
  }
  function pdfBlob(bytes) { return new Blob([bytes], { type: 'application/pdf' }); }

  T.merge = function (root) {
    var sh = shell(root, { accept: '.pdf,application/pdf', multiple: true, reorder: true, min: 2, kind: 'PDF files', filter: isPdf, action: 'Merge PDFs', pick: 'Choose PDF files' });
    sh.onRun(async function (files, say) {
      var L = await pdflib(), out = await L.PDFDocument.create(), total = 0;
      for (var i = 0; i < files.length; i++) {
        say('Adding ' + files[i].name + ' (' + (i + 1) + ' of ' + files.length + ')…'); await tick();
        var src = await loadPdfLibDoc(L, files[i]);
        var pages = await out.copyPages(src, src.getPageIndices());
        pages.forEach(function (p) { out.addPage(p); }); total += pages.length;
      }
      say('Saving…');
      var before = files.reduce(function (a, f) { return a + f.size; }, 0);
      return [{ name: 'merged.pdf', blob: pdfBlob(await out.save()), before: before, note: total + ' pages from ' + files.length + ' files' }];
    });
  };

  function pageCountHint(sh) {
    sh.onFiles(async function (files) {
      var info = sh.opt('[data-info]'); if (!info) return;
      info.textContent = '';
      if (!files[0]) return;
      try { var L = await pdflib(), d = await loadPdfLibDoc(L, files[0]); info.textContent = 'This PDF has ' + d.getPageCount() + ' pages.'; }
      catch (e) { info.textContent = e.message; }
    });
  }

  T.split = function (root) {
    var sh = shell(root, { accept: '.pdf,application/pdf', multiple: false, kind: 'a PDF file', filter: isPdf, action: 'Split PDF', pick: 'Choose a PDF file', zipName: 'split-pdf.zip',
      options:
        '<label class="field wide">What to do<select data-mode><option value="extract">Extract the pages I choose into one PDF</option><option value="ranges">Make one PDF for each range I type</option><option value="each">Save every page as its own PDF</option></select></label>' +
        '<label class="field wide">Pages <small data-info></small><input type="text" value="1-2" data-r placeholder="For example 1-3, 5, 8-10"></label>' });
    pageCountHint(sh);
    sh.onRun(async function (files, say) {
      var f = files[0], L = await pdflib(), src = await loadPdfLibDoc(L, f), n = src.getPageCount(), mode = sh.opt('[data-mode]').value, out = [];
      async function make(idx, name) {
        var d = await L.PDFDocument.create(), pages = await d.copyPages(src, idx);
        pages.forEach(function (p) { d.addPage(p); });
        out.push({ name: name, blob: pdfBlob(await d.save()), note: idx.length + (idx.length === 1 ? ' page' : ' pages') });
      }
      var b = baseName(f.name);
      if (mode === 'each') {
        for (var i = 0; i < n; i++) { say('Page ' + (i + 1) + ' of ' + n + '…'); await make([i], b + '-page-' + (i + 1) + '.pdf'); }
      } else {
        var rs = parseRanges(sh.opt('[data-r]').value, n);
        if (mode === 'extract') {
          var idx = [];
          rs.forEach(function (r) { for (var k = r[0]; k <= r[1]; k++) idx.push(k - 1); });
          await make(idx, b + '-extract.pdf');
        } else {
          for (var j = 0; j < rs.length; j++) {
            var ii = []; for (var k2 = rs[j][0]; k2 <= rs[j][1]; k2++) ii.push(k2 - 1);
            await make(ii, b + '-pages-' + rs[j][0] + (rs[j][1] !== rs[j][0] ? '-' + rs[j][1] : '') + '.pdf');
          }
        }
      }
      return out;
    });
  };

  T.rotate = function (root) {
    var sh = shell(root, { accept: '.pdf,application/pdf', multiple: true, kind: 'PDF files', filter: isPdf, action: 'Rotate PDF', pick: 'Choose PDF files', zipName: 'rotated-pdfs.zip',
      options:
        '<label class="field">Rotate<select data-a><option value="90">90° clockwise</option><option value="180">180°</option><option value="270">90° anticlockwise</option></select></label>' +
        '<label class="field">Pages <small>leave empty for all pages</small><input type="text" data-r placeholder="All pages"></label>' });
    sh.onRun(async function (files, say) {
      var L = await pdflib(), angle = +sh.opt('[data-a]').value, rtext = sh.opt('[data-r]').value.trim(), out = [];
      for (var i = 0; i < files.length; i++) {
        var f = files[i]; say('Rotating ' + f.name + '…'); await tick();
        try {
          var d = await loadPdfLibDoc(L, f), pages = d.getPages(), pick = null;
          if (rtext) { pick = {}; parseRanges(rtext, pages.length).forEach(function (r) { for (var k = r[0]; k <= r[1]; k++) pick[k - 1] = 1; }); }
          pages.forEach(function (p, k) { if (!pick || pick[k]) p.setRotation(L.degrees((p.getRotation().angle + angle) % 360)); });
          out.push({ name: baseName(f.name) + '-rotated.pdf', blob: pdfBlob(await d.save()), before: f.size });
        } catch (e) { out.push({ name: f.name, error: e.message }); }
      }
      return out;
    });
  };

  T.img2pdf = function (root) {
    var sh = shell(root, { accept: IMG_ACCEPT, multiple: true, reorder: true, kind: 'images', filter: isImage, action: 'Create PDF', pick: 'Choose images',
      options:
        '<label class="field">Page size<select data-size><option value="a4">A4</option><option value="letter">US Letter</option><option value="fit">Same as each image</option></select></label>' +
        '<label class="field">Orientation<select data-or><option value="auto">Automatic</option><option value="p">Portrait</option><option value="l">Landscape</option></select></label>' +
        '<label class="field">Margin<select data-m><option value="0">None</option><option value="28" selected>Small</option><option value="57">Large</option></select></label>' });
    sh.onRun(async function (files, say) {
      var L = await pdflib(), doc = await L.PDFDocument.create(), size = sh.opt('[data-size]').value, or = sh.opt('[data-or]').value, m = +sh.opt('[data-m]').value;
      var sizes = { a4: [595.28, 841.89], letter: [612, 792] }, before = 0;
      for (var i = 0; i < files.length; i++) {
        var f = files[i]; before += f.size;
        say('Adding image ' + (i + 1) + ' of ' + files.length + '…'); await tick();
        var src = await decodeImage(f), d = dims(src), s = Math.min(1, 3508 / Math.max(d.w, d.h));
        var cv = drawScaled(src, d.w * s, d.h * s, '#ffffff');
        var img = await doc.embedJpg(await (await toBlob(cv, 'image/jpeg', 0.9)).arrayBuffer());
        var pw, ph;
        if (size === 'fit') { pw = cv.width * 0.75 + 2 * m; ph = cv.height * 0.75 + 2 * m; }
        else {
          pw = sizes[size][0]; ph = sizes[size][1];
          var land = or === 'l' || (or === 'auto' && cv.width > cv.height);
          if (land) { var t = pw; pw = ph; ph = t; }
        }
        var page = doc.addPage([pw, ph]), k = Math.min((pw - 2 * m) / cv.width, (ph - 2 * m) / cv.height);
        var iw = cv.width * k, ih = cv.height * k;
        page.drawImage(img, { x: (pw - iw) / 2, y: (ph - ih) / 2, width: iw, height: ih });
      }
      say('Saving…');
      return [{ name: (files.length === 1 ? baseName(files[0].name) : 'images') + '.pdf', blob: pdfBlob(await doc.save()), before: before, note: files.length + (files.length === 1 ? ' page' : ' pages') }];
    });
  };

  async function openPdfjs(f) {
    var lib = await pdfjs();
    try { return await lib.getDocument({ data: new Uint8Array(await f.arrayBuffer()) }).promise; }
    catch (e) {
      if (e && e.name === 'PasswordException') throw new Error(f.name + ' is password-protected. Remove the password first, then try again.');
      throw new Error(f.name + ' could not be opened. It may be damaged or not a real PDF.');
    }
  }
  async function renderPage(doc, num, scale, bg) {
    var page = await doc.getPage(num), vp = page.getViewport({ scale: scale });
    var lim = 8000 / Math.max(vp.width, vp.height);
    if (lim < 1) vp = page.getViewport({ scale: scale * lim });
    var cv = canvasOf(vp.width, vp.height, bg === undefined ? '#ffffff' : bg);
    var ro = { canvasContext: cv.getContext('2d'), viewport: vp };
    if (bg === null) ro.background = 'rgba(0,0,0,0)';
    await page.render(ro).promise;
    var base = page.getViewport({ scale: 1 });
    page.cleanup();
    return { canvas: cv, wPt: base.width, hPt: base.height };
  }

  T.pdf2img = function (root, c) {
    c = c || {};
    var pngFirst = c.fmt === 'png';
    var sh = shell(root, { accept: '.pdf,application/pdf', multiple: false, kind: 'a PDF file', filter: isPdf, action: 'Convert to images', pick: 'Choose a PDF file', zipName: 'pdf-pages.zip',
      options:
        '<label class="field">Image quality<select data-dpi><option value="150">Standard (150 DPI)</option><option value="300">High, for printing (300 DPI)</option><option value="96">Small, for sharing (96 DPI)</option></select></label>' +
        '<label class="field">Format<select data-fmt><option value="image/jpeg"' + (pngFirst ? '' : ' selected') + '>JPG</option><option value="image/png"' + (pngFirst ? ' selected' : '') + '>PNG</option></select></label>' +
        (c.transparent ? '<label class="check"><input type="checkbox" data-clear checked> Transparent background (PNG only)</label>' : '') +
        '<label class="field">Pages <small data-info></small><input type="text" data-r placeholder="All pages"></label>' });
    pageCountHint(sh);
    sh.onRun(async function (files, say) {
      var f = files[0], doc = await openPdfjs(f), n = doc.numPages, mime = sh.opt('[data-fmt]').value, scale = +sh.opt('[data-dpi]').value / 72;
      var clear = !!(sh.opt('[data-clear]') && sh.opt('[data-clear]').checked) && mime === 'image/png';
      var rt = sh.opt('[data-r]').value.trim(), list = [];
      if (rt) parseRanges(rt, n).forEach(function (r) { for (var k = r[0]; k <= r[1]; k++) list.push(k); });
      else for (var k2 = 1; k2 <= n; k2++) list.push(k2);
      var out = [];
      for (var i = 0; i < list.length; i++) {
        say('Rendering page ' + list[i] + ' (' + (i + 1) + ' of ' + list.length + ')…');
        var r = await renderPage(doc, list[i], scale, clear ? null : undefined);
        out.push({ name: baseName(f.name) + '-page-' + list[i] + '.' + extFor(mime), blob: await toBlob(r.canvas, mime, 0.9), note: r.canvas.width + ' × ' + r.canvas.height + ' px' });
        r.canvas.width = r.canvas.height = 0;
      }
      doc.destroy();
      return out;
    });
  };

  T.compresspdf = function (root, c) {
    var presets = c.presets || [100, 200, 500, 1000, 2000];
    var sh = shell(root, { accept: '.pdf,application/pdf', multiple: false, kind: 'a PDF file', filter: isPdf, action: 'Compress PDF', pick: 'Choose a PDF file',
      options:
        '<div class="field wide">Target size <div class="inline"><input type="number" min="20" step="1" value="' + (c.target || 200) + '" data-target aria-label="Target size in KB" style="width:110px"> <span>KB or less</span></div>' +
        chipsHTML('t', presets, c.target || 200, 'KB') + '</div>' +
        '<label class="check"><input type="checkbox" data-gray> Black and white (much smaller for scanned documents)</label>' +
        '<p class="field wide" style="font-weight:400;margin:0"><small>Pages are saved as images to reach the size you need, so text in the result cannot be selected or searched.</small></p>' });
    var tIn = sh.opt('[data-target]'); wireChips(sh, 't', tIn);
    sh.onRun(async function (files, say) {
      var f = files[0], target = Math.round(+tIn.value * 1024), gray = sh.opt('[data-gray]').checked;
      if (!(target >= 20 * 1024)) throw new Error('Enter a target of at least 20 KB.');
      if (f.size <= target) return [{ name: f.name, blob: f, before: f.size, target: target, note: 'Already under ' + fmt(target) + ', kept as is' }];
      var doc = await openPdfjs(f), n = doc.numPages;
      var ladder = [[2, .75], [1.7, .65], [1.45, .58], [1.25, .52], [1.1, .46], [1, .4], [.85, .36], [.72, .32], [.62, .28], [.52, .25], [.44, .22], [.36, .2]];
      var best = null;
      for (var s = 0; s < ladder.length; s++) {
        var sc = ladder[s][0], q = ladder[s][1], pages = [], sum = 0;
        say('Trying quality level ' + (s + 1) + ' of ' + ladder.length + '…');
        for (var p = 1; p <= n; p++) {
          var r = await renderPage(doc, p, sc);
          if (gray) {
            var ctx = r.canvas.getContext('2d'), id = ctx.getImageData(0, 0, r.canvas.width, r.canvas.height), a = id.data;
            for (var k = 0; k < a.length; k += 4) { var y = a[k] * .299 + a[k + 1] * .587 + a[k + 2] * .114; a[k] = a[k + 1] = a[k + 2] = y; }
            ctx.putImageData(id, 0, 0);
          }
          var b = await toBlob(r.canvas, 'image/jpeg', q);
          r.canvas.width = r.canvas.height = 0;
          pages.push({ b: b, w: r.wPt, h: r.hPt }); sum += b.size;
          if (sum > target * 1.05 && s < ladder.length - 1) break;
        }
        if (pages.length < n) continue;
        best = pages;
        if (sum <= target * 0.97) break;
      }
      say('Saving…');
      var L = await pdflib(), out = await L.PDFDocument.create();
      for (var i = 0; i < best.length; i++) {
        var img = await out.embedJpg(await best[i].b.arrayBuffer()), pg = out.addPage([best[i].w, best[i].h]);
        pg.drawImage(img, { x: 0, y: 0, width: best[i].w, height: best[i].h });
      }
      doc.destroy();
      var blob = pdfBlob(await out.save());
      var note = n + (n === 1 ? ' page' : ' pages');
      if (blob.size > target) note += '. This is the smallest readable result. Try fewer pages, black and white, or a larger target';
      if (blob.size >= f.size) return [{ name: f.name, blob: f, before: f.size, target: target, note: 'Could not make this file smaller, kept the original' }];
      return [{ name: baseName(f.name) + '-compressed.pdf', blob: blob, before: f.size, target: target, note: note }];
    });
  };

  
  TF.register(T);
})(window.TF);

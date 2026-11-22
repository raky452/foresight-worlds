/* Lite YouTube showcase: posters only until the visitor presses play (no iframe on load). */
(function () {
  function buildIframe(id, title) {
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&modestbranding=1&playsinline=1';
    f.title = title;
    f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
    f.allowFullscreen = true;
    f.className = 'tfv-frame';
    return f;
  }
  function init(root) {
    var stage = root.querySelector('.tfv-stage');
    var tabs = root.querySelectorAll('.tfv-tab');
    var poster = stage.querySelector('.tfv-poster');
    function show(btn) {
      tabs.forEach(function (t) { t.setAttribute('aria-pressed', t === btn ? 'true' : 'false'); });
      var id = btn.getAttribute('data-id');
      var old = stage.querySelector('.tfv-frame');
      if (old) old.remove();
      poster.hidden = false;
      poster.setAttribute('data-id', id);
      poster.setAttribute('aria-label', 'Play ' + btn.getAttribute('data-title'));
      poster.querySelector('img').src = 'https://i.ytimg.com/vi/' + id + '/hqdefault.jpg';
      poster.querySelector('img').alt = btn.getAttribute('data-title');
      var cap = root.querySelector('.tfv-caption');
      if (cap) cap.textContent = btn.getAttribute('data-caption');
    }
    tabs.forEach(function (t) { t.addEventListener('click', function () { show(t); }); });
    poster.addEventListener('click', function () {
      var id = poster.getAttribute('data-id');
      var cur = root.querySelector('.tfv-tab[aria-pressed="true"]');
      poster.hidden = true;
      stage.appendChild(buildIframe(id, cur ? cur.getAttribute('data-title') : 'Video'));
    });
  }
  function boot() { document.querySelectorAll('[data-tf-video]').forEach(init); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();

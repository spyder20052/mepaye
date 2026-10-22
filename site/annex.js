/* =========================================================
   mepaye · standard des pages annexes · JS natif
   Barre de chapitres (collante, suit la lecture), explorateurs
   de modules (onglets au clavier), objet vivant de l'ouverture.
   ========================================================= */
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- barre de chapitres ---------- */
  const bar = $('[data-ax-bar]');
  if (bar) {
    const inner = $('.ax-bar__in', bar), ind = $('[data-ax-ind]', bar), links = $$('[data-ax-link]', bar);
    const chaps = links.map((a) => document.getElementById(a.hash.slice(1))).filter(Boolean);
    let cur = null;
    const place = (a) => {
      if (!a) { ind.style.opacity = '0'; return; }
      ind.style.opacity = '1';
      ind.style.width = `${a.offsetWidth}px`;
      ind.style.transform = `translateX(${a.offsetLeft}px)`;
      const left = a.offsetLeft - (inner.clientWidth - a.offsetWidth) / 2;
      inner.scrollTo({ left, behavior: reduce ? 'auto' : 'smooth' });
    };
    const setCur = (id) => {
      if (id === cur) return;
      cur = id;
      links.forEach((a) => {
        const on = a.hash.slice(1) === id;
        a.classList.toggle('is-on', on);
        if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      });
      place(links.find((a) => a.classList.contains('is-on')));
    };
    // le chapitre en cours : celui qui traverse le milieu de l'écran
    const seen = new Map();
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => seen.set(e.target.id, e.isIntersecting));
      const on = chaps.find((c) => seen.get(c.id));
      setCur(on ? on.id : null);
    }, { rootMargin: '-45% 0px -54% 0px' });
    chaps.forEach((c) => io.observe(c));
    // collée en haut : elle se décale sous la navigation quand celle-ci revient
    const sentinel = document.createElement('span');
    sentinel.setAttribute('aria-hidden', 'true');
    bar.before(sentinel);
    new IntersectionObserver(([e]) => bar.classList.toggle('is-stuck', !e.isIntersecting && e.boundingClientRect.top < 0)).observe(sentinel);
    links.forEach((a) => a.addEventListener('click', (e) => {
      const t = document.getElementById(a.hash.slice(1));
      if (!t) return;
      e.preventDefault();
      t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      history.replaceState(null, '', a.hash);
      t.setAttribute('tabindex', '-1');
      t.focus({ preventScroll: true });
    }));
    addEventListener('resize', () => place(links.find((a) => a.classList.contains('is-on'))));
  }

  /* ---------- explorateurs de modules ---------- */
  $$('[data-fxe]').forEach((box) => {
    const tabs = $$('[data-fxe-tab]', box), pvs = $$('[data-fxe-pv]', box), panel = $('[role="tabpanel"]', box);
    const pick = (t, focus) => {
      tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; });
      pvs.forEach((p) => p.classList.toggle('is-on', p.dataset.fxePv === t.dataset.fxeTab));
      panel.setAttribute('aria-labelledby', t.id);
      if (focus) t.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => pick(t));
      t.addEventListener('keydown', (e) => {
        const n = tabs.length;
        const k = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: n - 1 }[e.key];
        if (k === undefined) return;
        e.preventDefault();
        pick(tabs[(k + n) % n], true);
      });
    });
  });

  /* ---------- questions : ouverture et fermeture qui se déroulent ---------- */
  $$('details.ax-q').forEach((d) => {
    const sum = $('summary', d), body = $('.ax-q__a', d);
    if (!body) return;
    let anim = null;
    const ease = 'cubic-bezier(.32, .72, 0, 1)';
    const run = (from, to, open) => {
      if (anim) anim.cancel();
      d.classList.toggle('is-opening', open);
      d.classList.toggle('is-closing', !open);
      if (open) requestAnimationFrame(() => d.classList.remove('is-opening'));
      anim = body.animate({ height: [`${from}px`, `${to}px`] }, { duration: reduce ? 0 : 520, easing: ease });
      anim.onfinish = () => {
        anim = null;
        body.style.height = '';
        d.classList.remove('is-closing');
        if (!open) d.open = false;
      };
    };
    sum.addEventListener('click', (e) => {
      e.preventDefault();
      if (reduce) { d.open = !d.open; return; }
      if (!d.open || d.classList.contains('is-closing')) {
        const from = d.classList.contains('is-closing') ? body.offsetHeight : 0;
        d.open = true;
        run(from, body.scrollHeight, true);
      } else {
        run(body.offsetHeight, 0, false);
      }
    });
  });

  /* ---------- Tarifs : simulateur et packs de crédits ---------- */
  const nf = new Intl.NumberFormat('fr-FR');
  const fmt = (n) => nf.format(Math.round(n)).replace(/[  ]/g, ' ');
  const tss = $('[data-tss]');
  if (tss) {
    const pr = $('[data-tss-price]', tss), qt = $('[data-tss-qty]', tss);
    const fill = (r) => r.style.setProperty('--p', `${((r.value - r.min) / (r.max - r.min)) * 100}%`);
    const calc = () => {
      const g = pr.value * qt.value, f = g * .05;
      $('[data-tss-o-price]', tss).textContent = `${fmt(pr.value)} XOF`;
      $('[data-tss-o-qty]', tss).textContent = fmt(qt.value);
      $('[data-tss-gross]', tss).textContent = `${fmt(g)} XOF`;
      $('[data-tss-fee]', tss).textContent = `− ${fmt(f)} XOF`;
      $('[data-tss-net]', tss).textContent = `${fmt(g - f)} XOF`;
      fill(pr); fill(qt);
    };
    [pr, qt].forEach((r) => r.addEventListener('input', calc));
    calc();
  }
  /* grille des packs : payer avec le wallet ajoute 10 % de crédits */
  const tg = $('[data-tg]'), sw = $('[data-tg-wallet]');
  if (tg && sw) {
    const swap = (el, v) => { el.textContent = v; if (!reduce) { el.classList.remove('is-swap'); void el.offsetWidth; el.classList.add('is-swap'); } };
    const note = $('[data-tg-note]');
    sw.addEventListener('change', () => {
      const k = sw.checked ? 1.1 : 1;
      tg.classList.toggle('is-wallet', sw.checked);
      $$('[data-tg-col]', tg).forEach((c) => {
        const cr = Math.round(+c.dataset.cr * k);
        $$('[data-tg-cr]', c).forEach((el) => swap(el, fmt(cr)));
        $$('[data-tg-eb]', c).forEach((el) => swap(el, fmt(Math.floor(cr / 50))));
        $$('[data-tg-fo]', c).forEach((el) => swap(el, fmt(Math.floor(cr / 80))));
        $$('[data-tg-ebw]', c).forEach((el) => { el.textContent = Math.floor(cr / 50) > 1 ? 'ebooks' : 'ebook'; });
        $$('[data-tg-fow]', c).forEach((el) => { el.textContent = Math.floor(cr / 80) > 1 ? 'formations' : 'formation'; });
      });
      if (note) note.textContent = sw.checked ? 'Avec 10 % de crédits offerts en payant depuis votre wallet.' : 'Crédits du pack, hors bonus du wallet.';
    });
  }

  /* ---------- Affiliation : simulateur et réglage de la commission ---------- */
  const afs = $('[data-afs]');
  if (afs) {
    const pr = $('[data-afs-price]', afs), rt = $('[data-afs-rate]', afs), nb = $('[data-afs-n]', afs);
    const fill = (r) => r.style.setProperty('--p', `${((r.value - r.min) / (r.max - r.min)) * 100}%`);
    const calc = () => {
      const one = pr.value * .95 * rt.value / 100, tot = one * nb.value;
      $('[data-afs-o-price]', afs).textContent = `${fmt(pr.value)} XOF`;
      $('[data-afs-o-rate]', afs).textContent = `${rt.value} %`;
      $('[data-afs-o-n]', afs).textContent = fmt(nb.value);
      $('[data-afs-one]', afs).textContent = `${fmt(one)} XOF`;
      $('[data-afs-total]', afs).textContent = `${fmt(tot)} XOF`;
      $('[data-afs-cr]', afs).textContent = `${fmt(tot * 1.1)} XOF`;
      [pr, rt, nb].forEach(fill);
    };
    [pr, rt, nb].forEach((r) => r.addEventListener('input', calc));
    calc();
  }
  const afc = $('[data-afc]');
  if (afc) {
    const sync = () => {
      const net = 25000 * .95, a = net * afc.value / 100;
      $('[data-afc-o]').textContent = `${afc.value} %`;
      $('[data-afc-a]').textContent = fmt(a);
      $('[data-afc-y]').textContent = fmt(net - a);
      afc.style.setProperty('--p', `${((afc.value - afc.min) / (afc.max - afc.min)) * 100}%`);
    };
    afc.addEventListener('input', sync); sync();
  }

  /* ---------- l'objet vivant de l'ouverture ---------- */
  const fxh = $('[data-fxh]');
  if (fxh && !reduce) {
    const cards = $$('[data-fxh-s]', fxh), steps = $$('.fxh__steps li', fxh.parentElement);
    let k = 0, timer = null, paused = false;
    const go = () => {
      if (paused) return;
      k = (k + 1) % cards.length;
      cards.forEach((c, i) => c.classList.toggle('is-on', i === k));
      steps.forEach((s, i) => s.classList.toggle('is-on', i === k));
    };
    const fig = fxh.closest('figure');
    fig.addEventListener('mouseenter', () => { paused = true; });
    fig.addEventListener('mouseleave', () => { paused = false; });
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting && !timer) timer = setInterval(go, 3200);
      else if (!e.isIntersecting && timer) { clearInterval(timer); timer = null; }
    }).observe(fig);
  }
})();

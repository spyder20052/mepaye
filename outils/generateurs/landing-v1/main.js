/* =========================================================
   mepaye · landing v2 · JS natif, sans dépendance
   Une seule boucle rAF : chaque scène suit le scroll avec un
   amorti (lerp), seules transform et opacity sont animées, les
   positions sont mesurées une fois puis mises en cache.
   ========================================================= */
(() => {
  'use strict';

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, t) => a + (b - a) * t;
  const ease = (t) => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const easeOut = (t) => 1 - Math.pow(1 - t, 3);
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const nf = new Intl.NumberFormat('fr-FR');
  const fmt = (n) => nf.format(Math.round(n)).replace(/[  ]/g, ' ');
  const xof = (n) => `${fmt(n)} XOF`;
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  const tween = (from, to, dur, cb, done) => {
    if (reduce) { cb(to); done && done(); return; }
    const t0 = performance.now();
    const step = (now) => {
      const t = clamp((now - t0) / dur);
      cb(from + (to - from) * easeOut(t));
      t < 1 ? requestAnimationFrame(step) : done && done();
    };
    requestAnimationFrame(step);
  };
  const watch = (el, cb, threshold = 0.2) => {
    if (!el) return;
    new IntersectionObserver((es) => es.forEach((e) => cb(e.isIntersecting)), { threshold }).observe(el);
  };

  let vw = innerWidth, vh = innerHeight;

  /* =======================================================
     Moteur de scènes
     ======================================================= */
  const scenes = [];
  const scene = (el, opts) => { if (!el) return null; const s = { el, top: 0, h: 0, tgt: 0, cur: -1, prev: null, ...opts }; scenes.push(s); return s; };
  const pinProgress = (s, y) => clamp((y - s.top) / Math.max(1, s.h - vh));
  const enterProgress = (s, y, span = .85) => clamp((y + vh - s.top) / (vh * span));

  const measure = () => {
    vw = innerWidth; vh = innerHeight;
    scenes.forEach((s) => { s.pre && s.pre(); });
    const y = scrollY;
    scenes.forEach((s) => {
      const r = s.el.getBoundingClientRect();
      s.top = r.top + y; s.h = s.el.offsetHeight;
      s.post && s.post();
    });
    docH = Math.max(1, document.documentElement.scrollHeight - vh);
    onScroll();
  };

  // la position de défilement est lue une seule fois, à l'événement de défilement, puis réutilisée :
  // la relire après que les scènes ont écrit leurs styles forcerait un recalcul de la page à chaque image
  let sy = scrollY;
  let raf = 0, last = 0;
  const tick = (now) => {
    const dt = Math.min(64, now - last); last = now;
    const k = reduce ? 1 : 1 - Math.pow(1 - .15, dt / 16.67);
    const y = sy;
    let moving = false;
    for (const s of scenes) {
      const d = s.tgt - s.cur;
      if (Math.abs(d) > .0004) {
        let st = d * k;
        if (s.maxStep && !reduce) { const m = s.maxStep * dt / 16.67; st = clamp(st, -m, m); }
        s.cur += st; moving = true;
      } else s.cur = s.tgt;
      const near = y + vh > s.top - vh * .3 && y < s.top + s.h + vh * .3;
      if (near && s.cur !== s.prev) { s.render(s.cur); s.prev = s.cur; }
    }
    raf = moving ? requestAnimationFrame(tick) : 0;
  };
  const kick = () => { if (!raf) { last = performance.now(); raf = requestAnimationFrame(tick); } };

  /* =======================================================
     Navigation : les pages du site, partout
     - la barre montre toujours les liens du site
     - on descend : elle s'efface ; on remonte, on approche du
       bord haut ou on tabule : elle revient
     ======================================================= */
  const navEl = $('[data-nav]'), navBar = $('[data-nav-bar]');
  let lastY = scrollY, acc = 0, docH = 1;
  const setMode = (cls, on) => root.classList.toggle(cls, on);
  const showNav = () => { setMode('nav-hide', false); acc = 0; };
  const navUpdate = (y) => {
    const dy = y - lastY; lastY = y;
    setMode('is-scrolled', y > 4);
    navEl.style.setProperty('--pg', clamp(y / docH).toFixed(4));
    if (root.classList.contains('is-menu')) return;
    if (y < 80) { showNav(); return; }
    // seuils larges : un petit rebond du pavé tactile ne fait plus monter et descendre la barre
    acc = Math.sign(dy) === Math.sign(acc) ? acc + dy : dy;
    if (acc > 56) setMode('nav-hide', true);
    else if (acc < -40) showNav();
  };
  if (fine) addEventListener('pointermove', (e) => { if (e.clientY < 10) showNav(); }, { passive: true });
  navEl.addEventListener('focusin', showNav);

  const onScroll = () => {
    const y = sy = scrollY;
    navUpdate(y);
    for (const s of scenes) s.tgt = s.progress(s, y);
    kick();
  };
  addEventListener('scroll', onScroll, { passive: true });

  // ancres : défilement doux, avec le décalage de la barre
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href').slice(1);
    const t = id && document.getElementById(id);
    if (!t) return;
    e.preventDefault();
    const top = id === 'accueil' ? 0 : t.getBoundingClientRect().top + scrollY - 24;
    scrollTo({ top, behavior: reduce ? 'auto' : 'smooth' });
    if (id !== 'contenu') history.replaceState(null, '', id === 'accueil' ? location.pathname : `#${id}`);
  });

  /* Tarifs : la notification de retrait passe d'un opérateur Mobile Money à l'autre */
  const wdc = $('[data-wd-cycle]');
  if (wdc && !reduce) {
    const WD = [
      ['MTN MoMo', 'mtn-momo', '566 200', 'il y a 2 min'], ['Wave', 'wave', '312 500', 'à l’instant'],
      ['Orange Money', 'orange-money', '128 900', 'il y a 1 min'], ['Moov Money', 'moov-money', '245 000', 'à l’instant'],
      ['Airtel Money', 'airtel-money', '98 400', 'il y a 3 min'], ['Mixx by Yas', 'mixx-tg', '410 750', 'à l’instant'],
      ['Flooz', 'flooz', '75 300', 'il y a 1 min'], ['M-Pesa', 'm-pesa', '189 600', 'à l’instant'],
      ['Celtiis Cash', 'celtiis', '152 000', 'il y a 2 min'],
    ];
    // on précharge les logos pour que le changement soit net
    WD.forEach((w) => { new Image().src = `assets/logos/pm/${w[1]}.webp`; });
    const parts = { app: $('[data-wd-app]', wdc), logo: $('[data-wd-logo]', wdc), amt: $('[data-wd-amt]', wdc), when: $('[data-wd-when]', wdc) };
    let wi = 0, wdTimer = 0, wdSeen = false, wdHover = false;
    const swap = async () => {
      wi = (wi + 1) % WD.length;
      const [app, logo, amt, when] = WD[wi];
      // on anime le contenu, pas la carte : son léger flottement continue
      const kids = [...wdc.children];
      await Promise.all(kids.map((k, j) => k.animate([{ opacity: 1, transform: 'none', filter: 'blur(0)' }, { opacity: 0, transform: 'translateY(-6px)', filter: 'blur(3px)' }], { duration: 240, delay: j * 40, easing: 'cubic-bezier(.4,0,1,1)', fill: 'forwards' }).finished));
      parts.app.textContent = app; parts.logo.src = `assets/logos/pm/${logo}.webp`; parts.amt.textContent = amt; parts.when.textContent = when;
      kids.forEach((k, j) => k.animate([{ opacity: 0, transform: 'translateY(8px)', filter: 'blur(3px)' }, { opacity: 1, transform: 'none', filter: 'blur(0)' }], { duration: 520, delay: j * 60, easing: 'cubic-bezier(.22,1,.36,1)', fill: 'forwards' }));
    };
    const loop = () => { clearTimeout(wdTimer); if (wdSeen && !wdHover && !document.hidden) wdTimer = setTimeout(() => { swap().then(loop); }, 2600); };
    new IntersectionObserver(([e]) => { wdSeen = e.isIntersecting; loop(); }).observe(wdc);
    wdc.addEventListener('pointerenter', () => { wdHover = true; clearTimeout(wdTimer); });
    wdc.addEventListener('pointerleave', () => { wdHover = false; loop(); });
    document.addEventListener('visibilitychange', loop);
  }

  /* Accueil : le menu de la landing suit la section lue,
     « Pages » ouvre les autres pages du site */
  const land = $('[data-land]');
  if (land) {
    const ind = $('[data-land-ind]', land);
    const links = $$('[data-land-link]', land);
    const secs = links.map((a) => document.getElementById(a.getAttribute('href').slice(1)));
    let on = -1;
    const place = () => {
      const a = links[on];
      ind.classList.toggle('is-on', !!a);
      if (a) { ind.style.width = `${a.offsetWidth}px`; ind.style.transform = `translateX(${a.offsetLeft}px)`; }
    };
    // les positions des sections sont mesurées une fois (et à chaque changement de taille),
    // jamais pendant le défilement : lire une position force le navigateur à recalculer la page
    let tops = [];
    const measureLand = () => { const y = scrollY; tops = secs.map((sec) => (sec ? sec.getBoundingClientRect().top + y : Infinity)); };
    const spy = () => {
      const line = sy + vh * .35;
      let i = -1;
      tops.forEach((t, k) => { if (t <= line) i = k; });
      if (i === on) return;
      on = i;
      links.forEach((a, k) => {
        a.classList.toggle('is-on', k === i);
        if (k === i) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      });
      place();
    };
    let spyRaf = 0;
    addEventListener('scroll', () => { if (!spyRaf) spyRaf = requestAnimationFrame(() => { spyRaf = 0; spy(); }); }, { passive: true });
    const remeasureLand = () => { measureLand(); on = -2; spy(); place(); };
    addEventListener('resize', remeasureLand, { passive: true });
    addEventListener('load', remeasureLand);
    if (document.fonts) document.fonts.ready.then(remeasureLand);
    if ('ResizeObserver' in window) new ResizeObserver(remeasureLand).observe(document.body);
    measureLand();
    spy();
  }

  const pagesBtn = $('[data-pages]'), pagesPop = $('[data-pages-pop]');
  if (pagesBtn && pagesPop) {
    const setPop = (open, focus) => {
      pagesBtn.setAttribute('aria-expanded', String(open));
      pagesPop.hidden = !open;
      if (open && focus) $('a', pagesPop).focus();
    };
    pagesBtn.addEventListener('click', () => setPop(pagesBtn.getAttribute('aria-expanded') !== 'true'));
    pagesBtn.addEventListener('keydown', (e) => { if (e.key === 'ArrowDown') { e.preventDefault(); setPop(true, true); } });
    // flèches haut et bas pour passer d'une page à l'autre dans le panneau
    pagesPop.addEventListener('keydown', (e) => {
      const d = { ArrowDown: 1, ArrowUp: -1 }[e.key];
      if (!d) return;
      e.preventDefault();
      const items = $$('a', pagesPop);
      items[(items.indexOf(document.activeElement) + d + items.length) % items.length].focus();
    });
    document.addEventListener('click', (e) => { if (!pagesPop.hidden && !e.target.closest('.nav__pages')) setPop(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !pagesPop.hidden) { setPop(false); pagesBtn.focus(); } });
    pagesPop.addEventListener('focusout', (e) => { if (!e.relatedTarget || !e.relatedTarget.closest('.nav__pages')) setPop(false); });
    addEventListener('scroll', () => { if (!pagesPop.hidden && root.classList.contains('nav-hide')) setPop(false); }, { passive: true });
  }

  // menu mobile
  const burger = $('[data-burger]');
  const menu = $('[data-menu]');
  const setMenu = (open) => {
    burger.setAttribute('aria-expanded', String(open));
    $('.sr-only', burger).textContent = open ? 'Fermer le menu' : 'Ouvrir le menu';
    root.classList.toggle('is-menu', open);
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) { menu.hidden = false; requestAnimationFrame(() => requestAnimationFrame(() => menu.classList.add('is-open'))); }
    else { menu.classList.remove('is-open'); setTimeout(() => { if (!menu.classList.contains('is-open')) menu.hidden = true; }, 420); }
  };
  burger.addEventListener('click', () => setMenu(burger.getAttribute('aria-expanded') !== 'true'));
  // accueil : le menu bascule entre les sections de la page et les pages du site
  const segs = $$('[data-mseg]', menu);
  segs.forEach((b) => b.addEventListener('click', () => {
    if (b.getAttribute('aria-selected') === 'true') return;
    segs.forEach((x) => x.setAttribute('aria-selected', String(x === b)));
    $$('[data-mlist]', menu).forEach((l) => {
      const on = l.dataset.mlist === b.dataset.mseg;
      l.hidden = !on;
      if (on && !reduce) { l.classList.remove('is-swap'); void l.offsetWidth; l.classList.add('is-swap'); }
    });
  }));
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && root.classList.contains('is-menu')) { setMenu(false); burger.focus(); } });

  /* =======================================================
     Apparitions
     ======================================================= */
  const groups = new Map();
  $$('[data-reveal]').forEach((el) => {
    const i = groups.get(el.parentElement) || 0;
    groups.set(el.parentElement, i + 1);
    if (i) el.style.setProperty('--rd', `${Math.min(i, 4) * .08}s`);
  });
  const rio = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); rio.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
  $$('[data-reveal]').forEach((el) => rio.observe(el));

  /* Boutons magnétiques */
  if (fine && !reduce) {
    $$('[data-magnetic]').forEach((b) => {
      b.addEventListener('pointermove', (e) => {
        const r = b.getBoundingClientRect();
        b.style.translate = `${(((e.clientX - r.left) / r.width - .5) * 8).toFixed(1)}px ${(((e.clientY - r.top) / r.height - .5) * 6).toFixed(1)}px`;
      });
      b.addEventListener('pointerleave', () => (b.style.translate = ''));
    });
  }

  /* =======================================================
     1. HERO · passer la porte
     ======================================================= */
  const hero = $('[data-scene="hero"]');
  const hCopy = $('[data-h-copy]'), hStage = $('[data-h-stage]'), hPerson = $('[data-h-person]'), hFig = $('[data-h-fig]'), hCer = $('[data-h-ceramic]');
  const hFill = $('[data-h-fill]'), hInside = $('[data-h-inside]'), hPhone = $('[data-h-phone]'), hInsideT = $('.hero__inside-t');
  const hBanner = $('[data-h-banner]');
  const floats = $$('.fl', hero).map((el) => { const [x, y] = (el.dataset.fl || '0,0').split(',').map(Number); return { el, x, y, dir: Math.sign(x) || 1 }; });
  let stageRise = 0, archScale = 4, heroBannerOn = false;

  // générique d'ouverture (une fois par visite) : le nom et la vente sont joués en CSS dès le premier
  // affichage ; le script fait voler le logo jusqu'à sa place dans la barre, puis retire le voile
  const intro = $('[data-intro]');
  const introDone = new Promise((resolve) => {
    if (!intro || !root.classList.contains('has-intro')) { if (intro) intro.remove(); resolve(); return; }
    const FLY = 1950, END = 2850; // en ms depuis l'ouverture de la page, comme dans le CSS
    const logo = $('[data-intro-logo]', intro), navLogo = $('.nav__word');
    let over = false;
    const finish = () => {
      if (over) return; over = true;
      root.classList.remove('has-intro');
      try { sessionStorage.setItem('mp_intro', '1'); } catch (e) { /* stockage indisponible */ }
      setTimeout(() => intro.remove(), 60);
    };
    const fly = () => {
      if (over || !navLogo) return;
      const a = logo.getBoundingClientRect(), b = navLogo.getBoundingClientRect();
      intro.classList.add('is-fly');
      // vol en arc doux : le logo rétrécit et rejoint exactement le logo de la barre
      const k = b.width / a.width, dx = b.left - a.left, dy = b.top - a.top;
      logo.animate([
        { transform: 'translate(0, 0) scale(1)' },
        { transform: `translate(${dx}px, ${dy}px) scale(${k})` },
      ], { duration: 820, easing: 'cubic-bezier(.65, 0, .2, 1)', fill: 'forwards' });
      resolve(); // l'accueil s'installe pendant le vol
    };
    const tFly = setTimeout(fly, Math.max(0, FLY - performance.now()));
    const tEnd = setTimeout(finish, Math.max(0, END - performance.now()));
    const skip = () => {
      if (over) return;
      clearTimeout(tFly); clearTimeout(tEnd);
      intro.classList.add('is-skip'); resolve();
      setTimeout(finish, 300);
    };
    $('[data-intro-skip]', intro).addEventListener('click', skip);
    ['pointerdown', 'keydown', 'wheel', 'touchstart'].forEach((ev) => addEventListener(ev, skip, { once: true, passive: true }));
  });

  // entrée
  Promise.all([
    Promise.race([
      Promise.all([hPerson.decode ? hPerson.decode().catch(() => {}) : 0, document.fonts ? document.fonts.ready : 0]),
      sleep(1400),
    ]),
    introDone,
  ]).then(() => requestAnimationFrame(() => root.classList.add('is-ready')));

  /* La traversée de la porte suit le scroll image par image : rien ne bouge
     sans geste. Le rendu amorti a une vitesse plafonnée, si bien qu'un scroll
     très rapide montre quand même le zoom au lieu de le sauter. */
  const heroScene = scene(hero, {
    progress: pinProgress,
    post() {
      const sr = hStage.offsetTop;
      const aw = hStage.offsetWidth, ah = hStage.offsetHeight;
      stageRise = Math.max(0, sr - vh * (vw < 900 ? .2 : .13));
      // échelle à laquelle l'ouverture bleue de la céramique couvre tout l'écran
      const ow = hCer.offsetWidth * .457, oh = hCer.offsetHeight * .65;
      archScale = Math.max(vw / ow, vh / (oh * .7)) * 1.12;
      // chaque carte s'écarte vers le bord dont elle est la plus proche
      floats.forEach((f) => { f.dir = f.el.offsetLeft + f.el.offsetWidth / 2 < aw / 2 ? -1 : 1; });
    },
    maxStep: .02, // au plus 2 % de la progression par image : ~0,6 s minimum pour traverser la porte
    render(p) { if (!reduce) this.draw(p); },
    draw(p) {
      // séquence (p de 0 à SEQ) : ouverture courte, puis le zoom occupe l'essentiel du temps
      const a = ease(clamp(p / .16));
      const b = ease(clamp((p - .1) / .3));
      // sur téléphone l'ouverture couvre l'écran plus tôt : la scène intérieure arrive plus tôt,
      // pour qu'il n'y ait jamais d'écran tout bleu à faire défiler
      const k = vw < 900 ? .44 : .58;
      const c = ease(clamp((p - (k + .02)) / .12));
      hCopy.style.transform = `translate3d(0, ${(-a * 90).toFixed(1)}px, 0)`;
      hCopy.style.opacity = (1 - clamp(p / .1)).toFixed(3);
      hCopy.style.visibility = p > .12 ? 'hidden' : '';
      hStage.style.transform = `translate3d(0, ${(-a * stageRise).toFixed(1)}px, 0)`;
      // 1. la créatrice s'efface en glissant doucement, bien avant d'atteindre le sol de l'arche
      const f = clamp((p - .02) / .1), fe = ease(f);
      hPerson.style.transform = `translate3d(0, ${(f * f * 22).toFixed(2)}%, 0) scale(${(1 - fe * .04).toFixed(4)})`;
      hFig.style.visibility = f >= 1 ? 'hidden' : '';
      // 2. puis la caméra avance dans l'ouverture bleue de l'arche jusqu'à la remplir
      // zoom à vitesse perçue constante : l'échelle progresse de façon géométrique
      const z = clamp((p - .1) / (vw < 900 ? .38 : .52)), ze = z * z * (3 - 2 * z);
      hCer.style.transform = `scale(${Math.pow(archScale, ze).toFixed(4)})`;
      // sur mobile, les cartes sont de l'autre côté de la scène : elles s'écartent vers leur bord, et plus tôt
      const narrow = vw < 900;
      const fo = 1 - clamp((p - .01) / (narrow ? .07 : .09));
      const fe2 = ease(clamp((p - .02) / .08));
      const push = (a * 1.2 + b * 2) * 140;
      hFig.style.opacity = (1 - fe2).toFixed(3);
      floats.forEach((f) => {
        const fx = Math.abs(f.x) * f.dir;
        f.el.style.transform = `translate3d(${(fx * push).toFixed(1)}px, ${(f.y * push).toFixed(1)}px, 0)`;
        f.el.style.opacity = fo.toFixed(3);
        f.el.style.visibility = fo <= 0 ? 'hidden' : '';
      });
      // le bleu plein écran ne tient que le temps du fondu enchaîné avec la scène intérieure
      hFill.style.opacity = clamp((p - k) / .06).toFixed(3);
      hInside.style.opacity = c.toFixed(3);
      hInside.style.visibility = p > k + .02 ? 'visible' : 'hidden';
      hInsideT.style.transform = `translate3d(0, ${((1 - c) * 36).toFixed(1)}px, 0)`;
      hPhone.style.transform = `translate3d(0, ${((1 - c) * vh * .45).toFixed(1)}px, 0) rotateX(${((1 - c) * 30).toFixed(2)}deg) scale(${(.86 + c * .14).toFixed(4)})`;
      const on = p > k + .2;
      if (on !== heroBannerOn) {
        heroBannerOn = on;
        hBanner.classList.toggle('is-on', on);
        if (on) {
          tween(900000, 923750, 900, (v) => ($('[data-hgmv]').textContent = fmt(v)));
          tween(670000, 693750, 900, (v) => ($('[data-hwal]').textContent = fmt(v)));
          $('[data-hsales]').textContent = '125';
        } else {
          $('[data-hgmv]').textContent = '900 000'; $('[data-hwal]').textContent = '670 000'; $('[data-hsales]').textContent = '124';
        }
      }
    },
  });

  // inclinaison des cartes flottantes vers le pointeur
  if (fine && !reduce) {
    let tx = 0, ty = 0, pend = false;
    hero.addEventListener('pointermove', (e) => {
      tx = e.clientX / vw - .5; ty = e.clientY / vh - .5;
      if (pend) return; pend = true;
      requestAnimationFrame(() => {
        pend = false;
        $$('.fl__body', hero).forEach((el, i) => {
          const d = 1 + (i % 3) * .35;
          el.style.transform = `perspective(800px) rotateY(${(tx * 10).toFixed(2)}deg) rotateX(${(-ty * 8).toFixed(2)}deg) translate3d(${(tx * 14 * d).toFixed(1)}px, ${(ty * 10 * d).toFixed(1)}px, 0)`;
        });
      });
    });
    hero.addEventListener('pointerleave', () => $$('.fl__body', hero).forEach((el) => (el.style.transform = '')));
  }

  // notifications du hero : elles arrivent, s'empilent, se balaient
  const stack = $('[data-hnotifs]');
  const hBal = $('[data-hbal]'), hDelta = $('[data-hdelta]'), hBubble = $('[data-hbubble]');
  let balance = 670000;
  const feed = [
    { app: 'mepaye', t: 'Une vente ! mepaye vous paye', s: 'Vous venez de vendre pour 23 750 XOF', v: 23750 },
    { app: 'mepaye', t: 'Une vente ! mepaye vous paye', s: 'Vous venez de vendre pour 4 750 XOF', v: 4750 },
    { app: 'Wave', logo: 'assets/logos/wave.webp', t: 'Retrait reçu', s: '120 000 XOF depuis votre wallet mepaye', v: -120000 },
    { app: 'mepaye', t: 'Une vente ! mepaye vous paye', s: 'Vous venez de vendre pour 47 500 XOF', v: 47500 },
    { app: 'mepaye', t: 'Une vente ! mepaye vous paye', s: 'Vous venez de vendre pour 9 500 XOF', v: 9500 },
  ];
  let fi = 0, nTimer = null;
  const layout = () => {
    $$('.inotif', stack).forEach((n, i) => {
      if (n.dataset.pos === 'gone') return;
      n.dataset.pos = i < 3 ? String(i) : 'out';
      if (i >= 3) setTimeout(() => n.remove(), 700);
    });
  };
  const pushNotif = () => {
    const d = feed[fi++ % feed.length];
    const el = document.createElement('div');
    el.className = 'inotif';
    el.dataset.pos = 'enter';
    el.setAttribute('aria-hidden', 'true');
    el.innerHTML = `<span class="inotif__ic"><img src="${d.logo || 'assets/brand/symbole.svg'}" alt=""></span><span class="inotif__tx"><span class="inotif__top"><b>${d.app}</b><small>maintenant</small></span><b>${d.t}</b><span>${d.s}</span></span>`;
    stack.prepend(el);
    requestAnimationFrame(() => requestAnimationFrame(layout));
    const from = balance; balance = Math.max(0, balance + d.v);
    tween(from, balance, 900, (v) => (hBal.textContent = fmt(v)));
    hDelta.textContent = d.v > 0 ? `+${xof(d.v)}` : `Retrait · ${xof(-d.v)}`;
    hDelta.classList.remove('is-on'); void hDelta.offsetWidth; hDelta.classList.add('is-on');
    if (d.v > 0) { hBubble.classList.remove('is-pop'); void hBubble.offsetWidth; hBubble.classList.add('is-pop'); }
  };
  const startFeed = () => { if (!nTimer && !reduce) nTimer = setInterval(() => { if (heroScene.cur < .1) pushNotif(); }, 3800); };
  const stopFeed = () => { clearInterval(nTimer); nTimer = null; };
  setTimeout(() => { pushNotif(); setTimeout(pushNotif, reduce ? 0 : 900); startFeed(); }, reduce ? 0 : 1600);
  watch(hero, (v) => (v ? startFeed() : stopFeed()), 0);
  document.addEventListener('visibilitychange', () => (document.hidden ? stopFeed() : startFeed()));

  // balayer la notification du dessus
  stack.addEventListener('pointerdown', (e) => {
    const n = e.target.closest('.inotif');
    if (!n || n.dataset.pos !== '0') return;
    const x0 = e.clientX; let dx = 0;
    n.classList.add('is-drag'); n.setPointerCapture(e.pointerId);
    const move = (ev) => { dx = ev.clientX - x0; n.style.transform = `translateX(${dx}px) rotate(${dx * .04}deg)`; n.style.opacity = String(1 - Math.min(.7, Math.abs(dx) / 300)); };
    const up = () => {
      n.removeEventListener('pointermove', move); n.removeEventListener('pointerup', up); n.removeEventListener('pointercancel', up);
      n.classList.remove('is-drag');
      if (Math.abs(dx) > 70) {
        n.dataset.pos = 'gone';
        n.style.transform = `translateX(${Math.sign(dx) * 420}px) rotate(${Math.sign(dx) * 12}deg)`; n.style.opacity = '0';
        setTimeout(() => { n.remove(); layout(); }, 450);
        setTimeout(pushNotif, 380);
      } else { n.style.transform = ''; n.style.opacity = ''; }
    };
    n.addEventListener('pointermove', move); n.addEventListener('pointerup', up); n.addEventListener('pointercancel', up);
  });

  /* =======================================================
     2. VISITE PRODUIT (iPhone collant)
     ======================================================= */
  const story = $('[data-story]');
  const steps = $$('[data-step]'), screensEl = $$('[data-scr]'), railBtns = $$('[data-goto]'), pops = $$('[data-pop]');
  const cam = $('[data-story-cam]'), sArch = $('[data-story-arch]');
  const N = steps.length;
  const cams = [
    { ry: -18, rx: 6, rz: -2, y: 0, s: 1 },
    { ry: 16, rx: 4, rz: 1.5, y: -8, s: 1.02 },
    { ry: -12, rx: -3, rz: -1, y: 4, s: 1 },
    { ry: 14, rx: 5, rz: 2, y: -4, s: 1.03 },
  ];
  let curStep = -1;
  const setStep = (i) => {
    if (i === curStep) return;
    const prev = curStep; curStep = i;
    steps.forEach((s, j) => {
      s.classList.toggle('is-on', j === i);
      s.classList.toggle('is-past', j < i);
      s.inert = j !== i;
      s.setAttribute('aria-hidden', String(j !== i));
    });
    screensEl.forEach((s, j) => { s.classList.toggle('is-on', j === i); s.classList.toggle('is-left', j < i); });
    railBtns.forEach((b, j) => { b.classList.toggle('is-on', j === i); b.setAttribute('aria-current', j === i ? 'step' : 'false'); });
    pops.forEach((p, j) => p.classList.toggle('is-on', j === i));
    placeFocus(i);
    if (prev !== -1 && i === 2 && !reduce) setTimeout(() => simulateSale(true), 700);
  };
  // le projecteur : il éclaire l'élément clé de l'écran, un trait le relie à son étiquette
  const focusEl = $('[data-focus]'), link = $('[data-story-link]');
  const FOCUS = ['.shop__url', '[data-prod-list] .row', '[data-sales-list] .row', '.wcard'];
  let focusT = 0;
  function placeFocus(i) {
    if (!focusEl || !cam) return;
    clearTimeout(focusT);
    const run = () => {
      const scr = screensEl[i], t = scr && $(FOCUS[i], scr), pop = pops[i];
      if (!t || !pop) return;
      const phoneEl = $('.phone--story'), screen = $('.phone__scr', phoneEl);
      const sr = scr.getBoundingClientRect(), tr = t.getBoundingClientRect();
      // position dans l'écran, sans la translation de l'écran qui entre
      const x = tr.left - sr.left, y = tr.top - sr.top, pad = 5;
      Object.assign(focusEl.style, { left: `${x - pad}px`, top: `${y - pad}px`, width: `${tr.width + pad * 2}px`, height: `${tr.height + pad * 2}px`, borderRadius: `${parseFloat(getComputedStyle(t).borderTopLeftRadius) + pad}px` });
      focusEl.classList.add('is-on');
      // l'annotation reprend exactement ce que montre la ligne éclairée
      const amount = $('.row__r b', t), label = $('.row__tx b', t);
      if (i === 2 && amount) {
        const n = amount.firstChild ? amount.firstChild.textContent.trim() : amount.textContent.trim();
        $('.note__v', pop).innerHTML = `${n} <span>XOF</span>`;
      }
      if (i === 1 && amount && label) {
        $('b', pop).textContent = label.textContent.split(':')[0].trim();
        $('small', pop).textContent = `${amount.firstChild.textContent.trim()} XOF · en vente`;
      }
      // l'étiquette, à côté du téléphone, à la hauteur de l'élément (repère : la zone visuelle)
      const vis = cam.parentElement, vr = vis.getBoundingClientRect(), pr = screen.getBoundingClientRect(), fr = phoneEl.getBoundingClientRect();
      const cw = vr.width, right = false, popW = pop.offsetWidth, popH = pop.offsetHeight;
      const tx0 = pr.left - vr.left + x, ty = pr.top - vr.top + y + tr.height / 2;
      const phL = fr.left - vr.left, phR = fr.right - vr.left;
      const gap = 22;
      const narrow = innerWidth < 900;
      // à gauche si l'étiquette tient entre le texte et le téléphone, sinon à droite
      const txt = $('.story__text'), textR = txt ? txt.getBoundingClientRect().right - vr.left + 16 : -1e4;
      const fitsLeft = phL - gap - popW >= textR, fitsRight = phR + gap + popW <= innerWidth - vr.left - 12;
      const onRight = !fitsLeft && fitsRight;
      let px = onRight ? phR + gap : phL - gap - popW;
      if (narrow) px = onRight ? Math.min(cw - popW - 4, phL + (phR - phL) * .55) : Math.max(4, phL + (phR - phL) * .45 - popW);
      px = Math.max(-vr.left + 12, Math.min(innerWidth - vr.left - popW - 12, px));
      // sur téléphone, l'annotation se pose juste sous l'élément, sans le cacher
      const py = narrow ? ty + tr.height / 2 + 12 : ty - popH / 2;
      if (narrow) px = Math.max(4, phL - 28);
      pop.style.left = `${px}px`; pop.style.top = `${py}px`; pop.style.right = 'auto'; pop.style.bottom = 'auto';
      // le trait : du bord de l'élément au bord de l'étiquette
      // le point se pose sur le liseré bleu du projecteur, jamais sur le contenu
      const ax = onRight ? tx0 + tr.width + pad : tx0 - pad, bx = onRight ? px : px + popW;
      link.setAttribute('viewBox', `0 0 ${cw} ${vr.height}`);
      link.style.width = `${cw}px`; link.style.height = `${vr.height}px`;
      const path = $('path', link), dot = $('circle', link);
      path.setAttribute('d', `M${ax} ${ty}H${bx}`);
      dot.setAttribute('cx', ax); dot.setAttribute('cy', ty);
      link.classList.remove('is-on'); void link.offsetWidth; link.classList.add('is-on');
      link.classList.toggle('is-hidden', narrow);
    };
    requestAnimationFrame(run);
    focusT = setTimeout(run, 760);
  }
  addEventListener('resize', () => placeFocus(Math.max(0, curStep)));
  if (story) {
    scene(story, {
      progress: pinProgress,
      render(p) {
        setStep(Math.min(N - 1, Math.floor(p * N)));
        if (reduce) return;
        const f = clamp(p * N - .5, 0, N - 1);
        const i0 = Math.floor(f), i1 = Math.min(N - 1, i0 + 1), t = ease(f - i0);
        const a = cams[i0], b = cams[i1];
        // de face, comme un vrai téléphone posé : seule une légère respiration verticale
        cam.style.transform = `translate3d(0, ${lerp(a.y, b.y, t).toFixed(1)}px, 0)`;
        sArch.style.transform = `translate3d(${((f - 1.5) * -14).toFixed(1)}px, 0, 0) scale(${(1 + Math.sin(f * Math.PI) * .03).toFixed(4)})`;
      },
    });
    railBtns.forEach((b) => b.addEventListener('click', () => {
      const s = scenes.find((x) => x.el === story);
      const i = +b.dataset.goto;
      scrollTo({ top: s.top + ((i + .5) / N) * (s.h - vh), behavior: reduce ? 'auto' : 'smooth' });
    }));
    setStep(0);
  }

  // Boutique en direct
  const shop = $('[data-shop]');
  const slug = (v) => v.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'ma-boutique';
  const nameIn = $('[data-store-name]');
  const syncShop = () => {
    const v = nameIn.value.trim() || 'Ma boutique';
    $('[data-shop-name]').textContent = v;
    $('[data-shop-init]').textContent = v.charAt(0).toUpperCase();
    const d = `${slug(v)}.mepaye.shop`;
    $('[data-shop-url]').textContent = d;
    $('[data-pop-domain]').textContent = d;
  };
  nameIn.addEventListener('input', syncShop);
  $$('input[name="acc"]').forEach((r) => r.addEventListener('change', () => shop.style.setProperty('--accent', r.value)));

  // Ajouter un produit
  const prodList = $('[data-prod-list]');
  const kinds = {
    Ebook: { c: '#1F3A63', i: 'i-book', t: 'Nouvel ebook', p: '5 000' },
    Formation: { c: '#5B2C6F', i: 'i-play', t: 'Nouvelle formation', p: '25 000' },
    Coaching: { c: '#0E8A6A', i: 'i-home', t: 'Séance de coaching', p: '15 000' },
    Template: { c: '#2F5D50', i: 'i-doc', t: 'Nouveau template', p: '3 500' },
    'Communauté': { c: '#D9622B', i: 'i-link', t: 'Groupe privé', p: '2 000' },
  };
  let published = 3;
  $$('[data-add-product] .chip').forEach((chip) => chip.addEventListener('click', () => {
    const k = kinds[chip.dataset.kind];
    const li = document.createElement('li');
    li.className = 'row is-new';
    li.innerHTML = `<span class="row__th" style="--t:${k.c}"><svg><use href="#${k.i}"/></svg></span><span class="row__tx"><b>${k.t}</b><small>${chip.dataset.kind} · 0 vente</small></span><span class="row__r"><b>${k.p} <small>XOF</small></b><i class="live">Live</i></span>`;
    prodList.prepend(li);
    while (prodList.children.length > 6) prodList.lastElementChild.remove();
    if (curStep === 1) placeFocus(1);
    published++;
    $('[data-prod-n]').textContent = published; $('[data-prod-n2]').textContent = published;
    $('[data-prod-count]').textContent = `${published} publiés · 0 brouillon`;
    chip.classList.add('is-done'); setTimeout(() => chip.classList.remove('is-done'), 900);
  }));

  // Simuler une vente
  const salesList = $('[data-sales-list]');
  const sBanner = $('[data-s-banner]');
  const buyers = ['Awa Ndiaye', 'Koffi Mensah', 'Fatou Sow', 'Ibrahim Touré', 'Mariam Keita', 'Yao N’Guessan', 'Aïcha Bamba'];
  const items = [
    { t: 'Formation : vendre en ligne', c: '#5B2C6F', i: 'i-play', v: 23750 },
    { t: 'Guide : lancer sa boutique', c: '#1F3A63', i: 'i-book', v: 4750 },
    { t: 'Modèle de facture freelance', c: '#2F5D50', i: 'i-doc', v: 1900 },
    { t: 'Programme Wellness 30 jours', c: '#0866FF', i: 'i-play', v: 14900 },
  ];
  let net = 855000, settled = 124, bannerT = null;
  const showBanner = (title, sub) => {
    $('[data-s-banner-t]').textContent = title; $('[data-s-banner-s]').textContent = sub;
    sBanner.classList.add('is-on'); clearTimeout(bannerT);
    bannerT = setTimeout(() => sBanner.classList.remove('is-on'), 2600);
  };
  const simulateSale = (quiet) => {
    const it = items[Math.floor(Math.random() * items.length)];
    const who = buyers[Math.floor(Math.random() * buyers.length)];
    const li = document.createElement('li');
    li.className = 'row is-new';
    li.innerHTML = `<span class="row__th" style="--t:${it.c}"><svg><use href="#${it.i}"/></svg></span><span class="row__tx"><b>${it.t}</b><small>${who} · à l’instant</small></span><span class="row__r"><b>+${fmt(it.v)} <small>XOF</small></b><i class="ok">Réglé</i></span>`;
    salesList.prepend(li);
    while (salesList.children.length > 5) salesList.lastElementChild.remove();
    if (curStep === 2) placeFocus(2);
    const from = net; net += it.v; settled++;
    tween(from, net, 800, (v) => ($('[data-net]').textContent = fmt(v)));
    $('[data-settled]').textContent = settled;
    showBanner('Une vente ! mepaye vous paye', `Vous venez de vendre pour ${xof(it.v)}`);
    if (!quiet) $('[data-sale-note]').textContent = `Vente réglée : +${xof(it.v)}, payée par ${who}.`;
  };
  $('[data-sim-sale]').addEventListener('click', () => simulateSale(false));

  // Retirer ses gains
  let dest = 'Wave', wBal = 670000, wOut = 185000, wBusy = false;
  const destLogos = { Wave: 'assets/logos/wave.webp', 'Orange Money': 'assets/logos/orange.svg', 'MTN MoMo': 'assets/logos/mtn-momo.webp' };
  $$('[data-dest] button').forEach((b, i, all) => {
    b.addEventListener('click', () => {
      dest = b.dataset.destV;
      all.forEach((x) => x.setAttribute('aria-checked', String(x === b)));
      $('[data-pop-logo]').src = destLogos[dest];
      $('[data-pop-wd]').textContent = `Retrait vers ${dest}`;
    });
    b.addEventListener('keydown', (e) => {
      if (!['ArrowRight', 'ArrowLeft'].includes(e.key)) return;
      const n = all[(i + (e.key === 'ArrowRight' ? 1 : all.length - 1)) % all.length]; n.focus(); n.click();
    });
  });
  $('[data-withdraw]').addEventListener('click', async () => {
    if (wBusy) return; wBusy = true;
    const wbtn = $('[data-wbtn]'), wt = $('[data-wbtn-t]'), note = $('[data-wd-note]');
    const amount = wBal || 670000;
    if (!wBal) { wBal = amount; $('[data-wbal]').textContent = fmt(wBal); }
    wbtn.classList.add('is-press'); await sleep(160); wbtn.classList.remove('is-press');
    wt.textContent = 'Retrait en cours…';
    await sleep(reduce ? 0 : 900);
    tween(wBal, 0, 900, (v) => ($('[data-wbal]').textContent = fmt(v)));
    const o = wOut; wOut += amount;
    tween(o, wOut, 900, (v) => ($('[data-wout]').textContent = fmt(v)));
    wBal = 0;
    wbtn.classList.add('is-done'); wt.textContent = `Envoyé sur ${dest}`;
    showBanner(`Retrait envoyé sur ${dest}`, `${xof(amount)} arrivent sur votre compte`);
    note.textContent = `${xof(amount)} envoyés vers ${dest}.`;
    await sleep(3200);
    wbtn.classList.remove('is-done'); wt.textContent = 'Retirer mes gains';
    wBal = 670000; $('[data-wbal]').textContent = fmt(wBal);
    wBusy = false;
  });

  /* =======================================================
     3. PAIEMENTS · checkout
     ======================================================= */
  const co = $('[data-checkout]');
  if (co) {
    const form = $('[data-co-form]', co), mm = $('[data-co-mm]', co), card = $('[data-co-card]', co);
    const done = $('[data-co-done]', co), payBtn = $('[data-co-pay]', co), toast = $('[data-co-toast]');
    // le nom de chaque moyen vient de sa tuile (data-name) : la liste se règle dans le HTML
    const names = {};
    $$('input[name="pm"]', co).forEach((r) => { names[r.value] = r.dataset.name; });
    const hint = (m) => (m === 'wave' ? 'Vous validerez le paiement dans l’application Wave.' : `Vous confirmerez le paiement sur votre téléphone ${names[m]}.`);
    let method = 'wave';
    $$('input[name="pm"]', co).forEach((r) => r.addEventListener('change', () => {
      method = r.value;
      const isCard = method === 'card';
      mm.hidden = isCard; card.hidden = !isCard;
      if (!isCard) { $('[data-co-mm-label]', co).textContent = `Numéro ${names[method]}`; $('[data-co-hint]', co).textContent = hint(method); }
    }));
    const tel = $('[data-co-tel]', co);
    tel.addEventListener('input', () => { tel.value = tel.value.replace(/\D/g, '').slice(0, 10).replace(/(\d{2})(?=\d)/g, '$1 '); });
    const cc = $('[data-co-cc]', co), brand = $('[data-co-brand]', co);
    cc.addEventListener('input', () => {
      const d = cc.value.replace(/\D/g, '').slice(0, 16);
      cc.value = d.replace(/(\d{4})(?=\d)/g, '$1 ');
      brand.src = /^(5[1-5]|2[2-7])/.test(d) ? 'assets/logos/pm/mastercard.webp' : 'assets/logos/pm/visa.webp';
    });
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (payBtn.classList.contains('is-busy')) return;
      payBtn.classList.add('is-busy'); payBtn.setAttribute('aria-busy', 'true');
      await sleep(reduce ? 300 : 1600);
      payBtn.classList.remove('is-busy'); payBtn.removeAttribute('aria-busy');
      form.hidden = true; done.hidden = false;
      co.closest('[data-co-wrap]').classList.add('is-paid');
      $('[data-co-done-s]', co).textContent = `14 900 XOF payés avec ${names[method]}. Votre reçu arrive par e-mail.`;
      $('[data-co-reset]', co).focus({ preventScroll: true });
      await sleep(reduce ? 0 : 600);
      toast.classList.add('is-on');
      setTimeout(() => toast.classList.remove('is-on'), 4200);
    });
    $('[data-co-reset]', co).addEventListener('click', () => { co.closest('[data-co-wrap]').classList.remove('is-paid'); done.hidden = true; form.hidden = false; toast.classList.remove('is-on'); payBtn.focus({ preventScroll: true }); });
  }

  /* =======================================================
     4. TARIFS · calculateur
     ======================================================= */
  const setFill = (r) => r.style.setProperty('--p', `${((r.value - r.min) / (r.max - r.min)) * 100}%`);
  const price = $('[data-price]'), qty = $('[data-qty]');
  const calc = () => {
    const pv = +price.value, qv = +qty.value, gross = pv * qv, fee = gross * .05;
    $('[data-out-price]').textContent = xof(pv);
    $('[data-out-qty]').textContent = fmt(qv);
    $('[data-r-gross]').textContent = xof(gross);
    $('[data-r-fee]').textContent = xof(fee);
    $('[data-r-net]').textContent = xof(gross - fee);
    setFill(price); setFill(qty);
  };
  [price, qty].forEach((r) => r.addEventListener('input', calc));
  calc();

  /* =======================================================
     5. STUDIO IA
     ======================================================= */
  const aiSec = $('[data-scene="ai"]');
  const studio = $('[data-studio]');
  if (aiSec && studio) {
    scene(aiSec, {
      progress: (s, y) => enterProgress(s, y, 1.1),
      render(q) {
        if (reduce) return;
        const t = ease(q);
        studio.style.transform = `translate3d(0, ${((1 - t) * 70).toFixed(1)}px, 0) rotateX(${((1 - t) * 24).toFixed(2)}deg) scale(${(.92 + t * .08).toFixed(4)})`;
      },
    });
    const topic = $('[data-ai-topic]'), go = $('[data-ai-go]'), outline = $('[data-outline]');
    const phases = $$('[data-phases] li'), text = $('[data-doc-text]'), title = $('[data-doc-title]'), kind = $('[data-doc-kind]');
    const status = $('[data-ai-status]'), skel = $('.doc__skel', studio);
    let format = 'ebook', run = 0;
    const plans = {
      ebook: [['Pourquoi ce sujet compte', '4 pages'], ['Les bases, sans jargon', '6 pages'], ['Passer à l’action, étape par étape', '9 pages'], ['Les erreurs qui coûtent cher', '5 pages'], ['Aller plus loin', '3 pages']],
      formation: [['Module 1 · Les fondations', '3 leçons · 18 min'], ['Module 2 · La méthode', '4 leçons · 26 min'], ['Module 3 · Passer à l’action', '4 leçons · 31 min'], ['Module 4 · Mesurer et améliorer', '2 leçons · 14 min']],
    };
    const para = (t, f) => (f === 'ebook'
      ? `Ce guide vous accompagne pas à pas sur un sujet précis : ${t.charAt(0).toLowerCase() + t.slice(1)}. Chaque chapitre part d’une situation concrète et se termine par une action simple, à faire tout de suite. À la fin, vous savez quoi faire, dans quel ordre, et pourquoi.`
      : `Cette formation transforme « ${t} » en parcours guidé. Chaque module combine une courte vidéo, une fiche pratique et un exercice. Vos élèves avancent à leur rythme et suivent leur progression, leçon après leçon.`);
    const generate = async () => {
      const id = ++run;
      const live = () => id === run;
      const t = topic.value.trim() || 'Votre idée';
      go.disabled = true;
      outline.innerHTML = ''; text.textContent = ''; skel.classList.remove('is-off');
      phases.forEach((p) => p.classList.remove('is-on'));
      title.textContent = t; kind.textContent = format === 'ebook' ? 'Ebook' : 'Formation';
      status.textContent = 'Génération du plan…';
      const plan = plans[format];
      phases[0].classList.add('is-on');
      for (let i = 0; i < plan.length; i++) {
        await sleep(reduce ? 0 : 260); if (!live()) return;
        const li = document.createElement('li');
        li.innerHTML = `<span>${String(i + 1).padStart(2, '0')}</span><span class="outline__t">${plan[i][0]}<small>${plan[i][1]}</small></span>`;
        if (i === 0) li.classList.add('is-cur');
        outline.appendChild(li);
        if (i === 1) phases[1].classList.add('is-on');
        if (i === 3) phases[2].classList.add('is-on');
      }
      phases[2].classList.add('is-on');
      status.textContent = 'Rédaction en cours…';
      phases[3].classList.add('is-on');
      await sleep(reduce ? 0 : 200); if (!live()) return;
      skel.classList.add('is-off');
      const full = para(t, format);
      if (reduce) text.textContent = full;
      else for (let i = 0; i < full.length; i += 2) { if (!live()) return; text.textContent = full.slice(0, i + 2); await sleep(14); }
      status.textContent = `Prêt à publier : ${plan.length} ${format === 'ebook' ? 'chapitres' : 'modules'}, modifiables à tout moment.`;
      go.disabled = false;
    };
    $('[data-ai-form]').addEventListener('submit', (e) => { e.preventDefault(); generate(); });
    $$('[data-ai-sugg] button').forEach((b) => b.addEventListener('click', () => { topic.value = b.textContent; generate(); }));
    $$('[data-format] button').forEach((b, i, all) => b.addEventListener('click', () => {
      format = b.dataset.f; all.forEach((x) => x.setAttribute('aria-checked', String(x === b))); generate();
    }));
    let started = false;
    watch(studio, (v) => { if (v && !started) { started = true; generate(); } }, .4);
  }

  /* =======================================================
     6. CATALOGUE · travelling horizontal, scènes qui se jouent
        quand la carte passe au centre (ou au survol)
     ======================================================= */
  const catSec = $('[data-scene="cat"]');
  const track = $('[data-cat-track]');
  const cards = $$('[data-pc]', track);
  const catBar = $('[data-cat-bar]');
  let dist = 0, cardPos = [];
  const catLead = $('[data-cat-lead]');
  if (catLead && !fine) catLead.textContent = 'Neuf formats, livrés automatiquement après le paiement.';
  const setPlay = (c, on) => { if (c._on !== on) { c._on = on; c.classList.toggle('is-playing', on); } };
  if (catSec && track) {
    scene(catSec, {
      progress: pinProgress,
      pre() {
        if (reduce) return;
        dist = Math.max(0, track.scrollWidth - vw);
        catSec.style.height = `${Math.round(dist + vh * 1.15)}px`;
        cardPos = cards.map((c) => c.offsetLeft + c.offsetWidth / 2);
      },
      render(p) {
        if (reduce) return;
        const x = -p * dist;
        track.style.transform = `translate3d(${x.toFixed(1)}px, 0, 0)`;
        catBar.style.transform = `scaleX(${p.toFixed(4)})`;
        // une seule scène à la fois : au survol (souris) ou la carte centrale (tactile)
        let best = -1, bestD = 1;
        cards.forEach((c, i) => {
          const d = clamp((cardPos[i] + x - vw / 2) / vw, -1, 1);
          // mise au point douce au centre, sans rotation ; l'objet glisse un peu par rapport à son arche
          c.style.transform = `scale(${(1 - Math.abs(d) * .045).toFixed(4)})`;
          c.style.setProperty('--px', d.toFixed(3));
          if (Math.abs(d) < bestD) { bestD = Math.abs(d); best = i; }
        });
        cards.forEach((c, i) => setPlay(c, fine ? !!c._hover : (i === best && bestD < .36)));
      },
    });
    // à l'arrivée sur la section, les cartes entrent l'une après l'autre
    cards.forEach((c, i) => c.style.setProperty('--i', i));
    watch(catSec, (v) => { if (v) catSec.classList.add('is-in'); }, .15);
    cards.forEach((c) => {
      c.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse' && !reduce) { c._hover = true; setPlay(c, true); } });
      c.addEventListener('pointerleave', () => { c._hover = false; if (fine) setPlay(c, false); });
    });
  }

  /* =======================================================
     7. OUTILS
     ======================================================= */
  // Analytics
  const an = $('[data-analytics]');
  if (an) {
    const W = 600, H = 220, P = 24;
    const line = $('[data-line]', an), area = $('[data-area]', an), plot = $('[data-plot]', an);
    const cx = $('[data-cx]', an), cpt = $('[data-cpt]', an), tip = $('[data-ctip]', an);
    const tabs = $$('[data-range]', an);
    const end = new Date(2026, 9, 17);
    const months = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'];
    const shape = (seed, trend) => Array.from({ length: P }, (_, i) => Math.max(.12, .35 + trend * (i / (P - 1)) + Math.sin(i * .9 + seed) * .09 + Math.sin(i * .37 + seed * 2) * .07));
    const mk = (days, total, sales, conv, seed, trend) => {
      const s = shape(seed, trend), sum = s.reduce((a, b) => a + b, 0);
      const vals = s.map((v) => (v / sum) * total);
      const labels = s.map((_, i) => {
        if (days === 365) { const m = (end.getMonth() - (P - 1 - i) / 2 + 24) % 12; return `${months[Math.floor(m)]}`; }
        const d = new Date(end); d.setDate(end.getDate() - Math.round((P - 1 - i) * (days / P)));
        return `${d.getDate()} ${months[d.getMonth()]}`;
      });
      return { vals, labels, total, sales, conv };
    };
    const data = { 7: mk(7, 212400, 31, '3,1 %', 1.2, .3), 30: mk(30, 900000, 124, '3,8 %', 2.6, .55), 90: mk(90, 2410000, 342, '4,2 %', 4.1, .5), 365: mk(365, 9860000, 1386, '4,0 %', 5.3, .6) };
    let range = 30, cur = Array(P).fill(0), max = 1;
    const pts = (v) => v.map((y, i) => [(i / (P - 1)) * W, H - (y / max) * H * .9]);
    const path = (p) => p.reduce((d, pt, i) => {
      if (!i) return `M${pt[0].toFixed(1)},${pt[1].toFixed(1)}`;
      const p0 = p[i - 2] || p[i - 1], p1 = p[i - 1], p3 = p[i + 1] || pt;
      return `${d} C${(p1[0] + (pt[0] - p0[0]) / 6).toFixed(1)},${(p1[1] + (pt[1] - p0[1]) / 6).toFixed(1)} ${(pt[0] - (p3[0] - p1[0]) / 6).toFixed(1)},${(pt[1] - (p3[1] - p1[1]) / 6).toFixed(1)} ${pt[0].toFixed(1)},${pt[1].toFixed(1)}`;
    }, '');
    const draw = () => { const d = path(pts(cur)); line.setAttribute('d', d); area.setAttribute('d', `${d} L${W},${H} L0,${H} Z`); };
    const select = (r) => {
      const prev = data[range]; range = r;
      const dset = data[r];
      max = Math.max(...dset.vals) * 1.05;
      const from = cur.slice();
      tween(0, 1, 800, (t) => { cur = from.map((f, i) => f + (dset.vals[i] - f) * t); draw(); });
      tween(prev === dset ? 0 : prev.total, dset.total, 800, (v) => ($('[data-ch-total]', an).textContent = fmt(v)));
      $('[data-k-sales]', an).textContent = fmt(dset.sales);
      $('[data-k-conv]', an).textContent = dset.conv;
      tabs.forEach((b) => { const on = +b.dataset.range === r; b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; });
    };
    tabs.forEach((b, i) => {
      b.addEventListener('click', () => select(+b.dataset.range));
      b.addEventListener('keydown', (e) => {
        if (!['ArrowRight', 'ArrowLeft'].includes(e.key)) return;
        const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length]; n.focus(); select(+n.dataset.range);
      });
    });
    let hoverI = P - 1;
    const showAt = (i) => {
      hoverI = i;
      const rect = plot.getBoundingClientRect();
      const [px, py] = pts(cur)[i];
      const x = (px / W) * rect.width, y = (py / H) * rect.height;
      cx.style.transform = `translateX(${x}px)`;
      cpt.style.transform = `translate(${x}px, ${y}px)`;
      const tw = tip.offsetWidth;
      tip.style.transform = `translate(${clamp(x - tw / 2, 0, rect.width - tw)}px, -100%)`;
      $('[data-ctip-v]', an).textContent = xof(data[range].vals[i]);
      $('[data-ctip-d]', an).textContent = data[range].labels[i];
      plot.classList.add('is-hover');
    };
    plot.addEventListener('pointermove', (e) => { const r = plot.getBoundingClientRect(); showAt(Math.round(clamp((e.clientX - r.left) / r.width) * (P - 1))); });
    plot.addEventListener('pointerleave', () => plot.classList.remove('is-hover'));
    plot.tabIndex = 0;
    plot.setAttribute('role', 'img');
    plot.setAttribute('aria-label', 'Courbe des ventes. Utilisez les flèches pour lire chaque point.');
    plot.addEventListener('focus', () => showAt(hoverI));
    plot.addEventListener('blur', () => plot.classList.remove('is-hover'));
    plot.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { e.preventDefault(); showAt(Math.min(P - 1, hoverI + 1)); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); showAt(Math.max(0, hoverI - 1)); }
    });
    let started = false, liveT = null;
    watch(an, (v) => {
      if (v && !started) { started = true; select(30); }
      if (v && !liveT && !reduce) liveT = setInterval(() => { const el = $('[data-live]', an); el.textContent = clamp(+el.textContent + Math.round((Math.random() - .45) * 3), 3, 14); }, 2400);
      if (!v) { clearInterval(liveT); liveT = null; }
    }, .3);
  }

  // Multi-boutiques
  const sw = $('[data-stores]');
  if (sw) {
    const btn = $('[data-sw-btn]', sw), list = $('[data-sw-list]', sw), opts = $$('[role="option"]', list), cardEl = $('[data-sw-card]', sw);
    const open = (o) => { btn.setAttribute('aria-expanded', String(o)); list.hidden = !o; if (o) (opts.find((x) => x.getAttribute('aria-selected') === 'true') || opts[0]).focus(); };
    const pick = (li) => {
      opts.forEach((x) => x.setAttribute('aria-selected', String(x === li)));
      const dot = $('[data-sw-dot]', sw);
      dot.style.setProperty('--c', li.dataset.c); dot.textContent = li.dataset.n.charAt(0);
      $('[data-sw-name]', sw).textContent = li.dataset.n;
      $('[data-sw-dom]', sw).textContent = li.dataset.d;
      $('[data-sw-v]', sw).textContent = li.dataset.v;
      $('[data-sw-cur]', sw).textContent = li.dataset.cur;
      cardEl.classList.remove('is-swap'); void cardEl.offsetWidth; cardEl.classList.add('is-swap');
      open(false); btn.focus();
    };
    btn.addEventListener('click', () => open(list.hidden));
    opts.forEach((li, i) => {
      li.addEventListener('click', () => pick(li));
      li.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(li); }
        if (e.key === 'ArrowDown') { e.preventDefault(); opts[(i + 1) % opts.length].focus(); }
        if (e.key === 'ArrowUp') { e.preventDefault(); opts[(i + opts.length - 1) % opts.length].focus(); }
        if (e.key === 'Escape') { open(false); btn.focus(); }
      });
    });
    document.addEventListener('click', (e) => { if (!sw.contains(e.target) && !list.hidden) open(false); });
  }

  // Affiliation
  const copyText = async (t) => {
    try { await navigator.clipboard.writeText(t); return true; } catch (_) {
      const ta = document.createElement('textarea'); ta.value = t; ta.style.cssText = 'position:fixed;opacity:0'; document.body.appendChild(ta); ta.select();
      let ok = false; try { ok = document.execCommand('copy'); } catch (__) {} ta.remove(); return ok;
    }
  };
  const flash = (b, ok, base, labelEl = b) => {
    labelEl.textContent = ok ? 'Copié' : 'Copie impossible';
    b.classList.toggle('is-done', ok);
    clearTimeout(b._t); b._t = setTimeout(() => { labelEl.textContent = base; b.classList.remove('is-done'); }, 1800);
  };
  const rate = $('[data-rate]');
  if (rate) {
    const upd = () => { const v = +rate.value; $('[data-rate-out]').textContent = `${v} %`; $('[data-rate-calc]').textContent = xof(14900 * v / 100); setFill(rate); };
    rate.addEventListener('input', upd); upd();
    const cb = $('[data-copy]'); cb.addEventListener('click', async () => flash(cb, await copyText(cb.dataset.copy), 'Copier'));
  }

  // Automatisations
  const log = $('[data-log]');
  if (log) {
    const now = () => new Date().toLocaleTimeString('fr-FR', { hour12: false });
    const addLog = (txt, tag) => {
      const li = document.createElement('li');
      li.innerHTML = `<time>${now()}</time><span>${txt}</span><em>${tag}</em>`;
      log.prepend(li);
      while (log.children.length > 8) log.lastElementChild.remove();
    };
    const tg = $$('[data-tgl]');
    tg.forEach((b) => b.addEventListener('click', () => {
      const on = b.getAttribute('aria-checked') !== 'true';
      b.setAttribute('aria-checked', String(on));
      addLog(`${b.dataset.tgl} ${on ? 'activé' : 'désactivé'}`, 'Réglages');
    }));
    const isOn = (n) => tg.find((b) => b.dataset.tgl === n).getAttribute('aria-checked') === 'true';
    const amounts = [14900, 4750, 23750, 2000, 9500];
    let k = 0, t = null;
    watch(log, (v) => {
      if (v && !t && !reduce) t = setInterval(() => {
        const a = amounts[k++ % amounts.length];
        if (isOn('Webhooks')) addLog(`Vente réglée · ${xof(a)}`, 'Webhooks');
        if (isOn('Tracking & pixels')) setTimeout(() => addLog('Conversion envoyée', 'Tracking'), 350);
        if (isOn('Automatisations')) setTimeout(() => addLog('Accès envoyé au client', 'Automatisations'), 700);
      }, 4200);
      if (!v) { clearInterval(t); t = null; }
    }, .3);
  }

  /* =======================================================
     8. API · trois étapes, le code à gauche, l'effet à droite
     ======================================================= */
  const devwin = $('[data-devwin]');
  if (devwin) {
    const stepsB = $$('[data-api-step]'), ind = $('[data-segs-ind]'), desc = $('[data-api-desc]');
    const codes = $$('[data-code]'), ltabs = $$('[data-lang]'), fileEl = $('[data-ide-file]');
    const pvs = $$('[data-pv]'), url = $('[data-pv-url]'), pay = $('[data-pv-pay]'), ok = $('[data-pv-ok]');
    const bal = $('[data-pv-bal]'), notif = $('[data-pv-notif]'), hook = $('[data-pv-hook]');
    const keyRow = $('.pv-key'), state = $('[data-ide-state]'), runB = $('[data-ide-run]');
    const texts = [
      'Dans le menu Développeur, en un clic. Gardez-la côté serveur, jamais dans le navigateur.',
      'Créez un paiement avec le montant, puis redirigez votre client vers la page de paiement mepaye.',
      'Le paiement arrive dans votre wallet, et votre site est prévenu automatiquement.',
    ];
    let apiStep = -1, running = false, played = false;
    const placeInd = () => { const b = stepsB[Math.max(0, apiStep)]; ind.style.width = `${b.offsetWidth}px`; ind.style.transform = `translateX(${b.offsetLeft - 4}px)`; };
    const resetPreview = (i) => {
      url.textContent = 'monsite.com/boutique';
      pay.classList.remove('is-on'); ok.classList.remove('is-on');
      if (i === 2) { bal.textContent = '684 900'; notif.classList.add('is-on'); hook.classList.add('is-on'); }
      else { bal.textContent = '670 000'; notif.classList.remove('is-on'); hook.classList.remove('is-on'); }
    };
    const setApi = (i, fromRun) => {
      if (i === apiStep) return;
      apiStep = i;
      stepsB.forEach((b, j) => { const on = j === i; b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; });
      placeInd();
      desc.classList.add('is-swap');
      setTimeout(() => { desc.textContent = texts[i]; desc.classList.remove('is-swap'); }, reduce ? 0 : 180);
      codes.forEach((c) => { c.classList.add('has-focus'); $$('.ln', c).forEach((l) => l.classList.toggle('is-hl', l.dataset.l === String(i))); });
      pvs.forEach((p, j) => p.classList.toggle('is-on', j === i));
      if (!fromRun) resetPreview(i);
    };
    stepsB.forEach((b, i) => {
      b.addEventListener('click', () => { if (!running) setApi(i); });
      b.addEventListener('keydown', (e) => {
        if (!['ArrowRight', 'ArrowLeft'].includes(e.key)) return;
        const n = stepsB[(i + (e.key === 'ArrowRight' ? 1 : stepsB.length - 1)) % stepsB.length]; n.focus(); n.click();
      });
    });
    const showLang = (t) => {
      ltabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; });
      codes.forEach((c) => (c.hidden = c.dataset.code !== t.dataset.lang));
      fileEl.textContent = t.dataset.file;
    };
    ltabs.forEach((t, i) => {
      t.addEventListener('click', () => showLang(t));
      t.addEventListener('keydown', (e) => {
        if (!['ArrowRight', 'ArrowLeft'].includes(e.key)) return;
        const n = ltabs[(i + (e.key === 'ArrowRight' ? 1 : ltabs.length - 1)) % ltabs.length]; n.focus(); n.click();
      });
    });
    setApi(0); showLang(ltabs[0]);
    addEventListener('resize', placeInd, { passive: true });
    if (document.fonts) document.fonts.ready.then(placeInd);

    const copyB = $('[data-ide-copy]');
    copyB.addEventListener('click', async () => {
      const okc = await copyText(codes.find((c) => !c.hidden).textContent);
      copyB.classList.toggle('is-done', okc);
      copyB.setAttribute('aria-label', okc ? 'Code copié' : 'Copie impossible');
      clearTimeout(copyB._t);
      copyB._t = setTimeout(() => { copyB.classList.remove('is-done'); copyB.setAttribute('aria-label', 'Copier le code'); }, 1800);
    });

    const press = async (el, ms = 200) => { el.classList.add('is-press'); await sleep(reduce ? 0 : ms); el.classList.remove('is-press'); };
    const w = (ms) => sleep(reduce ? 0 : ms);
    const run = async () => {
      if (running) return;
      running = true; runB.disabled = true; $('span', runB).textContent = 'Exécution…';
      state.textContent = 'Création de la clé'; state.className = 'dw__state is-run';
      setApi(0, true); resetPreview(0);
      await w(500); await press($('[data-pv-create]'));
      keyRow.classList.add('is-new'); await w(900); keyRow.classList.remove('is-new');
      state.textContent = 'Paiement créé, client redirigé';
      setApi(1, true); await w(900);
      await press($('[data-pv-buy]'), 240);
      url.textContent = 'pay.mepaye.com/c/chk_8F2kQ9'; pay.classList.add('is-on');
      await w(1100); await press($('[data-pv-paybtn]'), 240);
      ok.classList.add('is-on'); state.textContent = 'Paiement Wave confirmé';
      await w(1200);
      setApi(2, true); notif.classList.remove('is-on'); hook.classList.remove('is-on');
      await w(500);
      tween(670000, 684900, 900, (v) => (bal.textContent = fmt(v)));
      notif.classList.add('is-on'); await w(700); hook.classList.add('is-on');
      state.textContent = 'Paiement reçu · 14 900 XOF'; state.className = 'dw__state is-ok';
      runB.disabled = false; $('span', runB).textContent = 'Rejouer'; running = false;
    };
    runB.addEventListener('click', run);
    watch(devwin, (v) => { if (v && !played && !reduce) { played = true; setTimeout(run, 600); } }, .45);
  }

  /* =======================================================
     9. AVIS · le fil d'agenda défile en continu ; la carte au
        centre est nette, les autres s'estompent (comme une roue
        de sélection). Il ne s'arrête jamais seul, seulement avec le bouton pause.
     ======================================================= */
  const vx = $('[data-vx]');
  if (vx) {
    const vxTrack = $('[data-vx-track]', vx), vxList = $('.vx__list', vxTrack), vxPause = $('[data-vx-pause]', vx);
    if (!reduce) {
      const clone = vxList.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true'); clone.removeAttribute('aria-label');
      $$('img', clone).forEach((im) => (im.alt = ''));
      vxTrack.appendChild(clone);
      const days = $$('.vx__day', vxTrack);
      let loopH = 1, H = 1, pos = [], off = 0, speed = 0, paused = false, vis = false, vraf = 0, vlast = 0;
      const SPEED = 28; // px par seconde
      const vxMeasure = () => { H = vx.clientHeight; loopH = Math.max(1, clone.offsetTop - vxList.offsetTop); pos = days.map((d) => [d.offsetTop + d.offsetHeight / 2]); };
      const step = (now) => {
        const dt = Math.min(64, now - vlast) / 1000; vlast = now;
        speed += ((paused ? 0 : 1) - speed) * (1 - Math.pow(.03, dt));
        off = (off + speed * SPEED * dt) % loopH;
        vxTrack.style.transform = `translate3d(0, ${(-off).toFixed(2)}px, 0)`;
        const c = H / 2;
        days.forEach((d, i) => {
          const n = Math.min(1, Math.abs(pos[i] - off - c) / (H * .55));
          d.style.transform = `scale(${(1 - n * n * .08).toFixed(4)})`;
          d.style.opacity = (1 - n * n * .5).toFixed(3);
        });
        vraf = vis ? requestAnimationFrame(step) : 0;
      };
      const run = () => { if (vis && !vraf) { vlast = performance.now(); vraf = requestAnimationFrame(step); } };
      watch(vx, (v) => { vis = v; run(); }, 0);
      vxPause.addEventListener('click', () => {
        paused = !paused;
        vxPause.setAttribute('aria-pressed', String(paused));
        $('.sr-only', vxPause).textContent = paused ? 'Reprendre le défilement' : 'Mettre le défilement en pause';
      });
      vxMeasure();
      if ('ResizeObserver' in window) new ResizeObserver(vxMeasure).observe(vxList);
      addEventListener('resize', vxMeasure, { passive: true });
    }
  }

  /* =======================================================
     10. FIN · deux pièces, un m
     ======================================================= */
  const finalSec = $('[data-scene="final"]');
  if (finalSec) {
    let lit = false, talkSeen = false, talkPhase = true;
    const finalSign = $('.final__sign', finalSec) || finalSec;
    // les deux personnes ne se parlent que lorsqu'elles sont à l'écran
    const setTalk = () => finalSec.classList.toggle('is-talk', !reduce && talkSeen && talkPhase);
    watch(finalSec, (v) => { talkSeen = v; setTalk(); }, 0);
    scene(finalSec, {
      // calé sur le logo lui-même : il parle en entrant par le bas, prend son volume au tiers haut de l'écran
      post() { const mk = $('.final__mark', finalSec); this.mt = mk.getBoundingClientRect().top + scrollY + mk.offsetHeight * .35; },
      progress: (s, y) => clamp((y + vh * .85 - s.mt) / (vh * .5)),
      render(m) {
        const t = reduce ? 1 : m;
        const st = finalSign.style; // sur le dessin seul : la section entière n'a pas à être recalculée
        st.setProperty('--m', easeOut(clamp(t / .48)).toFixed(4));
        st.setProperty('--talk', (1 - clamp((t - .32) / .14)).toFixed(3));
        st.setProperty('--h', ease(clamp((t - .48) / .18)).toFixed(4));
        st.setProperty('--x', ease(clamp((t - .64) / .24)).toFixed(4));
        const tp = t < .46;
        if (tp !== talkPhase) { talkPhase = tp; setTalk(); }
        const on = t > .96;
        if (on && !lit && !reduce) { lit = true; finalSec.classList.add('is-lit'); }
        else if (t < .4 && lit) { lit = false; finalSec.classList.remove('is-lit'); }
      },
    });
  }

  /* =======================================================
     Mesures : au chargement, au redimensionnement, aux polices
     ======================================================= */
  let rT = 0;
  const remeasure = () => { cancelAnimationFrame(rT); rT = requestAnimationFrame(measure); };
  addEventListener('resize', remeasure, { passive: true });
  addEventListener('load', remeasure);
  if (document.fonts) document.fonts.ready.then(remeasure);
  if ('ResizeObserver' in window) {
    let lastH = 0;
    new ResizeObserver(() => { const h = document.body.scrollHeight; if (Math.abs(h - lastH) > 4) { lastH = h; remeasure(); } }).observe(document.body);
  }
  measure();
  scenes.forEach((s) => { s.cur = s.tgt; s.render(s.cur); s.prev = s.cur; });
})();

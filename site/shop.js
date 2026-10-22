/* =========================================================
   mepaye · vitrine, page produit et paiement · JS natif
   Démonstration : rien n'est envoyé à un serveur.
   ========================================================= */
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const nf = new Intl.NumberFormat('fr-FR');
  const fmt = (n) => nf.format(n).replace(/[  ]/g, ' ');
  const store = {
    get(k) { try { return JSON.parse(sessionStorage.getItem(k)); } catch (e) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* stockage indisponible */ } },
  };

  /* La boutique créée à l'inscription s'affiche en aperçu */
  const mine = store.get('mp_shop');
  if (mine && mine.name) {
    const body = document.body;
    if (mine.color) body.style.setProperty('--c', mine.color);
    $$('[data-shop-name]').forEach((el) => { el.textContent = mine.name; });
    $$('[data-shop-init]').forEach((el) => { el.textContent = mine.name[0].toUpperCase(); });
    const pv = $('[data-shop-preview]');
    if (pv) pv.hidden = false;
  }

  /* Vitrine : filtre par type. Filtrée, la grille repasse en cartes simples. */
  const chips = $$('[data-f]');
  if (chips.length) {
    const cards = $$('[data-grid] [data-type]'), none = $('[data-none]');
    const wide = cards.map((k) => [...k.classList].find((c) => c.startsWith('sx-c--')));
    chips.forEach((c) => c.addEventListener('click', () => {
      chips.forEach((d) => d.setAttribute('aria-pressed', String(d === c)));
      const f = c.dataset.f;
      cards.forEach((k, i) => {
        k.hidden = f !== 'all' && k.dataset.type !== f;
        if (wide[i]) k.classList.toggle(wide[i], f === 'all');
        if (!k.hidden && !reduce) k.animate([{ opacity: 0, transform: 'translateY(8px)' }, { opacity: 1, transform: 'none' }], { duration: 420, delay: 30 * i, easing: 'cubic-bezier(.22,1,.36,1)', fill: 'backwards' });
      });
      none.hidden = cards.some((k) => !k.hidden);
    }));
  }

  /* Page produit : galerie à trois vues, au clic et aux flèches */
  const gal = $('[data-gallery]');
  if (gal) {
    const tabs = $$('[role="tab"]', gal);
    const pick = (t, focus) => {
      tabs.forEach((u) => {
        const on = u === t;
        u.setAttribute('aria-selected', String(on));
        u.tabIndex = on ? 0 : -1;
        document.getElementById(u.getAttribute('aria-controls')).hidden = !on;
      });
      if (focus) t.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => pick(t));
      t.addEventListener('keydown', (e) => {
        const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); }
      });
    });
  }

  /* Le produit choisi suit jusqu'au paiement */
  $$('[data-buy]').forEach((a) => a.addEventListener('click', () => {
    store.set('mp_cart', { name: a.dataset.name, type: a.dataset.type, price: +a.dataset.price, cover: a.dataset.cover || '' });
  }));
  const bar = $('[data-pp-bar]'), buyBox = $('.pb');
  if (bar && buyBox) {
    new IntersectionObserver(([e]) => {
      const show = !e.isIntersecting && e.boundingClientRect.top < 0;
      bar.classList.toggle('is-on', show);
      bar.setAttribute('aria-hidden', String(!show));
      $('a', bar).tabIndex = show ? 0 : -1;
    }).observe(buyBox);
  }

  /* pay.mepaye.com */
  const main = $('.ck2-main');
  if (!main) return;
  const cart = store.get('mp_cart');
  if (cart && cart.name) {
    $$('[data-ck-name]').forEach((el) => { el.textContent = cart.name; });
    $$('[data-ck-type]').forEach((el) => { el.textContent = cart.type; });
    $$('[data-ck-price]').forEach((el) => { el.textContent = fmt(cart.price); });
    const kind = { Formation: 'formation', Template: 'template', Ebook: 'ebook' }[cart.type] || 'formation';
    // la miniature du produit choisi si elle existe, sinon l'illustration de son type
    const img = $('[data-ck-cv="img"]');
    if (cart.cover && img) img.innerHTML = '<span class="cv cv--img" aria-hidden="true"><img src="' + cart.cover + '" alt="" width="900" height="900"></span>';
    const which = cart.cover && img ? 'img' : kind;
    $$('[data-ck-cv]').forEach((el) => { el.hidden = el.dataset.ckCv !== which; });
  }
  if (mine && mine.name) {
    $$('[data-ck-shop]').forEach((el) => { el.textContent = mine.name; });
    $$('[data-ck-init]').forEach((el) => { el.textContent = mine.name[0].toUpperCase(); });
  }

  const form = $('[data-ck-form]');
  const steps = $$('[data-ck-steps] li');
  const STEP = { '': 0, wait: 1, ok: 2, ko: 1 };
  const show = (name) => {
    form.hidden = !!name;
    main.classList.toggle('is-state', !!name);
    $$('[data-ck-state]').forEach((s) => { s.hidden = s.dataset.ckState !== name; });
    const at = STEP[name];
    steps.forEach((li, i) => {
      li.classList.toggle('is-done', i < at || (name === 'ok' && i === at));
      if (i === at && name !== 'ok') li.setAttribute('aria-current', 'step'); else li.removeAttribute('aria-current');
    });
    if (name) {
      const s = $(`[data-ck-state="${name}"]`);
      s.focus({ preventScroll: true });
      main.scrollIntoView({ block: 'nearest', behavior: reduce ? 'auto' : 'smooth' });
    } else { const f = $('input, button', form); if (f) f.focus(); }
  };
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  const receipt = (method) => {
    const n = () => Math.random().toString(36).slice(2, 6).toUpperCase();
    $('[data-rc-ref]').textContent = `MP-${n()}-${n()}`;
    $('[data-rc-date]').textContent = new Intl.DateTimeFormat('fr-FR', { day: 'numeric', month: 'long', hour: '2-digit', minute: '2-digit' }).format(new Date());
    $('[data-rc-m]').textContent = method;
  };
  $('[data-ck-retry]').addEventListener('click', () => show(''));

  /* mode test : deux simulations, comme la vraie page de test */
  $$('[data-ck-sim]').forEach((b) => b.addEventListener('click', async () => {
    $$('[data-ck-sim]').forEach((x) => { x.disabled = true; });
    b.classList.add('is-busy');
    await wait(reduce ? 0 : 700);
    $$('[data-ck-sim]').forEach((x) => { x.disabled = false; });
    b.classList.remove('is-busy');
    if (b.dataset.ckSim === 'ok') receipt('Simulation de test');
    show(b.dataset.ckSim);
  }));

  if (form.tagName === 'FORM') {
    const err = $('[data-ck-err]', form);
    $$('input', form).forEach((f) => f.addEventListener('input', () => f.removeAttribute('aria-invalid')));
    const tel = form.elements.tel;
    const hint = $('[data-ck-telhint]', form);
    const dial = $('[data-ck-dial]', form);
    const syncDial = () => { dial.textContent = form.elements.pays.selectedOptions[0].dataset.dial; };
    form.elements.pays.addEventListener('change', syncDial);
    syncDial();
    const syncTel = () => {
      const card = form.elements.moyen.value === 'carte';
      hint.textContent = card ? 'Pour vous joindre en cas de besoin.' : 'Le numéro de votre compte Mobile Money.';
    };
    $$('[name="moyen"]', form).forEach((r) => r.addEventListener('change', syncTel));
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const bad = [];
      if (!form.elements.nom.value.trim()) bad.push([form.elements.nom, 'votre nom']);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(form.elements.email.value.trim())) bad.push([form.elements.email, 'une adresse e-mail valide']);
      if (tel.value.replace(/\D/g, '').length < 8) bad.push([tel, 'un numéro de téléphone complet']);
      bad.forEach(([f]) => f.setAttribute('aria-invalid', 'true'));
      if (bad.length) { err.hidden = false; err.textContent = `Indiquez ${bad.map((b) => b[1]).join(', ')}.`; bad[0][0].focus(); return; }
      err.hidden = true;
      const m = $('[name="moyen"]:checked', form);
      const label = m.dataset.label;
      const number = `${dial.textContent} ${tel.value.trim()}`.replace(/\s+/g, '\u00a0');
      $('[data-ck-wait]').textContent = m.dataset.kind === 'card'
        ? 'Validation de votre carte auprès de votre banque.'
        : `Une demande ${label} a été envoyée au ${number}. Validez-la avec votre code secret.`;
      $('[data-ck-okmsg]').textContent = `Votre accès vous attend. La confirmation part à ${form.elements.email.value.trim()}.`;
      receipt(m.dataset.kind === 'card' ? label : `${label} · ${number}`);
      const ms = reduce ? 400 : 3200;
      main.style.setProperty('--ck-wait', `${ms}ms`);
      show('wait');
      await wait(ms);
      show('ok');
    });
  }
})();

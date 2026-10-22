/* =========================================================
   mepaye · écrans de compte · JS natif, sans dépendance
   Démonstration du parcours : rien n'est envoyé à un serveur.
   ========================================================= */
(() => {
  'use strict';

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const wait = (ms) => new Promise((r) => setTimeout(r, reduce ? 0 : ms));
  const isEmail = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim());

  /* ---------- le portail : arches concentriques calées sur la carte ---------- */
  const portal = $('.portal'), door = $('.card-a');
  if (portal && door) {
    const BAND = 12, RINGS = [BAND + 56, BAND + 150, BAND + 270];
    let raf = 0;
    const draw = () => {
      raf = 0;
      // géométrie de mise en page, sans les transformations des animations d'arrivée
      const W = Math.round(portal.clientWidth || portal.getBoundingClientRect().width), H = Math.round(portal.clientHeight || portal.getBoundingClientRect().height);
      const cw = door.offsetWidth, cx = door.offsetLeft + cw / 2, top = door.offsetTop, base = H + 4;
      const arch = (d) => { const r = cw / 2 + d, y = top - d + r; return `M${(cx - r).toFixed(1)} ${base}V${y.toFixed(1)}A${r} ${r} 0 0 1 ${(cx + r).toFixed(1)} ${y.toFixed(1)}V${base}`; };
      portal.setAttribute('viewBox', `0 0 ${W} ${H}`);
      portal.innerHTML = `<path class="portal__band" d="${arch(BAND)}Z"/>`
        + RINGS.map((d) => `<path class="portal__line" d="${arch(d)}"/>`).join('')
        + `<path class="portal__run" pathLength="100" d="${arch(RINGS[0])}"/><path class="portal__run portal__run--b" pathLength="100" d="${arch(RINGS[1])}"/>`
        + `<path class="portal__done" pathLength="100" d="${arch(BAND)}"/>`;
    };
    const ask = () => { if (!raf) raf = requestAnimationFrame(draw); };
    new ResizeObserver(ask).observe(door);
    addEventListener('resize', ask);
    addEventListener('load', ask);
    if (document.fonts) document.fonts.ready.then(ask);
    draw();
  }

  /* ---------- champs : erreurs accessibles ---------- */
  const setErr = (input, msg) => {
    const f = input.closest('.fi-a') || input.closest('.check');
    if (!f) return;
    f.classList.toggle('is-bad', !!msg);
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    const inCheck = f.classList.contains('check');
    let e = inCheck ? $('.f__err', f) : (f.nextElementSibling?.classList.contains('f__err') ? f.nextElementSibling : null);
    if (msg) {
      if (!e) { e = document.createElement('p'); e.className = 'f__err'; e.id = `${input.id}-err`; inCheck ? f.appendChild(e) : f.after(e); }
      e.textContent = msg;
      input.setAttribute('aria-describedby', [input.getAttribute('aria-describedby'), e.id].filter(Boolean).join(' ').trim());
    } else if (e) e.remove();
  };
  $$('.fi-a input, .check input').forEach((i) => i.addEventListener('input', () => setErr(i, '')));

  /* afficher ou masquer le mot de passe */
  $$('[data-eye]').forEach((b) => b.addEventListener('click', () => {
    const i = $(`#${b.getAttribute('aria-controls')}`);
    const show = i.type === 'password';
    i.type = show ? 'text' : 'password';
    b.setAttribute('aria-label', show ? 'Masquer le mot de passe' : 'Afficher le mot de passe');
    b.setAttribute('aria-pressed', String(show));
  }));

  /* règles du mot de passe, vérifiées en direct */
  const rules = { len: (v) => v.length >= 8, up: (v) => /[A-ZÀ-Ý]/.test(v), num: (v) => /\d/.test(v) };
  const pw = $('[data-pw]');
  if (pw) {
    const upd = () => $$('[data-rule]').forEach((li) => li.classList.toggle('is-ok', rules[li.dataset.rule](pw.value)));
    pw.addEventListener('input', upd); upd();
  }

  /* bouton en cours de traitement */
  const loading = async (btn, ms = 900) => {
    const t = $('.btn__t', btn); const old = t ? t.textContent : '';
    btn.classList.add('is-load'); btn.setAttribute('aria-busy', 'true');
    if (t && btn.dataset.loading) t.textContent = btn.dataset.loading;
    await wait(ms);
    btn.classList.remove('is-load'); btn.removeAttribute('aria-busy');
    if (t) t.textContent = old;
  };

  /* ---------- inscription : quatre étapes ---------- */
  const wiz = $('[data-wizard]');
  if (wiz) {
    const steps = $$('[data-step]', wiz);
    let cur = 0;
    const go = (i) => {
      steps.forEach((s, j) => { s.hidden = j !== i; });
      cur = i;
      const h = $('h1', steps[i]); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    };

    /* étape 1 : le compte */
    const validAccount = () => {
      let ok = true;
      const fn = $('#prenom'), ln = $('#nom'), em = $('#email'), p1 = $('#mdp'), p2 = $('#mdp2'), cgu = $('#cgu');
      if (!fn.value.trim()) { setErr(fn, 'Indiquez votre prénom.'); ok = false; }
      if (!ln.value.trim()) { setErr(ln, 'Indiquez votre nom.'); ok = false; }
      if (!isEmail(em.value)) { setErr(em, 'Adresse e-mail invalide.'); ok = false; }
      if (!Object.values(rules).every((r) => r(p1.value))) { setErr(p1, 'Respectez les trois règles ci-dessous.'); ok = false; }
      if (p2.value !== p1.value || !p2.value) { setErr(p2, 'Les mots de passe diffèrent.'); ok = false; }
      if (!cgu.checked) { setErr(cgu, 'Acceptez les CGU pour continuer.'); ok = false; }
      if (!ok) { const first = $('[aria-invalid="true"]', steps[0]); if (first) first.focus(); }
      return ok;
    };
    $('[data-form-account]').addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!validAccount()) return;
      $('[data-sent-to]').textContent = $('#email').value.trim();
      await loading(e.submitter || $('button[type="submit"]', e.target), 700);
      go(1); startResend(); $('.code input').focus();
    });

    /* étape 2 : le code reçu par e-mail */
    const code = $$('.code input');
    const codeOk = () => code.every((c) => /^\d$/.test(c.value));
    code.forEach((c, i) => {
      c.addEventListener('input', () => {
        c.value = c.value.replace(/\D/g, '').slice(-1);
        if (c.value && code[i + 1]) code[i + 1].focus();
        $('.code').classList.toggle('is-ok', codeOk());
        $('[data-code-err]').hidden = true;
      });
      c.addEventListener('keydown', (e) => {
        if (e.key === 'Backspace' && !c.value && code[i - 1]) code[i - 1].focus();
        if (e.key === 'ArrowLeft' && code[i - 1]) code[i - 1].focus();
        if (e.key === 'ArrowRight' && code[i + 1]) code[i + 1].focus();
      });
      c.addEventListener('paste', (e) => {
        const d = (e.clipboardData.getData('text') || '').replace(/\D/g, '').slice(0, 6);
        if (!d) return; e.preventDefault();
        d.split('').forEach((ch, k) => { if (code[k]) code[k].value = ch; });
        (code[d.length] || code[5]).focus();
        $('.code').classList.toggle('is-ok', codeOk());
      });
    });
    let timer = 0;
    const startResend = () => {
      const b = $('[data-resend]'); let n = 30;
      b.disabled = true; clearInterval(timer);
      const tick = () => { b.textContent = n > 0 ? `Renvoyer le code (${n} s)` : 'Renvoyer le code'; if (n-- <= 0) { b.disabled = false; clearInterval(timer); } };
      tick(); timer = setInterval(tick, 1000);
    };
    $('[data-resend]').addEventListener('click', () => { startResend(); $('[data-resent]').hidden = false; });
    $('[data-form-code]').addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!codeOk()) { $('[data-code-err]').hidden = false; (code.find((c) => !c.value) || code[0]).focus(); return; }
      await loading(e.submitter || $('button[type="submit"]', e.target), 700);
      go(2); $('#boutique').focus();
    });

    /* étape 3 : la boutique, l'aperçu se construit */
    const slug = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 30);
    const name = $('#boutique'), user = $('#adresse'), avail = $('[data-avail]');
    let userTouched = false;
    const RESERVED = ['mepaye', 'admin', 'aide', 'blog', 'api', 'app', 'www'];
    const paintShop = () => {
      const n = name.value.trim() || 'Votre boutique';
      const u = user.value || 'votre-boutique';
      $$('[data-shop-name]').forEach((el) => (el.textContent = n));
      $$('[data-shop-url]').forEach((el) => (el.textContent = u));
      $$('[data-shop-av]').forEach((el) => (el.textContent = (n[0] || 'V').toUpperCase()));
      if (!user.value) { avail.textContent = 'Lettres minuscules, chiffres et tirets.'; avail.className = 'hint-a'; return; }
      const taken = RESERVED.includes(user.value) || user.value.length < 3;
      avail.textContent = user.value.length < 3 ? 'Au moins 3 caractères.' : taken ? 'Cette adresse est déjà prise.' : 'Cette adresse est disponible.';
      avail.className = `hint-a ${taken ? 'is-ko' : 'is-ok'}`;
    };
    name.addEventListener('input', () => { if (!userTouched) user.value = slug(name.value); paintShop(); });
    user.addEventListener('input', () => { userTouched = true; user.value = slug(user.value); paintShop(); });
    $('[data-form-shop]').addEventListener('submit', async (e) => {
      e.preventDefault();
      let ok = true;
      if (!name.value.trim()) { setErr(name, 'Donnez un nom à votre boutique.'); ok = false; }
      if (user.value.length < 3 || RESERVED.includes(user.value)) { setErr(user, 'Adresse indisponible ou trop courte.'); ok = false; }
      if (!ok) { $('[aria-invalid="true"]', steps[2]).focus(); return; }
      await loading(e.submitter || $('button[type="submit"]', e.target), 600);
      go(3);
    });

    /* étape 4 : le style */
    const minis = $$('[data-shop], [data-shop-style]');
    $$('[name="theme"]').forEach((r) => r.addEventListener('change', () => minis.forEach((m) => m.style.setProperty('--c', r.value))));
    $('#sombre').addEventListener('change', (e) => minis.forEach((m) => m.classList.toggle('is-dark', e.target.checked)));
    $('[data-form-style]').addEventListener('submit', async (e) => {
      e.preventDefault();
      /* la boutique créée s'ouvre ensuite en aperçu dans la vitrine */
      try {
        sessionStorage.setItem('mp_shop', JSON.stringify({ name: name.value.trim(), slug: user.value, color: ($('[name="theme"]:checked') || {}).value || '#0866FF' }));
      } catch (err) { /* stockage indisponible */ }
      await loading(e.submitter || $('button[type="submit"]', e.target), 1100);
      go(4);
    });

    $$('[data-back]').forEach((b) => b.addEventListener('click', () => go(Math.max(0, cur - 1))));
    paintShop();
  }

  /* ---------- connexion ---------- */
  const login = $('[data-form-login]');
  if (login) {
    login.addEventListener('submit', async (e) => {
      e.preventDefault();
      const em = $('#email'), p = $('#mdp');
      let ok = true;
      if (!isEmail(em.value)) { setErr(em, 'Adresse e-mail invalide.'); ok = false; }
      if (!p.value) { setErr(p, 'Saisissez votre mot de passe.'); ok = false; }
      if (!ok) { $('[aria-invalid="true"]', login).focus(); return; }
      await loading($('button[type="submit"]', login), 900);
      welcome(em.value);
    });
  }

  /* ---------- connexion réussie : la porte s'ouvre ----------
     L'arche est une porte. Après la connexion :
     1. le formulaire s'efface ; une arche marine se pose, la coche s'y dessine, on salue la personne ;
     2. un trait de lumière fait le tour de la porte, comme une jauge ;
     3. la porte s'ouvre en deux battants, la lumière de l'espace jaillit ;
     4. on avance à travers la porte et l'on arrive dans son espace.
     Pas de redirection pour l'instant : l'espace n'est pas encore dessiné. */
  const EIN = 'cubic-bezier(.4, 0, 1, 1)', EOUT = 'cubic-bezier(.22, 1, .36, 1)', SPRING = 'cubic-bezier(.34, 1.45, .64, 1)';
  const anim = (el, kf, o) => el.animate(kf, { fill: 'both', ...o }).finished;

  function welcome(email) {
    const page = $('.authp'), card = $('.card-a'), wel = $('[data-welcome]');
    if (!page || !card || !wel) return;
    const local = (email.split('@')[0] || '').split(/[._\-+0-9]+/).filter(Boolean)[0] || '';
    const name = local ? local[0].toUpperCase() + local.slice(1).toLowerCase() : '';
    $('[data-wel-name]', wel).textContent = name || 'vous';
    if (reduce) { arrive(page, name); return; }

    const out = [...card.children].filter((c) => c !== wel);
    const parts = [$('.wel__mark', wel), $('.wel__k', wel), $('.wel__t', wel), $('.wel__s', wel)];
    Promise.all(out.map((c, i) => anim(c,
      [{ opacity: 1, transform: 'none', filter: 'blur(0)' }, { opacity: 0, transform: 'translateY(-12px)', filter: 'blur(6px)' }],
      { duration: 380, delay: i * 45, easing: EIN }))).then(async () => {
      out.forEach((c) => { c.hidden = true; });
      card.classList.add('is-welcome');
      wel.hidden = false;
      $('.wel__t', wel).focus({ preventScroll: true });
      anim(parts[0], [{ opacity: 0, transform: 'translateY(14px) scale(.6)' }, { opacity: 1, transform: 'none' }], { duration: 760, easing: SPRING });
      parts.slice(1).forEach((p, i) => anim(p,
        [{ opacity: 0, transform: 'translateY(10px)', filter: 'blur(4px)' }, { opacity: 1, transform: 'none', filter: 'blur(0)' }],
        { duration: 620, delay: 260 + i * 90, easing: EOUT }));
      requestAnimationFrame(() => page.classList.add('is-in'));
      await new Promise((r) => setTimeout(r, 2050));
      await Promise.all(parts.map((p, i) => anim(p,
        [{ opacity: 1, transform: 'none', filter: 'blur(0)' }, { opacity: 0, transform: 'scale(.96)', filter: 'blur(4px)' }],
        { duration: 300, delay: i * 30, easing: EIN })));
      openDoor(page, card, name);
    });
  }

  /* la porte : deux battants posés exactement sur l'arche, la lumière derrière */
  async function openDoor(page, card, name) {
    const r = card.getBoundingClientRect(), pr = page.getBoundingClientRect();
    const door = document.createElement('div');
    door.className = 'door';
    door.setAttribute('aria-hidden', 'true');
    Object.assign(door.style, { left: `${r.left - pr.left}px`, top: `${r.top - pr.top}px`, width: `${r.width}px`, height: `${r.height}px` });
    door.style.setProperty('--hw', `${r.width / 2}px`);
    door.innerHTML = '<span class="door__in"></span><span class="door__leaf door__leaf--l"><i></i></span><span class="door__leaf door__leaf--r"><i></i></span>';
    page.appendChild(door);
    card.style.visibility = 'hidden';
    page.classList.add('is-through');
    document.documentElement.style.overflow = 'hidden'; // la scène grandit : aucune barre de défilement ne doit apparaître
    const [inner, left, right] = door.children;

    // les battants pivotent, la lumière monte
    const SWING = 'cubic-bezier(.62, .02, .28, 1)';
    anim(left, [{ transform: 'rotateY(0deg)' }, { transform: 'rotateY(-106deg)' }], { duration: 1250, easing: SWING });
    anim(right, [{ transform: 'rotateY(0deg)' }, { transform: 'rotateY(106deg)' }], { duration: 1250, easing: SWING });
    $$('.door__leaf i', door).forEach((sh) => anim(sh, [{ opacity: 0 }, { opacity: .55 }], { duration: 1250, easing: SWING }));
    anim(inner, [{ opacity: 0, filter: 'brightness(.7)' }, { opacity: 1, filter: 'brightness(1)' }], { duration: 900, easing: EOUT });

    // on avance à travers la porte : la scène grandit autour du seuil
    await new Promise((res) => setTimeout(res, 520));
    const ox = r.left - pr.left + r.width / 2, oy = r.top - pr.top + Math.min(r.height * .42, r.width * .62);
    page.style.transformOrigin = `${ox}px ${oy}px`;
    await anim(page, [{ transform: 'scale(1)' }, { transform: 'scale(7)' }], { duration: 1450, easing: 'cubic-bezier(.66, 0, .82, .32)' });
    arrive(page, name);
  }

  /* l'espace : un seuil lumineux, la salutation, et la promesse du tableau de bord */
  function arrive(page, name) {
    const sp = document.createElement('section');
    sp.className = 'space';
    sp.setAttribute('aria-labelledby', 'space-t');
    sp.innerHTML = `<div class="space__in">
        <p class="space__k">Votre espace</p>
        <h1 class="space__t" id="space-t" tabindex="-1">Bienvenue${name ? `, <span></span>` : ''}.</h1>
        <p class="space__s">Votre tableau de bord arrive très bientôt.</p>
        <div class="space__cards" aria-hidden="true">
          <span class="space__c"><small>Solde disponible</small><b></b><i></i></span>
          <span class="space__c"><small>Ventes du mois</small><b></b><i></i></span>
          <span class="space__c"><small>Produits</small><b></b><i></i></span>
        </div>
        <a class="space__back" href="/">Retour au site</a>
      </div>`;
    if (name) $('.space__t span', sp).textContent = name;
    document.body.appendChild(sp);
    document.documentElement.style.overflow = 'hidden';
    const t = $('.space__t', sp);
    if (reduce) { page.style.visibility = 'hidden'; t.focus({ preventScroll: true }); return; }
    anim(sp, [{ opacity: 0 }, { opacity: 1 }], { duration: 520, easing: EOUT }).then(() => { page.style.visibility = 'hidden'; });
    [...$('.space__in', sp).children].forEach((el, i) => anim(el,
      [{ opacity: 0, transform: 'translateY(16px)', filter: 'blur(6px)' }, { opacity: 1, transform: 'none', filter: 'blur(0)' }],
      { duration: 760, delay: 180 + i * 90, easing: EOUT }));
    t.focus({ preventScroll: true });
  }

  /* ---------- lien de connexion, et mot de passe oublié ---------- */
  $$('[data-form-link]').forEach((form) => {
    const views = $$('[data-view]');
    const show = (v) => { views.forEach((x) => { x.hidden = x.dataset.view !== v; }); const h = $(`[data-view="${v}"] h1`); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); } };
    let timer = 0;
    const startResend = () => {
      const b = $('[data-resend]'); let n = 30;
      b.disabled = true; clearInterval(timer);
      const tick = () => { b.textContent = n > 0 ? `Renvoyer l’e-mail (${n} s)` : 'Renvoyer l’e-mail'; if (n-- <= 0) { b.disabled = false; clearInterval(timer); } };
      tick(); timer = setInterval(tick, 1000);
    };
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const em = $('#email', form);
      if (!isEmail(em.value)) { setErr(em, 'Adresse e-mail invalide.'); em.focus(); return; }
      await loading($('button[type="submit"]', form), 900);
      $$('[data-sent-to]').forEach((el) => (el.textContent = em.value.trim()));
      show('sent'); startResend();
    });
    $('[data-resend]')?.addEventListener('click', () => { startResend(); $('[data-resent]').hidden = false; });
    $('[data-change]')?.addEventListener('click', () => { show('ask'); $('#email', form).focus(); });
  });

  /* le lien « Recevoir un lien par e-mail » transmet l'adresse déjà saisie */
  /* (par le stockage de session, jamais dans l'adresse de la page) */
  const toLink = $('[data-to-link]');
  if (toLink) toLink.addEventListener('click', () => {
    const v = $('#email')?.value.trim();
    try { if (v) sessionStorage.setItem('mp_email', v); } catch (_) { /* stockage indisponible : on saisira l'adresse à nouveau */ }
  });
  if ($('[data-form-link]')) {
    try { const v = sessionStorage.getItem('mp_email'); const em = $('#email'); if (v && em && !em.value) em.value = v; sessionStorage.removeItem('mp_email'); } catch (_) { /* rien */ }
  }
})();

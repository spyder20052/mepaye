/* =========================================================
   mepaye · pages publiques · JS natif, sans dépendance
   Barre de navigation, menu mobile, apparitions, et les petites
   interactions propres à chaque page (calculateur, recherche,
   filtres, sommaire).
   ========================================================= */
(() => {
  'use strict';

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const nf = new Intl.NumberFormat('fr-FR');
  const fmt = (n) => nf.format(Math.round(n)).replace(/[  ]/g, ' ');
  const xof = (n) => `${fmt(n)} XOF`;

  /* Barre : elle s'efface quand on descend, revient quand on remonte */
  let lastY = scrollY, acc = 0, ticking = false;
  const onScroll = () => {
    ticking = false;
    const y = scrollY, dy = y - lastY; lastY = y;
    root.classList.toggle('is-scrolled', y > 4);
    if (root.classList.contains('is-menu')) return;
    if (y < 80) { root.classList.remove('nav-hide'); acc = 0; return; }
    acc = Math.sign(dy) === Math.sign(acc) ? acc + dy : dy;
    // seuils larges : un petit rebond du pavé tactile ne fait plus monter et descendre la barre
    if (acc > 56) root.classList.add('nav-hide');
    else if (acc < -40) root.classList.remove('nav-hide');
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  $('[data-nav]')?.addEventListener('focusin', () => root.classList.remove('nav-hide'));
  onScroll();

  /* Menu mobile */
  const burger = $('[data-burger]'), menu = $('[data-menu]');
  if (burger && menu) {
    const setMenu = (open) => {
      burger.setAttribute('aria-expanded', String(open));
      $('.sr-only', burger).textContent = open ? 'Fermer le menu' : 'Ouvrir le menu';
      root.classList.toggle('is-menu', open);
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) { menu.hidden = false; requestAnimationFrame(() => requestAnimationFrame(() => menu.classList.add('is-open'))); }
      else { menu.classList.remove('is-open'); setTimeout(() => { if (!menu.classList.contains('is-open')) menu.hidden = true; }, 420); }
    };
    burger.addEventListener('click', () => setMenu(burger.getAttribute('aria-expanded') !== 'true'));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape' && root.classList.contains('is-menu')) { setMenu(false); burger.focus(); } });
  }

  /* Apparitions */
  const groups = new Map();
  $$('[data-reveal]').forEach((el) => {
    const i = groups.get(el.parentElement) || 0;
    groups.set(el.parentElement, i + 1);
    if (i) el.style.setProperty('--rd', `${Math.min(i, 5) * .07}s`);
  });
  const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
  $$('[data-reveal]').forEach((el) => io.observe(el));

  const setFill = (r) => r.style.setProperty('--p', `${((r.value - r.min) / (r.max - r.min)) * 100}%`);

  /* Tarifs : ce que vous gardez */
  const price = $('[data-price]'), qty = $('[data-qty]');
  if (price && qty) {
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
  }

  /* Tarifs : le pack choisi */
  $$('[data-pack]').forEach((p) => p.addEventListener('click', (e) => {
    if (e.target.closest('a')) return;
    $$('[data-pack]').forEach((q) => q.classList.toggle('is-sel', q === p));
  }));

  /* Affiliation : simulateur de commission */
  const affP = $('[data-aff-price]'), affR = $('[data-aff-rate]'), affN = $('[data-aff-n]');
  if (affP && affR && affN) {
    const sim = () => {
      const p = +affP.value, r = +affR.value, n = +affN.value;
      $('[data-aff-price-out]').textContent = xof(p);
      $('[data-aff-rate-out]').textContent = `${r} %`;
      $('[data-aff-n-out]').textContent = fmt(n);
      $('[data-aff-one]').textContent = xof(p * r / 100);
      $('[data-aff-total]').textContent = xof(p * r / 100 * n);
      [affP, affR, affN].forEach(setFill);
    };
    [affP, affR, affN].forEach((r) => r.addEventListener('input', sim));
    sim();
  }

  /* Centre d'aide : recherche dans les articles */
  const q = $('[data-help-q]');
  if (q) {
    const items = $$('[data-help-item]'), cards = $$('[data-help-card]'), none = $('[data-help-none]');
    const norm = (t) => t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    q.addEventListener('input', () => {
      const v = norm(q.value.trim());
      root.classList.toggle('is-searching', !!v);
      items.forEach((it) => { it.hidden = v && !norm(it.textContent).includes(v); });
      cards.forEach((c) => { c.hidden = !$$('[data-help-item]', c).some((it) => !it.hidden); });
      none.hidden = cards.some((c) => !c.hidden);
    });
    $$('[data-help-quick]').forEach((b) => b.addEventListener('click', () => {
      q.value = b.dataset.helpQuick;
      q.dispatchEvent(new Event('input'));
      q.focus({ preventScroll: true });
      const first = cards.find((c) => !c.hidden);
      if (first) first.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }));
  }

  /* Blog : filtres par thème */
  const chips = $$('[data-filter]');
  if (chips.length) {
    const posts = $$('[data-cat]');
    chips.forEach((c) => c.addEventListener('click', () => {
      chips.forEach((d) => d.setAttribute('aria-pressed', String(d === c)));
      const f = c.dataset.filter;
      posts.forEach((p) => { p.hidden = f !== 'all' && p.dataset.cat !== f; });
    }));
  }

  /* Pages légales : la section en cours est surlignée dans le sommaire */
  const toc = $$('[data-toc] a');
  if (toc.length && 'IntersectionObserver' in window) {
    const map = new Map(toc.map((a) => [a.getAttribute('href').slice(1), a]));
    const seen = new Set();
    const tio = new IntersectionObserver((es) => {
      es.forEach((e) => (e.isIntersecting ? seen.add(e.target.id) : seen.delete(e.target.id)));
      const cur = [...map.keys()].find((id) => seen.has(id));
      if (cur) toc.forEach((a) => a.classList.toggle('is-on', a === map.get(cur)));
    }, { rootMargin: '-20% 0px -60% 0px' });
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) tio.observe(s); });
  }

  /* Article d'aide : votre avis */
  const fb = $('[data-feedback]');
  if (fb) {
    const btns = $$('button', fb), ok = $('[data-feedback-ok]', fb);
    btns.forEach((b) => b.addEventListener('click', () => {
      btns.forEach((c) => c.setAttribute('aria-pressed', String(c === b)));
      ok.hidden = false;
      ok.textContent = b.dataset.v === 'oui' ? 'Merci, votre avis nous aide à améliorer l’aide.' : 'Merci. Écrivez-nous à contact@mepaye.com, nous vous répondons sous 24 h ouvrées.';
    }));
  }

  /* Développeurs : exemples de code (langage, copie, lignes de chaque étape) */
  const dv = $('[data-dv-code]');
  if (dv) {
    const tabs = $$('[data-lang]', dv), pres = $$('pre[data-code]', dv), file = $('[data-ide-file]', dv), copy = $('[data-ide-copy]', dv);
    const steps = $$('[data-dv-step]');
    let on = -1;
    const hl = (i) => {
      pres.forEach((p) => {
        p.classList.toggle('has-focus', i >= 0);
        $$('.ln', p).forEach((l) => l.classList.toggle('is-hl', l.dataset.l === String(i)));
      });
    };
    const pick = (t, focus) => {
      tabs.forEach((u) => { const s = u === t; u.setAttribute('aria-selected', String(s)); u.tabIndex = s ? 0 : -1; });
      pres.forEach((p) => { p.hidden = p.dataset.code !== t.dataset.lang; });
      file.textContent = t.dataset.file;
      if (focus) t.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => pick(t));
      t.addEventListener('keydown', (e) => {
        const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); }
      });
    });
    copy.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(pres.find((p) => !p.hidden).innerText.trim());
        copy.classList.add('is-done'); copy.setAttribute('aria-label', 'Code copié');
        setTimeout(() => { copy.classList.remove('is-done'); copy.setAttribute('aria-label', 'Copier le code'); }, 1600);
      } catch (e) { /* presse-papiers indisponible */ }
    });
    steps.forEach((b) => {
      const i = +b.dataset.dvStep;
      b.addEventListener('click', () => {
        on = on === i ? -1 : i;
        steps.forEach((c) => c.setAttribute('aria-pressed', String(+c.dataset.dvStep === on)));
        hl(on);
      });
      b.addEventListener('mouseenter', () => hl(i));
      b.addEventListener('mouseleave', () => hl(on));
    });
  }

  /* Développeurs : le journal des événements défile tant qu'il est visible */
  const dlog = $('[data-dv-log]');
  if (dlog && !reduce) {
    const ev = [['payment.succeeded · 4 750 XOF', '200'], ['payment.succeeded · 23 750 XOF', '200'], ['payment.failed · 9 500 XOF', '200'], ['payment.succeeded · 2 000 XOF', '200'], ['payment.succeeded · 25 000 XOF', '200']];
    let k = 0, timer = null;
    const tick = () => {
      const [s, e] = ev[k++ % ev.length];
      const li = document.createElement('li');
      li.innerHTML = `<time>${new Date().toLocaleTimeString('fr-FR')}</time><span>${s}</span><em>${e}</em>`;
      dlog.append(li);
      while (dlog.children.length > 6) dlog.firstElementChild.remove();
    };
    new IntersectionObserver(([en]) => {
      if (en.isIntersecting && !timer) timer = setInterval(tick, 1800);
      else if (!en.isIntersecting && timer) { clearInterval(timer); timer = null; }
    }).observe(dlog);
  }

  /* Documentation : onglets de langage et copie du code */
  const copyText = async (txt, btn, label) => {
    try {
      await navigator.clipboard.writeText(txt);
      btn.classList.add('is-done');
      if (label) btn.setAttribute('aria-label', 'Copié');
      setTimeout(() => { btn.classList.remove('is-done'); if (label) btn.setAttribute('aria-label', label); }, 1600);
      return true;
    } catch (e) { return false; }
  };
  $$('[data-cb]').forEach((box) => {
    const tabs = $$('[role="tab"]', box), pres = $$('pre', box);
    const pick = (i, focus) => {
      tabs.forEach((t, j) => { t.setAttribute('aria-selected', String(i === j)); t.tabIndex = i === j ? 0 : -1; });
      pres.forEach((p, j) => { p.hidden = i !== j; });
      if (focus) tabs[i].focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => pick(i));
      t.addEventListener('keydown', (e) => {
        const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { e.preventDefault(); pick((i + d + tabs.length) % tabs.length, true); }
      });
    });
    const cp = $('[data-cb-copy]', box);
    cp.addEventListener('click', () => copyText(pres.find((p) => !p.hidden).innerText.trim(), cp, 'Copier le code'));
  });

  /* Créer un ebook : le style change la couverture, les chapitres s'écrivent */
  const eb = $('[data-eb]');
  if (eb) {
    const cover = $('[data-eb-cover]', eb), radios = $$('[data-eb-style]', eb), chs = $$('[data-eb-ch]', eb), status = $('[data-eb-status]', eb);
    const setStyle = (r, focus) => {
      radios.forEach((x) => { const on = x === r; x.setAttribute('aria-checked', String(on)); x.tabIndex = on ? 0 : -1; });
      cover.className = `eb__cover eb__cover--${r.dataset.ebStyle}`;
      if (focus) r.focus();
    };
    radios.forEach((r, i) => {
      r.addEventListener('click', () => setStyle(r));
      r.addEventListener('keydown', (e) => {
        const d = ['ArrowRight', 'ArrowDown'].includes(e.key) ? 1 : ['ArrowLeft', 'ArrowUp'].includes(e.key) ? -1 : 0;
        if (d) { e.preventDefault(); setStyle(radios[(i + d + radios.length) % radios.length], true); }
      });
    });
    if (reduce) {
      chs.forEach((c) => c.classList.add('is-done'));
      status.textContent = 'Ebook prêt : PDF et DOCX';
    } else {
      let k = 0, timer = null;
      const step = () => {
        if (k === chs.length) { status.textContent = 'Ebook prêt : PDF et DOCX'; chs.forEach((c) => c.classList.replace('is-on', 'is-done')); k = -1; return; }
        if (k === -1 || k === 0) { chs.forEach((c) => c.classList.remove('is-on', 'is-done')); k = 0; }
        chs.forEach((c, j) => { c.classList.toggle('is-done', j < k); c.classList.toggle('is-on', j === k); });
        status.textContent = `Écriture du chapitre ${k + 1}`;
        k++;
      };
      new IntersectionObserver(([en]) => {
        if (en.isIntersecting && !timer) { step(); timer = setInterval(step, 2600); }
        else if (!en.isIntersecting && timer) { clearInterval(timer); timer = null; }
      }, { threshold: .3 }).observe(eb);
    }
  }

  /* Contact : le message est préparé dans la messagerie de l'utilisateur */
  const ct = $('[data-ct]');
  if (ct) {
    const err = $('[data-ct-err]', ct);
    $$('input, textarea', ct).forEach((f) => f.addEventListener('input', () => f.removeAttribute('aria-invalid')));
    ct.addEventListener('submit', (e) => {
      e.preventDefault();
      const nom = ct.elements.nom, mail = ct.elements.email, msg = ct.elements.message;
      const bad = [];
      if (!nom.value.trim()) bad.push([nom, 'votre nom']);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail.value.trim())) bad.push([mail, 'une adresse e-mail valide']);
      if (msg.value.trim().length < 5) bad.push([msg, 'votre message']);
      bad.forEach(([f]) => f.setAttribute('aria-invalid', 'true'));
      if (bad.length) { err.hidden = false; err.textContent = `Indiquez ${bad.map((b) => b[1]).join(', ')}.`; bad[0][0].focus(); return; }
      err.hidden = true;
      const sujet = ct.elements.sujet.value;
      const body = `${msg.value.trim()}\n\n${nom.value.trim()}\n${mail.value.trim()}`;
      location.href = `mailto:contact@mepaye.com?subject=${encodeURIComponent(`[${sujet}] Message de ${nom.value.trim()}`)}&body=${encodeURIComponent(body)}`;
    });
  }
  $$('[data-copy-mail]').forEach((b) => b.addEventListener('click', async () => {
    const ok = await copyText(b.dataset.copyMail, b);
    b.textContent = ok ? 'Adresse copiée' : b.dataset.copyMail;
    setTimeout(() => { b.textContent = 'Copier l’adresse'; }, 1800);
  }));

  if (reduce) $$('[data-reveal]').forEach((el) => el.classList.add('is-in'));
})();

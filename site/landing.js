/* mepaye · landing : la page est statique. Seul le logo avant le pied de page s'anime :
   deux personnes se parlent, se rejoignent et forment le m de mepaye, en suivant le défilement. */
(() => {
  'use strict';
  const menu = document.querySelector('.top__menu');
  const fin = document.querySelector('[data-final]');
  const sign = fin && fin.querySelector('.final__sign');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (sign) {
    const clamp = (v) => Math.min(1, Math.max(0, v));
    const ease = (t) => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
    let raf = 0, seen = false;
    const render = () => {
      raf = 0;
      const r = sign.getBoundingClientRect(), vh = innerHeight;
      // 0 quand le logo entre par le bas, 1 quand il atteint le tiers haut de l'écran
      const t = reduce ? 1 : clamp((vh * .9 - r.top) / (vh * .6));
      const m = ease(clamp(t / .6)), h = ease(clamp((t - .62) / .3));
      fin.style.setProperty('--m', m.toFixed(4));
      fin.style.setProperty('--h', h.toFixed(4));
      fin.style.setProperty('--talk', (1 - clamp((t - .4) / .16)).toFixed(3));
      fin.classList.toggle('is-talk', !reduce && seen && t < .56);
    };
    const ask = () => { if (!raf) raf = requestAnimationFrame(render); };
    new IntersectionObserver(([e]) => { seen = e.isIntersecting; ask(); }).observe(fin);
    addEventListener('scroll', ask, { passive: true });
    addEventListener('resize', ask);
    render();
  }
  // la barre se cache quand on descend, revient quand on remonte
  const top = document.querySelector('.top');
  if (top) {
    let lastY = scrollY, acc = 0, tick = 0;
    const upd = () => {
      tick = 0;
      const y = scrollY, dy = y - lastY; lastY = y;
      top.classList.toggle('is-stuck', y > 4);
      if (y < 60 || (menu && menu.open)) { top.classList.remove('is-hidden'); acc = 0; return; }
      acc = Math.sign(dy) === Math.sign(acc) ? acc + dy : dy;
      if (acc > 24) top.classList.add('is-hidden');
      else if (acc < -16) top.classList.remove('is-hidden');
    };
    addEventListener('scroll', () => { if (!tick) tick = requestAnimationFrame(upd); }, { passive: true });
    top.addEventListener('focusin', () => top.classList.remove('is-hidden'));
  }
  // le menu mobile se ferme après un choix, ou au clic en dehors
  if (menu) {
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) menu.open = false; });
    document.addEventListener('click', (e) => { if (menu.open && !menu.contains(e.target)) menu.open = false; });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') menu.open = false; });
  }
})();

// Apparition au défilement : titre, pastilles puis visuel de chaque section, une seule fois
(() => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  const groups = [...document.querySelectorAll('main .sec')];
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('is-in'); io.unobserve(e.target);
  }), { rootMargin: '0px 0px -10% 0px', threshold: .08 });
  document.documentElement.classList.add('rv');
  groups.forEach(sec => {
    const items = sec.querySelectorAll(':scope .wrap > .sh, :scope .wrap > .sh__strong, :scope .wrap > .sh__small, :scope .wrap > .chiprow, :scope .wrap > .panel, :scope .wrap > .kinds, :scope .wrap > .quotes, :scope .wrap > .why, :scope .wrap > ul');
    items.forEach((el, i) => { el.classList.add('rv-i'); el.style.setProperty('--rv-d', Math.min(i, 3) * 0.08 + 's'); io.observe(el); });
  });
})();

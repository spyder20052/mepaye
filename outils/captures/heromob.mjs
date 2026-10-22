import { chromium } from 'playwright-core';
const out = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
// hauteurs visibles réelles dans Safari / Chrome mobile (barres affichées)
for (const [n, w, h] of [['360', 360, 640], ['390', 390, 664], ['393', 393, 659], ['430', 430, 740]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
  await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' }); await p.waitForTimeout(1200);
  await p.screenshot({ path: `${out}/hm-${n}.png` });
  const r = await p.evaluate(() => { const q = s => { const e = [...document.querySelectorAll(s)].find(x => x.getClientRects().length && getComputedStyle(x).display !== 'none'); return e ? Math.round(e.getBoundingClientRect().bottom) : null; }; return { stage: q('.stage'), fine: q('.hero__fine'), btns: q('.hero__ctas'), vh: innerHeight }; });
  console.log(n, JSON.stringify(r));
  await p.close();
}
await b.close();

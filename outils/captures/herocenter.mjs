import { chromium } from 'playwright-core';
const out = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const [n, w, h] of [['360', 360, 640], ['390', 390, 664], ['390t', 390, 844], ['300t', 296, 636], ['430', 430, 740], ['430t', 430, 932]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' }); await p.waitForTimeout(1000);
  await p.screenshot({ path: `${out}/hc-${n}.png` });
  const r = await p.evaluate(() => { const t = document.querySelector('.hero__t').getBoundingClientRect().top; const f = [...document.querySelectorAll('.hero__fine')].find(x => getComputedStyle(x).display !== 'none').getBoundingClientRect().bottom; return { top: Math.round(t - 52), bas: Math.round(innerHeight - f), vh: innerHeight }; });
  console.log(n, JSON.stringify(r));
  await p.close();
}
await b.close();

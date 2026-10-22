import { chromium } from 'playwright-core';
const out = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const [n, w, h] of [['1000', 1000, 656], ['1280', 1280, 720], ['1440', 1440, 900], ['390', 390, 844]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' }); await p.waitForTimeout(2600);
  await p.screenshot({ path: `${out}/hs-${n}.png` });
  console.log(n, await p.evaluate(() => { const s = document.querySelector('.stage').getBoundingClientRect(); return [Math.round(s.top), Math.round(s.bottom), Math.round(s.left), Math.round(innerWidth - s.right)]; }));
  await p.close();
}
await b.close();

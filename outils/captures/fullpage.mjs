import { chromium } from 'playwright-core';
const out = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const [n, w] of [['d', 1440], ['m', 390]]) {
  const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1, reducedMotion: 'reduce' });
  await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' }); await p.waitForTimeout(800);
  await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); });
  await p.waitForTimeout(600);
  await p.screenshot({ path: `${out}/full-${n}.png`, fullPage: true });
  const ph = await p.$('#affiliation .split__fig'); await ph.scrollIntoViewIfNeeded();
  await p.close();
}
const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, reducedMotion: 'reduce' });
await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' });
const el = await p.$('#affiliation'); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(500);
await el.screenshot({ path: `${out}/aff-d.png` });
await b.close();

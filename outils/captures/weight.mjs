import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const [n, w, h, d] of [['mobile', 390, 844, 3], ['desktop', 1440, 900, 2]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: d, isMobile: n === 'mobile' });
  let first = 0; p.on('response', async r => { if (r.request().resourceType() === 'image') { try { first += (await r.body()).length; } catch {} } });
  await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' });
  const atLoad = first;
  await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 80)); } });
  await p.waitForTimeout(1500);
  const broken = await p.evaluate(() => [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src));
  console.log(n, 'premier écran', Math.round(atLoad / 1024), 'Ko', 'page entière', Math.round(first / 1024), 'Ko', 'cassées', broken);
  await p.close();
}
await b.close();

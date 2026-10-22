import { chromium } from 'playwright-core';
const [out, id] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
for (const [n, vp, mob] of [['d', { width: 1440, height: 900 }, false], ['m', { width: 390, height: 844 }, true]]) {
  const p = await (await b.newContext({ viewport: vp, isMobile: mob, hasTouch: mob, deviceScaleFactor: 2 })).newPage();
  await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  await p.locator('#' + id).scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
  await p.locator('#' + id).screenshot({ path: `${out}/${id}-${n}.png` });
}
await b.close();

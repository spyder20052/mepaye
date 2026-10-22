import { chromium } from 'playwright-core';
const dir = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: 393, height: 54 }, deviceScaleFactor: 4 });
for (const isl of ['1', '0']) {
  await p.goto(`file://${dir}/bar.html?island=${isl}`); await p.waitForTimeout(200);
  await p.screenshot({ path: `${dir}/sb-${isl}.png`, omitBackground: true, clip: { x: 0, y: 0, width: 393, height: 54 } });
}
console.log(await p.evaluate(() => getComputedStyle(document.querySelector('.time')).fontFamily + ' | ' + document.fonts.check('600 17px -apple-system')));
await b.close();

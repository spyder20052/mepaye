import { chromium } from 'playwright-core';
const dir = process.argv[2];
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage({ viewport: { width: 393, height: 798 }, deviceScaleFactor: 800 / 393 });
await p.goto(`file://${dir}/notif.html`); await p.waitForTimeout(500);
await p.screenshot({ path: `${dir}/notif.png`, clip: { x: 0, y: 0, width: 393, height: 798 } });
await b.close();

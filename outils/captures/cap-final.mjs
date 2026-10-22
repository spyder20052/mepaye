import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await (await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 })).newPage();
await p.goto('http://localhost:5188/', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
const el = p.locator('section[data-final]');
await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
const box = await el.boundingBox();
await p.screenshot({ path: 'captures-revue/avis/final-transition-m.png', clip: { x: 0, y: Math.max(0, box.y - 500), width: 390, height: Math.min(844, box.height + 500) } });
await b.close();

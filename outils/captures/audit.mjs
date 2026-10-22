import { chromium } from 'playwright-core';
import fs from 'fs';
const pages = fs.readdirSync(new URL('../../site', import.meta.url).pathname).filter((f) => f.endsWith('.html'));
const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const bad = [];
for (const [w, h, mob] of [[1440, 900, false], [390, 844, true]]) {
  const ctx = await b.newContext({ viewport: { width: w, height: h }, isMobile: mob, hasTouch: mob });
  // hors connexion : Google Fonts ne répond jamais, on l'écoute pas, sinon networkidle ne finit pas
  await ctx.route('**fonts.googleapis.com**', (r) => r.abort());
  await ctx.route('**fonts.gstatic.com**', (r) => r.abort());
  for (const pg of pages) {
    const p = await ctx.newPage();
    const errs = []; p.on('pageerror', (e) => errs.push(e.message)); p.on('console', (m) => m.type() === 'error' && errs.push(m.text().slice(0, 100)));
    p.on('requestfailed', (r) => errs.push('fail ' + r.url().slice(-60)));
    p.on('response', (r) => { if (r.status() >= 400 && r.url().includes('localhost')) errs.push(r.status() + ' ' + r.url().slice(-50)); });
    await p.goto('http://localhost:5188/' + (pg === 'index.html' ? '' : pg.replace('.html', '')), { waitUntil: 'networkidle' });
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    if (errs.length || sw > w) bad.push([w, pg, sw, errs.slice(0, 3)]);
    await p.close();
  }
  await ctx.close();
}
console.log(pages.length, 'pages x2', JSON.stringify(bad, null, 1));
await b.close();

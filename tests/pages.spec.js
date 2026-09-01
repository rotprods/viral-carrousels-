const { test, expect } = require('@playwright/test');

const origin = 'http://127.0.0.1:4173';
const viewports = [
  { name: 'iphone-390', width: 390, height: 844 },
  { name: 'iphone-430', width: 430, height: 932 },
  { name: 'desktop-1440', width: 1440, height: 1000 },
];

for (const vp of viewports) {
  test(`${vp.name}: Pages control plane is responsive and clean`, async ({ browser }) => {
    const context = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
    await context.grantPermissions(['clipboard-read','clipboard-write'], { origin });
    const page = await context.newPage();
    const consoleErrors = [];
    const pageErrors = [];
    const failed = [];
    page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
    page.on('pageerror', e => pageErrors.push(String(e)));
    page.on('requestfailed', r => failed.push(`${r.method()} ${r.url()}`));
    await page.goto(origin, { waitUntil: 'networkidle' });
    const dims = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
    expect(dims.sw).toBeLessThanOrEqual(dims.cw + 1);
    await expect(page.locator('a[href*="697fac8775c081919387509ec73c69a5"]')).toBeVisible();
    await expect(page.locator('.prompt')).toHaveCount(18);
    expect(consoleErrors).toEqual([]);
    expect(pageErrors).toEqual([]);
    expect(failed).toEqual([]);
    await context.close();
  });
}

test('P00–P17 copy canonical prompt source', async ({ browser }) => {
  const context = await browser.newContext();
  await context.grantPermissions(['clipboard-read','clipboard-write'], { origin });
  const page = await context.newPage();
  await page.goto(origin, { waitUntil: 'networkidle' });
  for (let i = 0; i < 18; i++) {
    const id = `P${String(i).padStart(2,'0')}`;
    const card = page.locator(`#prompt-${id.toLowerCase()}`);
    await expect(card).toHaveCount(1);
    await card.locator('button').click();
    const copied = (await page.evaluate(() => navigator.clipboard.readText())).trim();
    expect(copied.startsWith(`## ${id}`)).toBeTruthy();
    expect(copied.length).toBeGreaterThan(40);
  }
  await context.close();
});

test('portable source files are published with Pages', async ({ request }) => {
  for (const path of [
    '/prompts/PROMPTS.md',
    '/templates/visual-dna.template.json',
    '/templates/DESIGN.template.md',
    '/skills/visual-brand-system/SKILL.md',
    '/adapters/CODEX.md',
    '/adapters/CLAUDE_CODE.md',
    '/adapters/HIGGSFIELD_SUPERCOMPUTER.md',
  ]) {
    const r = await request.get(origin + path);
    expect(r.ok(), `${path} should be published`).toBeTruthy();
    expect((await r.body()).length).toBeGreaterThan(20);
  }
});

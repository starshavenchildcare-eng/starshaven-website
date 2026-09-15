const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const baseURL = process.env.BASE_URL || "http://127.0.0.1:4173";
const routes = ["/", "/home/", "/about/", "/programs/", "/enrolment-waitlist/", "/licensing-journey/", "/contact/", "/privacy/"];
const reviewDir = path.resolve("review");
fs.mkdirSync(reviewDir, { recursive: true });

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const viewport of [
      { name: "desktop", width: 1440, height: 1000 },
      { name: "mobile", width: 390, height: 844 },
    ]) {
      const context = await browser.newContext({ viewport });
      const page = await context.newPage();
      const consoleErrors = [];
      page.on("console", (message) => {
        if (message.type() === "error") consoleErrors.push(message.text());
      });
      page.on("pageerror", (error) => consoleErrors.push(error.message));

      for (const route of routes) {
        const response = await page.goto(baseURL + route, { waitUntil: "networkidle" });
        assert(response && response.ok(), `${viewport.name} ${route} returned ${response && response.status()}`);
        assert((await page.title()).includes("Stars Haven Childcare"), `${route} has an unexpected title`);
        assert((await page.locator("h1").count()) === 1, `${route} does not have exactly one h1`);
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
        assert(overflow <= 1, `${viewport.name} ${route} overflows horizontally by ${overflow}px`);
        const body = await page.locator("body").innerText();
        assert(!/not licensed by the Government of Ontario|Opening Sept 2025|7am\s*-\s*6pm/i.test(body), `${route} contains stale content`);
      }

      await page.goto(baseURL + "/", { waitUntil: "networkidle" });
      if (viewport.name === "mobile") {
        const toggle = page.locator(".menu-toggle");
        await toggle.click();
        assert((await toggle.getAttribute("aria-expanded")) === "true", "Mobile menu did not open");
        assert(await page.locator("#site-nav").isVisible(), "Mobile navigation is not visible after opening");
        await page.keyboard.press("Escape");
        assert((await toggle.getAttribute("aria-expanded")) === "false", "Escape did not close mobile menu");
      }
      await page.screenshot({ path: path.join(reviewDir, `home-${viewport.name}.png`), fullPage: true });
      assert(consoleErrors.length === 0, `${viewport.name} browser errors: ${consoleErrors.join(" | ")}`);
      await context.close();
    }

    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await context.newPage();
    await page.goto(baseURL + "/enrolment-waitlist/", { waitUntil: "networkidle" });
    await page.locator("details").first().click();
    await page.screenshot({ path: path.join(reviewDir, "enrolment-mobile.png"), fullPage: true });
    assert(await page.locator('a[href="mailto:starshavenchildcare@gmail.com"]').count(), "Current contact email is missing");
    await context.close();

    const noJs = await browser.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: false });
    const noJsPage = await noJs.newPage();
    await noJsPage.goto(baseURL + "/", { waitUntil: "domcontentloaded" });
    assert(await noJsPage.locator("#site-nav").isVisible(), "Navigation is unavailable without JavaScript");
    await noJs.close();

    console.log(`Verified ${routes.length} routes at desktop and mobile sizes.`);
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(error.stack || error);
  process.exit(1);
});

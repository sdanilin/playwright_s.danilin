import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Make sure to run headed.
        browser = await p.chromium.launch(headless=False)

        # Setup context however you like.
        context = await browser.new_context(viewport={"width":1920,"height":1080}, storage_state="auth.json")

        # Start tracing before creating / navigating a page.
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        # # Pause the page, and start recording manually.
        # page = await context.new_page()
        # await page.pause()
        # Open new page
        page = await context.new_page()
        # Go to https://beta.au.alterosmart.dev/
        await page.goto("https://beta.au.alterosmart.dev/")
        # Click text=Alerts >> nth=1
        await page.locator("text=Alerts").nth(1).click()
        await page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/alerts")
        # Click text=Settings >> nth=1
        await page.locator("text=Settings").nth(1).click()
        await page.wait_for_url("https://beta.au.alterosmart.dev/settings")
        # Click text=Alerts >> nth=3
        await page.locator("text=Alerts").nth(3).click()
        await page.wait_for_url("https://beta.au.alterosmart.dev/settings/signal-events")
        # Click text=Missing data
        await page.locator("text=Missing data").click()

        # Stop tracing and export it into a zip archive.
        context.tracing.stop(path="trace.zip")

        # ---------------------
        await context.close()
        await browser.close()
        asyncio.run(main())
from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")


    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Open new page
    page = context.new_page()
    # Go to https://beta.au.alterosmart.dev/
    page.goto("https://beta.au.alterosmart.dev/")
    # Click .hideableLeftMenu_icon__\+ooh9 > svg:nth-child(2)
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg:nth-child(2)").click()
    # Click text=Сигнальные ситуации >> nth=2
    page.locator("text=Сигнальные ситуации").nth(2).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/alerts")
    # Click text=Настройки >> nth=1
    page.locator("text=Настройки").nth(1).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings")
    # Click text=Сигнальные ситуации >> nth=3
    page.locator("text=Сигнальные ситуации").nth(3).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings/signal-events")
    # Click text=Пропуски
    page.locator("text=Пропуски").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
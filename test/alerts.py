from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width":1920,"height":1080}, storage_state="auth.json")

    # Open new page
    page = context.new_page()

    # Go to https://beta.au.alterosmart.dev/
    page.goto("https://beta.au.alterosmart.dev/")

    # Click text=Alerts
    page.locator("text=Alerts").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/alerts")

    # Click .pq-trends-header > div:nth-child(2)
    page.locator(".pq-trends-header > div:nth-child(2)").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/alerts/table")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

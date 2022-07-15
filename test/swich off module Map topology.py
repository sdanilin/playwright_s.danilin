from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport={"width":1920,"height":1080}, storage_state="auth.json")

    # Open new page
    page = context.new_page()

    # Go to https://beta.au.alterosmart.dev/
    page.goto("https://beta.au.alterosmart.dev/")

    # Click text=Equipment map
    page.locator("text=Equipment map").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/map")

    # Click text=Settings
    page.locator("text=Settings").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings/topology")

    # Click text=System
    page.locator("text=System").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings/system/about")

    # Click text=System modules
    page.locator("text=System modules").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings/system/modules")

    # Click text=Map topologyMap topology >> label span
    page.locator("text=Map topologyMap topology >> label span").click()

    # Click text=Equipment map
    page.locator("text=Equipment map").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/map")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

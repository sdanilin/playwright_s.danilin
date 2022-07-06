from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://beta.au.alterosmart.dev/
    page.goto("https://beta.au.alterosmart.dev/")
    # Go to https://beta.au.alterosmart.dev/login
    page.goto("https://beta.au.alterosmart.dev/login")
    # Click text=Do not have an account?Sign upen >> div >> nth=3
    page.locator("text=Do not have an account?Sign upen >> div").nth(3).click()
    # Click text=Логин >> input
    page.locator("text=Логин >> input").click()
    # Fill text=Логин >> input
    page.locator("text=Логин >> input").fill("s.danilin")
    # Press Tab
    page.locator("text=Логин >> input").press("Tab")
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("123123123")
    # Press Enter
    page.locator("input[type=\"password\"]").press("Enter")
    page.wait_for_url("https://beta.au.alterosmart.dev/")
    # Click #pq div >> nth=2
    page.locator("#pq div").nth(2).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/pq")
    # Click .pq-trends-header > div:nth-child(2)
    page.locator(".pq-trends-header > div:nth-child(2)").click()
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
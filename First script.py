'''User autorization on web site AU-Beta'''

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://beta.au.alterosmart.dev/login
    page.goto("https://beta.au.alterosmart.dev/login")

    # Click text=Username >> input
    page.locator("text=Username >> input").click()

    # Fill text=Username >> input
    page.locator("text=Username >> input").fill("s.danilin")

    # Click text=Username >> input
    page.locator("text=Username >> input").click()

    # Click input[type="password"]
    page.locator("input[type=\"password\"]").click()

    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("********")

    # Click svg
    page.locator("svg").click()

    # Click path
    page.locator("path").click()

    # Click button:has-text("Sign in")
    page.locator("button:has-text(\"Sign in\")").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
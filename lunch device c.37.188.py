from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://beta.au.alterosmart.dev/
    page.goto("https://beta.au.alterosmart.dev/")
    # Go to https://beta.au.alterosmart.dev/login
    page.goto("https://beta.au.alterosmart.dev/login")
    # Click text=Username >> input
    page.locator("text=Username >> input").click()
    # Fill text=Username >> input
    page.locator("text=Username >> input").fill("s.danilin")
    # Press Tab
    page.locator("text=Username >> input").press("Tab")
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("123123123")
    # Press Enter
    page.locator("input[type=\"password\"]").press("Enter")
    page.wait_for_url("https://beta.au.alterosmart.dev/")
    # Click .hideableLeftMenu_icon__\+ooh9 > svg:nth-child(2)
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg:nth-child(2)").click()
    # Click text=Настройки >> nth=1
    page.locator("text=Настройки").nth(1).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings")
    # Click text=Топология >> nth=1
    page.locator("text=Топология").nth(1).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings/topology")
    # Click li:nth-child(3) > .tree_node__CkUpb > .tpl-icon
    page.locator("li:nth-child(3) > .tree_node__CkUpb > .tpl-icon").click()
    # Click .tpl-branch > ul > li:nth-child(3) > .tree_node__CkUpb > .tpl-icon
    page.locator(".tpl-branch > ul > li:nth-child(3) > .tree_node__CkUpb > .tpl-icon").click()
    # Click .tpl-branch > ul > li:nth-child(3) > ul > li:nth-child(3) > .tree_node__CkUpb > .tpl-icon
    page.locator(".tpl-branch > ul > li:nth-child(3) > ul > li:nth-child(3) > .tree_node__CkUpb > .tpl-icon").click()
    # Click .tpl-branch > ul > li:nth-child(3) > ul > li:nth-child(3) > ul > li > .tree_node__CkUpb > .tpl-icon >> nth=0
    page.locator(".tpl-branch > ul > li:nth-child(3) > ul > li:nth-child(3) > ul > li > .tree_node__CkUpb > .tpl-icon").first.click()
    # Click span:has-text("tcp42") >> nth=0
    page.locator("span:has-text(\"tcp42\")").first.click()
    # Click text=Считать конфигурацию
    page.locator("text=Считать конфигурацию").click()
    # Click div:nth-child(6) > .nsi-panel__title > svg
    page.locator("div:nth-child(6) > .nsi-panel__title > svg").click()
    # Click text=Скаляры
    page.locator("text=Скаляры").click()
    # Click text=Дискретные сигналы
    page.locator("text=Дискретные сигналы").click()
    # Click text=Запустить
    page.locator("text=Запустить").click()
    # Click .hideableLeftMenu_icon__\+ooh9 > svg >> nth=0
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg").first.click()
    # Click .hideableLeftMenu_icon__\+ooh9 > svg >> nth=0
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg").first.click()
    # Click .hideableLeftMenu_icon__\+ooh9 > svg:nth-child(2)
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg:nth-child(2)").click()
    # Click svg:has-text("Развернуть все")
    page.locator("svg:has-text(\"Развернуть все\")").click()
    # Click svg:has-text("Свернуть все")
    page.locator("svg:has-text(\"Свернуть все\")").click()
    # Click #system__nav__screen__panel >> text=Топология
    page.locator("#system__nav__screen__panel >> text=Топология").click()
    # Click div:has-text("Карта устройствЭкраныСигнальные ситуацииИмпорт/ЭкспортЖурналСправочникиОтчетыБиб") >> nth=1
    page.locator("div:has-text(\"Карта устройствЭкраныСигнальные ситуацииИмпорт/ЭкспортЖурналСправочникиОтчетыБиб\")").nth(1).click()
    # Click .hideableLeftMenu_icon__\+ooh9 > svg >> nth=0
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg").first.click()
    # Click .alerts__button > svg >> nth=0
    page.locator(".alerts__button > svg").first.click()
    page.wait_for_url("https://beta.au.alterosmart.dev/user/profile")
    # Click .hideableLeftMenu_icon__\+ooh9 > svg:nth-child(2)
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg:nth-child(2)").click()
    # Click .hideableLeftMenu_icon__\+ooh9 > svg >> nth=0
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg").first.click()
    # Click div:nth-child(3) >> nth=0
    page.locator("div:nth-child(3)").first.click()
    # Click text=Изменен пользователь Serg >> nth=0
    page.locator("text=Изменен пользователь Serg").first.click()
    page.wait_for_url("https://beta.au.alterosmart.dev/settings/users")
    # Click text=email: s.sanok1@alterosmart.com >> nth=0
    page.locator("text=email: s.sanok1@alterosmart.com").first.click()
    # Click div:has-text("История измененийПоследние действия5 июль 17:54:57Sergemail: s.sanok1@alterosmar") >> nth=0
    page.locator("div:has-text(\"История измененийПоследние действия5 июль 17:54:57Sergemail: s.sanok1@alterosmar\")").first.click()
    # Click text=114
    page.locator("text=114").click()
    # Click text=Сигнальные ситуации >> nth=2
    page.locator("text=Сигнальные ситуации").nth(2).click()
    # Click text=te_end=0 16:40:41 — 16:40:42
    page.locator("text=te_end=0 16:40:41 — 16:40:42").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/alerts/list")
    # Click .hideableLeftMenu_icon__\+ooh9 > svg >> nth=0
    page.locator(".hideableLeftMenu_icon__\\+ooh9 > svg").first.click()
    # Click text=Экраны >> nth=1
    page.locator("text=Экраны").nth(1).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/")
    # Click #pq div >> nth=2
    page.locator("#pq div").nth(2).click()
    page.wait_for_url("https://beta.au.alterosmart.dev/dashboards/pq")
    # Click [placeholder="Поиск"]
    page.locator("[placeholder=\"Поиск\"]").click()
    # Press a with modifiers
    page.locator("[placeholder=\"Поиск\"]").press("Control+a")
    # Click div:nth-child(32) > .gantt__col-1 > .registrator-cell > au-checkbox > .checkbox > .checkbox__checkmark
    page.locator("div:nth-child(32) > .gantt__col-1 > .registrator-cell > au-checkbox > .checkbox > .checkbox__checkmark").click()
    # Click .pq-trends-header > div:nth-child(2)
    page.locator(".pq-trends-header > div:nth-child(2)").click()
    # Click text=tcp42
    page.locator("text=tcp42").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/registrators/d8cf7db5-5ed0-4b19-aff0-a8eb72e5a1a4/power")
    # Click text=НЧК
    page.locator("text=НЧК").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/registrators/d8cf7db5-5ed0-4b19-aff0-a8eb72e5a1a4/lfo")
    # Click text=Несимметрия
    page.locator("text=Несимметрия").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/registrators/d8cf7db5-5ed0-4b19-aff0-a8eb72e5a1a4/unbalance")
    # Click text=Зафиксировать Ua на векторной диаграммеТокиНапряжения >> div >> nth=1
    page.locator("text=Зафиксировать Ua на векторной диаграммеТокиНапряжения >> div").nth(1).click()
    # Click text=Дискретные сигналы
    page.locator("text=Дискретные сигналы").click()
    page.wait_for_url("https://beta.au.alterosmart.dev/registrators/d8cf7db5-5ed0-4b19-aff0-a8eb72e5a1a4/digitals")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)

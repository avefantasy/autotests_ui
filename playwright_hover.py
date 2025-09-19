from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим ссылку registration и наводим курсор
    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.hover()

    # Задержка 5s
    page.wait_for_timeout(5000)
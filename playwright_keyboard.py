from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Фокус на поле Email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # Имитация нажатия клавиш для ввода текста посимвольно
    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=300)
    page.keyboard.press("ControlOrMeta+A")

    # Задержка 5s
    page.wait_for_timeout(5000)
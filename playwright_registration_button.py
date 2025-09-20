from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверка, что кнопка registration - disabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Посимвольный ввод email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.focus()
    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=300)

    # Посимвольный ввод username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.focus()
    for char in 'username':
        page.keyboard.type(char, delay=300)

    # Посимвольный ввод password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.focus()
    for char in 'password':
        page.keyboard.type(char, delay=300)

    # Проверка, что кнопка registration - enabled
    expect(registration_button).not_to_be_disabled()
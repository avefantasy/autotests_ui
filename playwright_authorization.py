from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнение email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполнение password
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    # Нажатие кнопки Login
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверка сообщения об ошибке
    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    # Задержка 5s
    page.wait_for_timeout(5000)
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Проверка наличия элемента email на странице
    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    # Проверка наличия элемента password на странице
    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

    # Проверка наличия элемента login на странице
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    # Переход на форму registration
    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.click()

    # Проверка наличия элемента email на странице
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    # Проверка наличия элемента password на странице
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    #  Проверка наличия элемента registration на странице
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()

    # Задержка 5s
    page.wait_for_timeout(5000)
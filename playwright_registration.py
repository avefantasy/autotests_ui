from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнение email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    # Заполнение username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # Заполнение password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # Нажатие на кнопку registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Проверка видимости заголовка Dashboard
    dashboard_visible = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_visible).to_be_visible()
    expect(dashboard_visible).to_have_text("Dashboard")

    # Задержка 5s
    page.wait_for_timeout(5000)
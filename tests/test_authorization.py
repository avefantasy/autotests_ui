import pytest
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"),
                                            ("user.name@gmail.com", "  "),
                                            ("  ", "password")])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    # Переход на страницу входа
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнение email
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполнение password
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    # Нажатие кнопки Login
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверка сообщения об ошибке
    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
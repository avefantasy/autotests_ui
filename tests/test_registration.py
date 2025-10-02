from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    # Переход на страницу входа
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнение email
    registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    # Заполнение username
    registration_username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # Заполнение password
    registration_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # Нажатие на кнопку registration
    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Проверка успешной регистрации, на экране Dashboard
    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
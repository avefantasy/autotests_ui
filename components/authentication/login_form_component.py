from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    # Заполнение email и password
    def fill(self, email, password):
        self.email_input.fill(email)

        self.password_input.fill(password)

    # Проверка корректности email и password
    def check_visible(self, email, password):
        expect(self.email_input).to_have_value(email)
        expect(self.password_input).to_have_value(password)

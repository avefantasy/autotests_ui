from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input

import allure


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page,'login-form-password-input', 'Password')

    # Заполнение email и password
    @allure.step("Fill login form")
    def fill(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)

    # Проверка корректности email и password
    @allure.step("Check visible login form")
    def check_visible(self, email, password):
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)

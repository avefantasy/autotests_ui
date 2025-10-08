import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link

# Page Object для страницы регистрации
class RegistrationPage(BasePage):
    # Метод, хранящий локаторы
    def __init__(self, page: Page):
        super().__init__(page)

        # Компонент для заполнения формы регистрации и проверки корректности данных
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')

        self.login_link = Link(page, 'registration-page-login-link', 'Login')

    # Нажатие на ссылку login
    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))

    # Нажатие кнопки регистрации
    def click_registration_button(self):
        self.registration_button.click()

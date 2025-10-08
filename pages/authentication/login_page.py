import re
from playwright.sync_api import Page

from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent

# Page Object для страницы авторизации
class LoginPage(BasePage):
    # Метод, хранящий локаторы
    def __init__(self, page: Page):
        super().__init__(page)

        # Компонент заполнения формы авторизации и проверки данных
        self.login_form = LoginFormComponent(page)


        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(
            page,'login-page-wrong-email-or-password-alert', 'Wrong email or password')


    # Нажатие кнопки авторизации
    def click_login_button(self):
        self.login_button.click()

    # Нажатие ссылки регистрации
    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    # Проверка сообщения об ошибке
    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")

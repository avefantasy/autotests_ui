from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent

# Page Object для страницы авторизации
class LoginPage(BasePage):
    # Метод, хранящий локаторы
    def __init__(self, page: Page):
        super().__init__(page)

        # Компонент заполнения формы авторизации и проверки данных
        self.login_form = LoginFormComponent(page)


        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('register-page-register-button')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # Нажатие кнопки авторизации
    def click_login_button(self):
        self.login_button.click()

    # Нажатие ссылки регистрации
    def click_registration_button(self):
        self.registration_link.click()

    # Проверка сообщения об ошибке
    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")

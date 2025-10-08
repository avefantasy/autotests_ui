from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button

# Page Object для страницы регистрации
class RegistrationPage(BasePage):
    # Метод, хранящий локаторы
    def __init__(self, page: Page):
        super().__init__(page)

        # Компонент для заполнения формы регистрации и проверки корректности данных
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')

    # Нажатие кнопки регистрации
    def click_registration_button(self):
        self.registration_button.click()

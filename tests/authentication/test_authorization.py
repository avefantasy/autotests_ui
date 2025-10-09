import allure
import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.AUTHORIZATION) # Добавили story
class TestAuthorization:
    @pytest.mark.parametrize("email, password", [("user.name@gmail.com", "password"),
                                                 ("user.name@gmail.com", "  "),
                                                 ("  ", "password")])
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        allure.dynamic.title(f"Attempt to login with email: {email}")

        # Переход на страницу входа
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполнение email и password
        login_page.login_form.fill(email=email, password=password)
        login_page.login_form.check_visible(email=email, password=password)

        # Нажатие кнопки Login
        login_page.click_login_button()

        # Проверка сообщения об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self,login_page: LoginPage, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        # Переход на страницу регистрации
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Регистрация
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        # Проверка видимости Dashboard и выход из профиля
        dashboard_page.check_visible_dashboard_title.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        # Заполнение email и password
        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.login_form.check_visible(email="user.name@gmail.com", password="password")

        # Нажатие кнопки Login
        login_page.click_login_button()

        # Проверка Dashboard на экране
        dashboard_page.check_visible_dashboard_title.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):

        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        # Переходим по ссылке регистрации
        login_page.click_registration_link()

        # Проверяем форму регистрации
        registration_page.registration_form.check_visible(email="", username="", password="")



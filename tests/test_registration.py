import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    # Переход на страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнение email, username и password
    registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
    registration_page.registration_form.check_visible(email="user.name@gmail.com", username="username", password="password")

    # Нажатие на кнопку registration
    registration_page.click_registration_button()

    # Проверка успешной регистрации, на экране Dashboard
    dashboard_page.check_visible_dashboard_title.check_visible()
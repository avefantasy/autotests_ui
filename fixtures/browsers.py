import pytest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage

# Фикстура открытия и закрытия браузера
@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

# Фикстура регистрация нового пользователя и сохранение авторизованного состояния
@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    # Переход на страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнение email
    # Заполнение username
    # Заполнение password
    # Нажатие на кнопку registration
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    # Сохранение авторизованного состояния в json файл
    context.storage_state(path="browser-state.json")
    browser.close()

# Фикстура авторизованной сессии
@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page(storage_state="browser-state.json")
    browser.close()

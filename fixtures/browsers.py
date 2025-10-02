import pytest
from playwright.sync_api import Playwright, Page

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

    # Переход на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнение email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    # Заполнение username
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # Заполнение password
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    # Нажатие на кнопку registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранение авторизованного состояния в json файл
    context.storage_state(path="browser-state.json")

# Фикстура авторизованной сессии
@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page(storage_state="browser-state.json")
    browser.close()

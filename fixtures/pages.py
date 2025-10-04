import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

# Фикстура инициализации LoginPage
@pytest.fixture()
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

# Фикстура инициализации RegistrationPage
@pytest.fixture()
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

# Фикстура инициализации DashboardPage
@pytest.fixture()
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)

# Фикстура инициализации CoursesListPage

def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)

# Фикстура инициализации CreateCoursePage

def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)
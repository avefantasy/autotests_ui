import pytest
from playwright.sync_api import Page
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage

# Фикстура инициализации LoginPage
@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

# Фикстура инициализации RegistrationPage
@pytest.fixture()
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)

# Фикстура инициализации DashboardPage
@pytest.fixture()
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page=page)

# Фикстура инициализации CoursesListPage
@pytest.fixture()
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)

# Фикстура инициализации CreateCoursePage
@pytest.fixture()
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)

# Открытие страницы Dashboard минуя авторизацию
@pytest.fixture
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=page_with_state)
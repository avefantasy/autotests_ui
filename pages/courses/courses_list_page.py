from playwright.sync_api import Page, expect
from pages.base_page import BasePage

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.сourse_view_menu_component import CourseViewMenuComponent

# Page Object для проверки страницы Courses
class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Проверка NavBar и SideBar
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Компонент для проверки отсутствия курсов
        self.empty_view = EmptyViewComponent(page, 'courses-list')

        # Компонент для проверки наличия курсов
        self.course_view = CourseViewComponent(page)

        # Компонент для заголовка и кнопки создания курса
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Компонент для работы с меню курса
        self.view_menu = CourseViewMenuComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )



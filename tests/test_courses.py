from playwright.sync_api import Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, chromium_page_with_state: Page, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):

        # Переход на страницу Courses
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка NavBar и SideBar
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        # Проверка наличия и текста заголовка "Courses"
        courses_list_page.check_visible_courses_title()

        # Проверка отсутствия курсов
        courses_list_page.check_visible_empty_view()

        #Проверка отображения кнопки создания курса
        courses_list_page.check_visible_create_course_button()

    def test_create_course(self, chromium_page_with_state: Page, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Переход на страницу создания курсов
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Проверка заголовка и неактивности кнопки создания курса
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()

        # Картинка предпросмотра и блок предпросмотра картинки курса
        create_course_page.check_visible_image_preview_empty_view()

        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        create_course_page.check_visible_image_upload_view()

        # Проверка формы создания курса
        create_course_page.check_visible_create_course_form(title="", description="", estimated_time="", max_score="0", min_score="0")

        # Проверка наличия заголовка "Exercises"
        create_course_page.check_visible_exercises_title()

        # Проверка наличия кнопки создания задания
        create_course_page.check_visible_create_exercise_button()

        # Проверка отображения блока с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()

        # Загрузка картинки курса
        create_course_page.upload_preview_image(file = "./testdata/files/robot.png")

        # Проверка, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.check_visible_image_upload_view()

        # Заполнение формы создания курса
        create_course_page.fill_create_course_form(title = "Playwright",
                                                estimated_time = "2 weeks",
                                                description = "Playwright",
                                                max_score = "100",
                                                min_score = "10")

        # Нажатие кнопки создания курса
        create_course_page.click_create_course_button()

        # Проверка наличия заголовка "Courses"
        courses_list_page.check_visible_courses_title()

        # Проверка наличия кнопки создания курса
        courses_list_page.check_visible_create_course_button()

        # Проверка корректности отображаемых данных на карточке курса
        courses_list_page.check_visible_course_card(index=0,
                                                    title="Playwright",
                                                    max_score="100",
                                                    min_score="10",
                                                    estimated_time="2 weeks")



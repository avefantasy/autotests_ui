from playwright.sync_api import Page
import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    # Отсутствие курсов
    def test_empty_courses_list(self, chromium_page_with_state: Page, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):

        # Переход на страницу Courses
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка NavBar и SideBar
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        # Проверка наличия и текста заголовка "Courses", отображения кнопки создания курса
        courses_list_page.toolbar_view.check_visible()

        # Проверка отсутствия курсов
        courses_list_page.check_visible_empty_view()

    # Создание курса
    def test_create_course(self, chromium_page_with_state: Page, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Переход на страницу создания курсов
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        courses_list_page.navbar.check_visible("username")

        # Проверка заголовка и неактивности кнопки создания курса
        create_course_page.check_course_toolbar.check_visible()

        # Картинка предпросмотра и блок предпросмотра картинки курса
        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        # Проверка формы создания курса
        create_course_page.create_course_form.check_visible(title="", description="", estimated_time="", max_score="0", min_score="0")

        # Проверка наличия заголовка "Exercises"
        # Проверка наличия кнопки создания задания
        create_course_page.create_course_exercises_toolbar.check_visible()

        # Проверка отображения блока с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()

        # Загрузка картинки курса
        create_course_page.image_upload_widget.upload_preview_image(file = "./testdata/files/robot.png")

        # Проверка, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # Заполнение формы создания курса
        create_course_page.create_course_form.fill(title = "Playwright",
                                                estimated_time = "2 weeks",
                                                description = "Playwright",
                                                max_score = "100",
                                                min_score = "10")

        # Проверка корректности введённых данных
        create_course_page.create_course_form.check_visible(title="Playwright",
                                                   estimated_time="2 weeks",
                                                   description="Playwright",
                                                   max_score="100",
                                                   min_score="10")

        # Нажатие кнопки создания курса
        create_course_page.check_course_toolbar.click_create_course_button()

        # Проверка наличия кнопки создания курса и наличия заголовка "Courses"
        courses_list_page.toolbar_view.check_visible()

        # Проверка корректности отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright",
                                                    max_score="100",
                                                    min_score="10",
                                                    estimated_time="2 weeks")

    # Изменение курса
    def test_edit_course(self, chromium_page_with_state: Page, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Переход на страницу создания курсов
        chromium_page_with_state.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Загрузка картинки курса
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/robot.png")

        # Заполнение формы создания курса
        create_course_page.create_course_form.fill(title="Playwright",
                                                   estimated_time="2 weeks",
                                                   description="Playwright",
                                                   max_score="100",
                                                   min_score="10")

        # Нажатие кнопки создания курса
        create_course_page.check_course_toolbar.click_create_course_button()

        # Проверка корректности отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright",
                                                    max_score="100",
                                                    min_score="10",
                                                    estimated_time="2 weeks")

        # Через меню карточки курса нажимаем на кнопку "Edit"
        courses_list_page.view_menu.click_edit(index=0)

        # Изменение данных формы создания курса
        create_course_page.create_course_form.fill(title="PlaywrightTest",
                                                   estimated_time="2 weeks test",
                                                   description="Playwright test",
                                                   max_score="90",
                                                   min_score="20")

        # Нажатие кнопки создания курса
        create_course_page.check_course_toolbar.click_create_course_button()

        # Проверка корректности обновлённых отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(index=0,
                                                    title="PlaywrightTest",
                                                    max_score="90",
                                                    min_score="20",
                                                    estimated_time="2 weeks test")
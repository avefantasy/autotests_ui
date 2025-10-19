from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.navigation.navbar_component import NavbarComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent


# Page Object для проверки страницы создания курса
class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        # Создание заданий в курсе
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        # Проверка пустых блоков
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

        # Картинка предпросмотра и блок предпросмотра картинки курса
        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')

        # Заполнение формы создания курса.
        self.create_course_form = CreateCourseFormComponent(page)

        # Проверка корректность отображения панели управления
        self.check_course_toolbar = CreateCourseToolbarViewComponent(page)

        # Заголовок и кнопка создания задания
        self.create_course_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
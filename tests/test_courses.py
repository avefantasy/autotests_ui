from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    # Переход на страницу Courses
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия и текста заголовка "Courses"
    title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_have_text("Courses")

    # Проверка наличия и текста блока "There is no results"
    block_courses = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_courses).to_have_text("There is no results")

    # Проверка наличия и видимости иконки пустого блока
    icon_courses = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_courses).to_be_visible()

    # Проверка наличия и текста описания блока: "Results from the load test pipeline will be displayed here"
    description_block_courses = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_block_courses).to_have_text("Results from the load test pipeline will be displayed here")
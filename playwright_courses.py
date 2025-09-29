from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
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

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    # Переход на страницу Courses
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия и текста заголовка "Courses"
    title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_have_text("Courses")

    # Проверка наличия и текста блока "There is no results"
    block_courses = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_courses).to_have_text("There is no results")

    # Проверка наличия и видимости иконки пустого блока
    icon_courses = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_courses).to_be_visible()

    # Проверка наличия и текста описания блока: "Results from the load test pipeline will be displayed here"
    description_block_courses = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_block_courses).to_have_text("Results from the load test pipeline will be displayed here")

    # Задержка 5s
    page.wait_for_timeout(5000)
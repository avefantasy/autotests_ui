from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until='networkidle')

    # Ошибка - неправильный локатор
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    #Ошибка - неправильное взаимодействие с элементом
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    #Ошибка - DOM-дерево не успело прогрузиться
    page.evaluate("""
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = 'New Text';
        }
        """
    )

    # Задержка 5s
    page.wait_for_timeout(5000)
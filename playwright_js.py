from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ожидание полной загрузки страницы
    )

    # JS-код для замены текста заголовка
    new_text = 'New Text'
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = text;
        }
        """,
        new_text
    )
    page.wait_for_selector('#authentication-ui-course-title-text')

    # Задержка 5s
    page.wait_for_timeout(5000)
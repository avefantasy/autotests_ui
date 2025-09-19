from playwright.sync_api import sync_playwright, Request, Response

# Логирование запросов
def log_request(request: Request):
    print(f'Request: {request.url}')


# Логирование ответов
def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')


with sync_playwright() as playwright:
    #Открытие браузера и создание страницы
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу входа
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Обработчики событий
    page.on('request', log_request)
    #page.remove_listener('request', log_request)
    page.on('response', log_response)

    # Задержка 5s
    page.wait_for_timeout(5000)
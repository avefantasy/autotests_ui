from playwright.sync_api import Page, Locator, expect
import allure


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:  # Добавили свойство type_of
        return "base element"

    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавляем аргумент nth со значением по умолчанию 0
        locator = self.locator.format(**kwargs)
        with allure.step(f'Getting locator with "data-testid={locator}" at index "{nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)  # Теперь выбираем элемент по индексу

    def click(self,nth: int = 0, **kwargs):
        # "Лениво" инициализируем локатор
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            # Выполняем нажатие на элемент
            locator.click()

    def check_visible(self, nth: int = 0,  **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            # Инициализируем локатор "лениво"
            locator = self.get_locator(nth, **kwargs)
            # Проверяем, что элемент виден на странице
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            locator = self.get_locator(nth ,**kwargs)
            expect(locator).to_have_text(text)
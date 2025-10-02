import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные на сервер аналитики")
    #print("Данная фикстура будет запущена автоматически перед каждым автотестом")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотеста")
    #print("Данная фикстура будет запущена один раз на всю тестовую сессию")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаём данные пользователя один раз на тестовый класс")
    #print("Данная фикстура будет запущена на каждый тестовый класс")

@pytest.fixture()
def browser():
    print("[FUNCTION] Открываем браузер на каждый автотест")
    #print("Данная фикстура будет запущена на каждый автотест")

class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...
    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...
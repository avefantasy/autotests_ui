import allure

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass

def test_feature1():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")

def test_feature():
    with allure.step("Opening browser"):
        ...

    with allure.step("Creating course"):
        ...

    with allure.step("Closing browser"):
        ...
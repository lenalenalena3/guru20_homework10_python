import allure
from allure_commons.types import Severity
from selene import browser, be, have


def test1_allure_not():
    search_test = "lenalenalena3/lesson2_python"
    issues = 'Issues 2406'

    browser.open('https://github.com')
    browser.element('.search-input').should(be.visible).click()
    browser.element('#query-builder-test').should(be.visible).send_keys(search_test).press_enter()
    browser.element(f'a[href="/{search_test}"]').should(be.visible).click()
    browser.element('#issues-tab').should(be.visible).click()
    browser.element("#repository-input").should(have.value_containing("is:issue"))
    browser.element(f'//a[.="{issues}"]').should(be.visible)


def test2_allure_with():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label("owner", "tinkalyuk")
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Переход по ссылке репозитория")
    allure.dynamic.link("https://github.com", name="Testing")
    allure.dynamic.title("Переход по ссылке репозитория вариант 1 (with)")
    allure.dynamic.description("Тест c использованием with")
    allure.dynamic.epic("Эпик")

    search_test = "lenalenalena3/lesson2_python"
    issues = 'Issues 2406'

    with allure.step("Открываем главую страницу GitHub"):
        browser.open('https://github.com')
    with allure.step(f"Ищем репозиторий {search_test}"):
        browser.element('.search-input').should(be.visible).click()
        browser.element('#query-builder-test').should(be.visible).send_keys(search_test).press_enter()
    with allure.step(f"Переходим по ссылке репозитория {search_test}"):
        browser.element(f'a[href="/{search_test}"]').should(be.visible).click()
    with allure.step("Открываем вкладку Issue"):
        browser.element('#issues-tab').should(be.visible).click()
        browser.element("#repository-input").should(have.value_containing("is:issue"))
    with allure.step(f"На вкладке Issue проверяем, что есть {issues}"):
        browser.element(f'//a[.="{issues}"]').should(be.visible)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "tinkalyuk")
@allure.feature("Задачи в репозитории")
@allure.story("Переход по ссылке репозитория")
@allure.link("https://github.com", name="Testing")
@allure.title("Переход по ссылке репозитория вариант 2 (@allure.step)")
@allure.description("Тест с использованием @allure.step")
@allure.epic("Эпик")
def test3_allure_step():
    search_test = "lenalenalena3/lesson2_python"
    issues = 'Issues 2406'

    open_page()
    search(search_test)
    open_link(search_test)
    open_issues()
    should_issues(issues)


@allure.step("Открываем главую страницу GitHub")
def open_page():
    browser.open('https://github.com')


@allure.step("Ищем репозиторий {value}")
def search(value):
    browser.element('.search-input').should(be.visible).click()
    browser.element('#query-builder-test').should(be.visible).send_keys(value).press_enter()


@allure.step("Переходим по ссылке репозитория {value}")
def open_link(value):
    browser.element(f'a[href="/{value}"]').should(be.visible).click()


@allure.step("Открываем вкладку Issue")
def open_issues():
    browser.element('#issues-tab').should(be.visible).click()
    browser.element("#repository-input").should(have.value_containing("is:issue"))


@allure.step("На вкладке Issue проверяем, что есть {value}")
def should_issues(value):
    browser.element(f'//a[.="{value}"]').should(be.visible)
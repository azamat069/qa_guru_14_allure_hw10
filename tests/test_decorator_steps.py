import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Открываем строку поиска')
def open_search_field():
    browser.element('.header-search-button').click()


@allure.step('Вводим запрос поиска репозитория {repo_name}')
def search_repo(repo_name):
    browser.element('#query-builder-test').send_keys(repo_name).press_enter()


@allure.step('Переход в репозиторий {repo_name}')
def click_repo(repo_name):
    browser.element(by.link_text(repo_name)).click()


@allure.step('Переходим во вкладку Issues')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие issue с названием {issue_text}')
def should_see_issue(issue_text):
    browser.element(by.partial_text(issue_text)).should(be.visible)


def test_decorator_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Проверка наличия Issue в репозитории')
    allure.dynamic.link("https://github.com", name="Testing")
    open_main_page()
    open_search_field()
    search_repo('eroshenkoam/allure-example')
    click_repo('eroshenkoam/allure-example')
    open_issues_tab()
    should_see_issue('hello')

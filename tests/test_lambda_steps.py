import allure
from selene import browser, by, be


def test_with_allure_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    with allure.step('Открываем строку поиска'):
        browser.element('.header-search-button').click()

    with allure.step('Вводим запрос поиска репозитория'):
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step('Переход в репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переходим во вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие issue с названием hello'):
        browser.element(by.partial_text('hello')).should(be.visible)

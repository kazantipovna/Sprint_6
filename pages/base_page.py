from time import sleep

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.params import URLs


class BasePage:
    """Суперкласс базовой страницы, ее методы и кнопки есть на всех наследуемых"""

    def __init__(self, driver):
        self.driver = driver
        self.url = URLs.main_url

    @allure.step('Открываем страничку {url}')
    def open(self, url):
        """Открываем выбранную страничку"""
        self.driver.get(url)

    @allure.step('Получаем элемент {locator}')
    def get_web_element(self, locator):
        """Получаем необходимый веб элемент"""
        element = self.wait_for_element_is_visible(locator)
        self.scroll_to_web_element(element)
        return self.driver.find_element(*locator)

    @allure.step('Ждем элемент {locator}')
    def wait_for_element_is_visible(self, locator):
        """Ждун элемента"""
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Скроллим до элемента {web_element}')
    def scroll_to_web_element(self, web_element):
        """Скроллим до элемента"""
        self.driver.execute_script('arguments[0].scrollIntoView();', web_element)

    def wait_for_url(self, expected_url, attempts_count=20, attempt_timeout=0.3):
        """Ждет ссылку 20 раз по 0.3 секунды и возвращает её"""
        current_url = self.driver.current_url
        for _ in range(attempts_count):
            sleep(attempt_timeout)
            current_url = self.driver.current_url
            if expected_url in current_url:
                break
        return current_url

    # noinspection PyBroadException
    @staticmethod
    def click_web_element(web_element: WebElement, attempts_count: int = 10, attempts_timeout: float = 0.3):
        """
        Повторно кликает в элемент страницы, пока не кликнет успешно, иначе, через attempts_timeout,
         выдаст последнюю ошибку
        :param web_element: WebElement - вэб-элемент
        :param attempts_count: int - количество попыток
        :param attempts_timeout: float - таймаут между попытками
        :return: None
        """
        for i in range(attempts_count):
            try:
                web_element.click()
                break
            except Exception as last_exception:
                sleep(attempts_timeout)
                if i == attempts_count - 1:
                    raise last_exception

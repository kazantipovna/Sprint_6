from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageLocators:
    """Локаторы"""
    main_img = By.XPATH, './/img[@alt="Scooter"]'
    ya_img = By.XPATH, './/img[@alt="Yandex"]'
    cookie_btn = By.XPATH, "//button[text()='да все привыкли']"


class BasePage:
    """Суперкласс базовой страницы, ее методы есть на всех наследуемых"""

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://qa-scooter.praktikum-services.ru/'
        self.locators = None

    @allure.step('Открываем страничку и принимаем куки')
    def open(self):
        """Открываем страничку и принимаем куки"""
        self.driver.get(self.url)
        try:
            self.cookie_btn.click()
        except:
            pass

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

    @property
    def main_img(self):
        """Возвращаем логотип "Самокат" """
        return self.get_web_element(BasePageLocators.main_img)

    @property
    def ya_img(self):
        """Возвращаем логотип "Яндекс" """
        return self.get_web_element(BasePageLocators.ya_img)

    @property
    def cookie_btn(self):
        """Возвращаем кнопку для принятия куки """
        return self.get_web_element(BasePageLocators.cookie_btn)

    def wait_for_url(self, expected_url, attempts_count=20, attempt_timeout=0.3):
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

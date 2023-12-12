import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage, BasePageLocators


class MainPageLocators(BasePageLocators):
    """Класс локаторов"""
    def __init__(self):
        super().__init__()
        self.order_top_btn = By.XPATH, "(//button[text()='Заказать'])[1]"
        self.order_bottom_btn = By.XPATH, "(//button[text()='Заказать'])[2]"
        self.main_header = By.CLASS_NAME, 'Home_Header__iJKdX'


class MainPage(BasePage):
    """Класс основной страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://qa-scooter.praktikum-services.ru/'
        self.locators = MainPageLocators()

    @property
    def order_top_btn(self):
        """Возвращаем верхнюю кнопку "Заказать" """
        return self.get_web_element(self.locators.order_top_btn)

    @property
    def order_bottom_btn(self):
        """Возвращаем нижнюю кнопку "Заказать" """
        return self.get_web_element(self.locators.order_bottom_btn)

    @property
    def main_header(self):
        """Возвращаем заголовок главной страницы """
        return self.get_web_element(self.locators.main_header)

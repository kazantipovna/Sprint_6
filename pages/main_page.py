from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.params import URLs


class MainPageLocators:
    """Класс локаторов"""
    order_top_btn = By.XPATH, "(//button[text()='Заказать'])[1]"
    order_bottom_btn = By.XPATH, "(//button[text()='Заказать'])[2]"
    main_header = By.CLASS_NAME, 'Home_Header__iJKdX'
    main_img = By.XPATH, './/img[@alt="Scooter"]'
    ya_img = By.XPATH, './/img[@alt="Yandex"]'


class MainPage(BasePage):
    """Класс основной страницы"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = URLs.main_url
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

    @property
    def main_img(self):
        """Возвращаем логотип "Самокат" """
        return self.get_web_element(self.locators.main_img)

    @property
    def ya_img(self):
        """Возвращаем логотип "Яндекс" """
        return self.get_web_element(self.locators.ya_img)

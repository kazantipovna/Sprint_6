import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators


class OrderForWhoPageLocators(BasePageLocators):
    """Класс локаторов"""
    def __init__(self):
        super().__init__()
        self.order_btn = By.XPATH, "//button[contains(text(), 'Заказать')]"
        self.form_title = By.XPATH, "//div[contains(text(), 'Для кого самокат')]"
        self.name = By.XPATH, './/input[@placeholder="* Имя"]'
        self.surname = By.XPATH, './/input[@placeholder="* Фамилия"]'
        self.address = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
        self.station = By.XPATH, './/input[@placeholder="* Станция метро"]'
        self.phone = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'
        self.next_btn = By.XPATH, "//button[contains(text(), 'Далее')]"


class OrderForWhoPage(BasePage):
    """Класс странички заказа с формой "Для кого" """

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://qa-scooter.praktikum-services.ru/order'
        self.locators = OrderForWhoPageLocators()

    @property
    def order_btn(self):
        """Возвращаем кнопку "Заказать" """
        return self.get_web_element(self.locators.order_btn)

    @property
    def next_btn(self):
        """Возвращаем кнопку "Далее" """
        return self.get_web_element(self.locators.next_btn)

    @property
    def form_title(self):
        """Возвращаем заголовок формы "Для кого" """
        return self.get_web_element(self.locators.form_title)

    @property
    def name(self):
        """Возвращаем поле "Имя" в форме "Для кого" """
        return self.get_web_element(self.locators.name)

    @property
    def surname(self):
        """Возвращаем поле "Фамилия" в форме "Для кого" """
        return self.get_web_element(self.locators.surname)

    @property
    def address(self):
        """Возвращаем поле "Адрес" в форме "Для кого" """
        return self.get_web_element(self.locators.address)

    @property
    def station(self):
        """Возвращаем поле "Станция метро" в форме "Для кого" """
        return self.get_web_element(self.locators.station)

    @allure.step('Находим и выбираем станцию {station_name} из выпадашки в форме "Для кого"')
    def set_station(self, station_name):
        """Находим и выбираем станцию из выпадашки"""
        self.station.send_keys(station_name)
        self.station.send_keys(Keys.DOWN)
        self.station.send_keys(Keys.ENTER)

    @property
    def phone(self):
        """Возвращаем поле "Номер телефона в форме "Для кого" """
        return self.get_web_element(self.locators.phone)

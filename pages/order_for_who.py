import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.params import URLs


class OrderForWhoPageLocators:
    """Класс локаторов"""
    order_btn = By.XPATH, "//button[contains(text(), 'Заказать')]"
    form_title = By.XPATH, "//div[contains(text(), 'Для кого самокат')]"
    name = By.XPATH, './/input[@placeholder="* Имя"]'
    surname = By.XPATH, './/input[@placeholder="* Фамилия"]'
    address = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    station = By.XPATH, './/input[@placeholder="* Станция метро"]'
    phone = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'
    next_btn = By.XPATH, "//button[contains(text(), 'Далее')]"


class OrderForWhoPage(BasePage):
    """Класс странички заказа с формой "Для кого" """

    def __init__(self, driver):
        super().__init__(driver)
        self.url = URLs.order_url
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

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_form_for_who(self, name, surname, address, station, phone):
        self.name.send_keys(name)
        self.surname.send_keys(surname)
        self.address.send_keys(address)
        self.set_station(station)
        self.phone.send_keys(phone)
        self.next_btn.click()

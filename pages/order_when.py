import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.params import URLs


class OrderWhenPageLocators:
    """Класс локаторов"""
    when_date = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]'
    rent_term = By.XPATH, '//*[text()="* Срок аренды"]'
    rent_term_item = By.XPATH, "//div[@class='Dropdown-menu']//div[text()='{}']"
    black_check = By.ID, 'black'
    gray_check = By.ID, 'grey'
    comment = By.XPATH, './/input[@placeholder="Комментарий для курьера"]'
    order_btn = By.XPATH, '(//button[text()="Заказать"])[2]'
    form_title = By.CLASS_NAME, 'Order_Header__BZXOb'
    approve_form = By.XPATH, '//div[text()="Хотите оформить заказ?"]'
    yes_bnt = By.XPATH, '(//button[text()="Да"])'
    order_done = By.XPATH, '//div[text()="Заказ оформлен"]'
    view_status_btn = By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"


class OrderWhenPage(BasePage):
    """Класс странички заказа с формой "Про аренду" """

    def __init__(self, driver):
        super().__init__(driver)
        self.url = URLs.order_url
        self.locators = OrderWhenPageLocators()

    @property
    def when_date(self):
        """Возвращаем поле ввода даты аренды"""
        return self.get_web_element(self.locators.when_date)

    @allure.step('Жмем кнопку Enter, чтобы дата ввелась')
    def set_when_date(self, when_date):
        """Жмем кнопку Enter, чтобы дата ввелась"""
        self.when_date.send_keys(when_date)
        self.when_date.send_keys(Keys.ENTER)

    @property
    def rent_term(self):
        """Возвращаем поле ввода срока аренды"""
        return self.get_web_element(self.locators.rent_term)

    @allure.step('Активируем выпадашку срока аренды: {rent_term}')
    def rent_term_item(self, rent_term):
        """Активируем выпадашку срока аренды"""
        selector_type, selector = self.locators.rent_term_item
        return self.get_web_element((selector_type, selector.format(rent_term)))

    @allure.step('Кликаем выбранный срок аренды в выпадашке: {rent_term}')
    def set_rent_term(self, rent_term):
        """Кликаем выбранный срок аренды в выпадашке"""
        self.rent_term.click()
        self.rent_term_item(rent_term).click()

    @property
    def black_check(self):
        """Возвращаем чекбокс черного"""
        return self.get_web_element(self.locators.black_check)

    @property
    def gray_check(self):
        """Возвращаем чекбокс серого"""
        return self.get_web_element(self.locators.gray_check)

    @allure.step('Выбираем цвет самоката: {color}')
    def color(self, color):
        """Выбираем чекбокс в зависимости от цвета"""
        if color == 'серая безысходность':
            return self.gray_check
        elif color == 'чёрный жемчуг':
            return self.black_check
        else:
            return None

    @property
    def comment(self):
        """Возвращаем поле комментария"""
        return self.get_web_element(self.locators.comment)

    @property
    def order_btn(self):
        """Возвращаем кнопку "Заказать" """
        return self.get_web_element(self.locators.order_btn)

    @property
    def approve_form(self):
        """Возвращаем форму подтверждения заказа"""
        return self.get_web_element(self.locators.approve_form)

    @property
    def form_title(self):
        """Возвращаем заголовок формы"""
        return self.get_web_element(self.locators.form_title)

    @property
    def yes_bnt(self):
        """Возвращаем кнопку "Да" из формы подтверждения заказа"""
        return self.get_web_element(self.locators.yes_bnt)

    @property
    def order_done(self):
        """Возвращаем форму "Заказ Оформлен" """
        return self.get_web_element(self.locators.order_done)

    @property
    def view_status_btn(self):
        """Возвращаем кнопку "Посмотреть статус" """
        return self.get_web_element(self.locators.view_status_btn)

    @allure.step('Заполняем форму "Про аренду"')
    def fill_form_when(self, date, term, color, comment):
        self.set_when_date(date)
        self.set_rent_term(term)
        self.color(color).click()
        self.comment.send_keys(comment)
        self.order_btn.click()

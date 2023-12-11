import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators


class QuestionPageLocators(BasePageLocators):
    def __init__(self):
        """Локаторы"""
        super().__init__()
        self.FAQ_panel = By.CLASS_NAME, 'Home_FAQ__3uVm4'
        self.FAQ_question = By.ID, 'accordion__heading-{}'
        self.FAQ_answer = By.ID, 'accordion__panel-{}'


class QuestionPage(BasePage):
    """Класс странички с вопросами"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://qa-scooter.praktikum-services.ru/'
        self.locators = QuestionPageLocators()

    @allure.step('Находим вопрос по его номеру, зашитому в локатор')
    def get_question_by_number(self, question_number):
        """Находим вопрос по его номеру"""
        locator_type, locator_selector = self.locators.FAQ_question
        locator = locator_type, locator_selector.format(question_number)
        self.wait_for_element_is_visible(locator)
        return self.driver.find_element(*locator)

    @allure.step('Находим ответ по номеру вопроса')
    def get_answer_by_number(self, question_number):
        """Находим ответ по номеру вопроса"""
        locator_type, locator_selector = self.locators.FAQ_answer
        locator = locator_type, locator_selector.format(question_number)
        self.wait_for_element_is_visible(locator)
        return self.driver.find_element(*locator)

    @allure.step('Скроллим до блока с вопросами')
    def scroll_to_faq(self):
        """Скроллим до блока с вопросами,
        открыть страничку и скролл до вопросов в отдельном методе в этом случае работает очень сильно быстрее,
        чем если писать это в мясе теста"""
        self.driver.get(self.url)
        faq_element = self.driver.find_element(*self.locators.FAQ_panel)
        self.scroll_to_web_element(faq_element)

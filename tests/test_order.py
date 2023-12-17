import allure
import pytest
from pages.main_page import MainPage
from pages.order_for_who import OrderForWhoPage
from pages.order_when import OrderWhenPage
from tests.params import URLs
from tests.params.data_order import ORDERS_DATA


class TestOrder:
    @allure.title('Проверка заказа самоката')
    @allure.description('Положительный сценарий проверки заказа самоката с верхней и нижней кнопок')
    @pytest.mark.parametrize('order_params', ORDERS_DATA)
    def test_order_scooter(self, driver, order_params):
        """Тест на проверку заказа самоката"""
        with allure.step('Открываем главную страницу в браузере:'):
            main_page = MainPage(driver)
            main_page.open(URLs.main_url)

        with allure.step(f'Запускаем тест на проверку заказа самоката с кнопки {order_params["order_button"]}:'):
            # noinspection PyTypeChecker
            order_btn = getattr(main_page, order_params['order_button'])
            main_page.click_web_element(order_btn)

        with allure.step(f'Заполняем форму "Для кого":'):
            order_for_who_page = OrderForWhoPage(driver)
            order_for_who_page.fill_form_for_who(order_params['name'], order_params['surname'], order_params['address'],
                                                 order_params['station'], order_params['phone'])

        with allure.step(f'Заполняем форму "Про аренду":'):
            order_when_page = OrderWhenPage(driver)
            order_when_page.fill_form_when(order_params['date'], order_params['term'], order_params['color'],
                                           order_params['comment'])

        with allure.step(f'Подтверждаем заказ:'):
            order_when_page.yes_bnt.click()
            expected_form_title = 'Заказ оформлен'
            assert expected_form_title in order_when_page.order_done.text, \
                f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'

    @allure.title('Проверка кнопки "Самокат"')
    @allure.description('Проверка перехода по кнопке "Самокат" на главную страницу')
    def test_logo_button(self, driver):
        with allure.step('Открываем страницу регистрации в браузере:'):
            main_page = MainPage(driver)
            main_page.open(URLs.order_url)

        with allure.step(f'Переходим на главную страницу через кнопку "Самокат":'):
            main_page.click_web_element(main_page.main_img)
            expected_form_title = 'пару дней'
            assert expected_form_title in main_page.main_header.text, \
                f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'

    @allure.title('Проверка кнопки "Яндекс"')
    @allure.description('Проверка перехода по кнопке "Яндекс" на "Дзен"')
    def test_dzen_button(self, driver):
        with allure.step('Открываем главную страницу в браузере:'):
            main_page = MainPage(driver)
            main_page.open(URLs.main_url)

        with allure.step('Переходим на "Дзен":'):
            main_page.click_web_element(main_page.ya_img)
            expected_url = 'https://dzen.ru/?yredirect=true'
            main_page.driver.switch_to.window(main_page.driver.window_handles[1])
            assert main_page.wait_for_url(expected_url) == expected_url, f'Ошибка: переход на "Дзен" не осуществлен'

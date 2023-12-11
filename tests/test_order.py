import allure
import pytest

from pages.main_page import MainPage
from pages.order_for_who import OrderForWhoPage
from pages.order_when import OrderWhenPage
from tests.params.data_order import ORDERS_DATA


class TestOrder:
    @allure.title('Проверка заказа самоката')
    @allure.description('Положительный сценарий проверки заказа самоката с верхней и нижней кнопок')
    @pytest.mark.parametrize('order_params', ORDERS_DATA)
    def test_order_scooter(self, driver, order_params):
        """Тест на проверку заказа самоката"""
        with allure.step('Открываем главную страницу в браузере:'):
            main_page = MainPage(driver)
            main_page.open()

        with allure.step(f'Запускаем тест на проверку заказа самоката с кнопки {order_params["order_button"]}:'):
            # noinspection PyTypeChecker
            order_btn = getattr(main_page, order_params['order_button'])
            main_page.click_web_element(order_btn)

            order_for_who_page = OrderForWhoPage(driver)
            expected_form_title = 'Для кого самокат'
            assert expected_form_title in order_for_who_page.form_title.text, \
                f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'

        with allure.step(f'Заполняем форму "Для кого":'):
            order_for_who_page.name.send_keys(order_params['name'])
            order_for_who_page.surname.send_keys(order_params['surname'])
            order_for_who_page.address.send_keys(order_params['address'])
            order_for_who_page.set_station(order_params['station'])
            order_for_who_page.phone.send_keys(order_params['phone'])
            order_for_who_page.next_btn.click()

            order_when_page = OrderWhenPage(driver)
            expected_form_title = 'Про аренду'
            assert expected_form_title in order_when_page.form_title.text, \
                f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'

        with allure.step(f'Заполняем форму "Про аренду":'):
            order_when_page.set_when_date(order_params['date'])
            order_when_page.set_rent_term(order_params['term'])
            order_when_page.color(order_params['color']).click()
            order_when_page.comment.send_keys(order_params['comment'])
            order_when_page.order_btn.click()

            expected_form_title = 'Хотите оформить заказ?'
            assert expected_form_title in order_when_page.approve_form.text, \
                f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'

        with allure.step(f'Подтверждаем заказ:'):
            order_when_page.yes_bnt.click()

        with allure.step(f'Получаем сообщение с подтверждением заказа:'):
            expected_form_title = 'Заказ оформлен'
            assert expected_form_title in order_when_page.order_done.text, \
                f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'

        with allure.step(f'Переходим в статус заказа после его оформления:'):
            order_when_page.view_status_btn.click()

        with allure.step(f'Переход на страницу через кнопку "{order_params["logo_button"]}":'):
            if order_params["logo_button"] == 'main_img':
                main_page.click_web_element(main_page.main_img)
                expected_form_title = 'пару дней'
                assert expected_form_title in main_page.main_header.text, \
                    f'Ошибка: заголовок не соответствует заданному: {expected_form_title}'
            else:
                main_page.click_web_element(main_page.ya_img)
                expected_url = 'https://dzen.ru/?yredirect=true'
                main_page.driver.switch_to.window(main_page.driver.window_handles[1])
                assert main_page.wait_for_url(expected_url) == expected_url, f'Ошибка: переход на дзен не осуществлен'

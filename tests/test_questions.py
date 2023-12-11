import allure

from pages.question_page import QuestionPage
from tests.params import data_questions
import pytest


class TestFAQ:
    @allure.title('Проверка аккордеона FAQ')
    @allure.description('Тест проверки корректности ответа на вопрос по номеру вопроса')
    @pytest.mark.parametrize('question_num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question(self, driver, question_num):
        """Тест проверки корректности ответа на вопрос по номеру вопроса (номер вопроса и ответа зашиты в локаторах)"""
        question_page = QuestionPage(driver)
        question_page.scroll_to_faq()
        question_page.click_web_element(question_page.get_question_by_number(question_num))

        question_answer = question_page.get_answer_by_number(question_num).text
        expected_answer = data_questions.text_check[question_num]
        assert expected_answer == question_answer, f'Ошибка: текст не соответствует заданному: {expected_answer}'

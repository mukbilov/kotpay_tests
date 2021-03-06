from pages.pay_page import PayPage
import pytest


class TestPayPage:
    def test_check_page_elements(self, browser, link):  # RTM-91 Проверка элементов платежной страницы покупателя
        PayPage(browser, link+"?order=123")\
            .open()\
            .check_page_elements()

    def test_check_card_number_input(self, browser, link):  # RTM-92 Проверка поля ввода номера карты
        PayPage(browser, link + '?order=112')\
            .check_card_number_input()

    def test_check_card_user_input(self, browser, link):  # RTM-97 Проверка поля ввода данных держателя карты
        PayPage(browser, link + '?order=112')\
            .check_user_name_input()

    def test_check_card_date_input(self, browser, link):  # RTM-93 Проверка поля ввода срока действия карты
        PayPage(browser, link)\
            .check_card_month_input()\
            .check_card_year_input()

    def test_check_cvc_input(self, browser, link):  # RTM-94 Проверка поля ввода CVC
        PayPage(browser, link)\
            .check_cvc_input()

    def test_check_success_page(self, browser, link):
        PayPage(browser, link + '?orderId=123')\
            .open()\
            .check_success_page_elements()

    def test_check_unsuccess_page(self, browser, link):
        PayPage(browser, link + '?orderId=')\
            .open()\
            .check_success_page_elements()

    def test_check_pay_button(self, browser, link):  # RTM-96 Проверка активации кнопки "Оплатить"
        PayPage(browser, link)\
            .open()\
            .check_pay_button()

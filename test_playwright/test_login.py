import allure

from data import card_number, card_expire_date, card_cvc, user_first_name, user_last_name, user_email
from pages.main_page import MainPage
from pages.start_page import StartPage


class TestLogin:

    @allure.title('Test unsuccessful donate')
    @allure.description('Test unsuccessful donate using wrong credit card data')
    def test_unsuccessful_donate(self, page):
        start_page = StartPage(page)
        main_page = MainPage(page)

        start_page.navigate()
        start_page.click_give_now_button()
        main_page.choose_monthly_donate()
        main_page.enter_donation_amount(100, 'USD')
        main_page.click_donate_monthly_button()
        main_page.uncheck_cover_transaction_costs()
        main_page.click_pay_by_credit_card()
        main_page.enter_card_data(card_number, card_expire_date, card_cvc)
        main_page.click_card_continue_button()
        main_page.enter_user_data(user_first_name, user_last_name, user_email)
        main_page.click_donate()
        main_page.check_error_message_cc()

    @allure.title('Test unsuccessful donate 2')
    @allure.description('Test unsuccessful donate using wrong credit card data (for the second time :))')
    def test_unsuccessful_donate_2(self, page):
        start_page = StartPage(page)
        main_page = MainPage(page)

        start_page.navigate()
        start_page.click_give_now_button()
        main_page.choose_monthly_donate()
        main_page.enter_donation_amount(100, 'USD')
        main_page.click_donate_monthly_button()
        main_page.uncheck_cover_transaction_costs()
        main_page.click_pay_by_credit_card()
        main_page.enter_card_data(card_number, card_expire_date, card_cvc)
        main_page.click_card_continue_button()
        main_page.enter_user_data(user_first_name, user_last_name, user_email)
        main_page.click_donate()
        main_page.check_error_message_cc()

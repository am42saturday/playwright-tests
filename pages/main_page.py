import allure
from playwright.sync_api import expect


class MainPage:
    def __init__(self, page):
        self.page = page

    @property
    def donation_iframe(self):
        return self.page.wait_for_selector('[title="Donation Widget"]').content_frame()

    @property
    def card_number_input_iframe(self):
        return self.donation_iframe.wait_for_selector('[title="Secure card number input frame"]').content_frame()

    @property
    def exp_date_input_iframe(self):
        return self.donation_iframe.wait_for_selector('[title="Secure expiration date input frame"]').content_frame()

    @property
    def cvc_input_iframe(self):
        return self.donation_iframe.wait_for_selector('[title="Secure CVC input frame"]').content_frame()

    @property
    def choose_monthly_donate_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=give-monthly]')

    @property
    def amount_input_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=amount]')

    @property
    def amount_currency_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=currency-selector]')

    @property
    def donate_monthly_button_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=donate-button]')

    @property
    def cover_transaction_costs_checkbox_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=cover-fee-checkbox]')

    @property
    def pay_by_credit_card_button_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=cc-button]')

    @property
    def cc_number_input_locator(self):
        return self.card_number_input_iframe.wait_for_selector('[name=cardnumber]')

    @property
    def cc_expiration_date_input_locator(self):
        return self.exp_date_input_iframe.wait_for_selector('[name=exp-date]')

    @property
    def cc_cvc_input_locator(self):
        return self.cvc_input_iframe.wait_for_selector('[name=cvc]')

    @property
    def card_continue_button_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=card-continue]')

    @property
    def first_name_input_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=personal-first-name]')

    @property
    def last_name_input_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=personal-last-name]')

    @property
    def email_input_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=personal-email]')

    @property
    def donate_button_locator(self):
        return self.donation_iframe.wait_for_selector('[data-qa=privacy-continue]')

    @property
    def error_message_locator(self):
        return self.donation_iframe.locator('[data-qa=card-continue-error-title]')

    @allure.step('Choose monthly donate')
    def choose_monthly_donate(self):
        self.choose_monthly_donate_locator.click()

    @allure.step('Enter donation amount')
    def enter_donation_amount(self, amount, currency):
        self.amount_input_locator.fill(str(amount))
        self.amount_currency_locator.select_option(currency)

    @allure.step('Click Donate Monthly button')
    def click_donate_monthly_button(self):
        self.donate_monthly_button_locator.click()

    @allure.step('Uncheck Cover transaction costs checkbox')
    def uncheck_cover_transaction_costs(self):
        self.cover_transaction_costs_checkbox_locator.click()

    @allure.step('Choose Pay by credit card')
    def click_pay_by_credit_card(self):
        self.pay_by_credit_card_button_locator.click()

    @allure.step('Enter user card data')
    def enter_card_data(self, number, date, cvc):
        self.cc_number_input_locator.fill(number)
        self.cc_expiration_date_input_locator.fill(date)
        self.cc_cvc_input_locator.fill(cvc)

    @allure.step('Click Continue Button')
    def click_card_continue_button(self):
        self.card_continue_button_locator.click()

    @allure.step('Enter user data')
    def enter_user_data(self, first_name, last_name, email):
        self.first_name_input_locator.fill(first_name)
        self.last_name_input_locator.fill(last_name)
        self.email_input_locator.fill(email)

    @allure.step('Click Donate')
    def click_donate(self):
        self.donate_button_locator.click()

    @allure.step('Check Error message on credit card form')
    def check_error_message_cc(self):
        expect(self.donation_iframe.locator('[data-qa=active-screen-credit-card]')).to_be_visible()
        expect(self.error_message_locator).to_have_text("Your card was declined.", timeout=5000)

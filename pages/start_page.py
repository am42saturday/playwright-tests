import allure
from data import BASE_URL


class StartPage:
    def __init__(self, page):
        self.page = page

    @property
    def donate_button_iframe(self):
        return self.page.wait_for_selector('[title="Donate Button"]').content_frame()

    @property
    def give_now_button_locator(self):
        return self.donate_button_iframe.wait_for_selector('[qa=fun-element]')

    @allure.step('Open Start Page')
    def navigate(self):
        self.page.goto(BASE_URL)

    @allure.step('Click Give Now Button')
    def click_give_now_button(self):
        self.give_now_button_locator.click()


from pageObject.meals_pricing_page import MealsPricingPage
from utils.logger import log_decorator


class MealsPricingHandler(MealsPricingPage):
    def __init__(self):
        super(MealsPricingHandler, self).__init__()

    @log_decorator
    def click_clear_machine_loc(self):
        self.clear_machine_loc().click()

    @log_decorator
    def click_clear_machine_yes_lco(self):
        self.clear_machine_yes_loc().clicik()

    @log_decorator
    def click_clear_machine_no_lco(self):
        self.clear_machine_no_loc().clicik()
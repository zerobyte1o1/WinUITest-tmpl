from pageObject.home_page import HomePage
from utils.logger import log_decorator


class HomeHandler(HomePage):
    """
    home页面的操作
    """

    def __init__(self):
        super().__init__()

    @log_decorator
    def click_meals_pricing_loc(self):
        self.meals_pricing_loc().click()

    @log_decorator
    def click_meals_management_loc(self):
        self.meals_management_loc().click()

    @log_decorator
    def click_revenue_analysis_loc(self):
        self.revenue_analysis_loc().click()

    @log_decorator
    def click_member_management_loc(self):
        self.member_management_loc().click()

    @log_decorator
    def click_setting_loc(self):
        self.setting_loc().click()

    @log_decorator
    def click_min_loc(self):
        self.min_loc().click()

    @log_decorator
    def click_close_loc(self):
        self.close_loc().click()


if __name__ == '__main__':
    HomeHandler().click_meals_pricing_loc()

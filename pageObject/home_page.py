from pageObject.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        pass

    def get_meals_procing_loc(self):
        return self.locate_element(best_match='菜品计价')

    def get_meals_management_loc(self):
        return self.locate_element(best_match='菜品管理')
    def get_revenue_analysis_loc(self):
        return self.locate_element(best_match='')


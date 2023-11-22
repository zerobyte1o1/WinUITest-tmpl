from pageObject.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        pass

    def get_mals_procing_loc(self):
        return self.locate_element('best_match','菜品计价')

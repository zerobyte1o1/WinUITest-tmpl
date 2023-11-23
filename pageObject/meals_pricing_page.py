from pageObject.base_page import BasePage


class MealsPricingPage(BasePage):
    def __init__(self):
        super(MealsPricingPage, self).__init__()

    def order_mgr_loc(self):
        return self.locate_element(title='订单')

    def food_management_loc(self):
        return self.locate_element(title='菜品')

    def clear_machine_loc(self):
        return self.locate_element(title='清机')

    def clear_machine_yes_loc(self):
        return self.locate_element(auto_id='PageBase.widgetMain.CashierWidget.SFMessageForm.btnOk')

    def clear_machine_no_loc(self):
        return self.locate_element(auto_id='PageBase.widgetMain.CashierWidget.SFMessageForm.btnCancel')
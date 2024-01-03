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

    def digital_selection_loc(self):
        return self.locate_element(title="数字点选")

    def drink_loc(self):
        return self.locate_element(title="酒水饮料")

    def non_standard_loc(self):
        return self.locate_element(title="非标品")

    def calculation_loc(self, digit: str):
        """
        定位数字键盘输入
        :param digit:str
        :return:
        """
        return self.locate_element(title=digit)

    def reidentify_loc(self):
        return self.locate_element(title="重新识别")

    def merged_payment_loc(self):
        return self.locate_element(title="合并支付")

    def auto_payment_loc(self):
        return self.locate_element(title="自动支付")

    def cash_payment_loc(self):
        return self.locate_element(title="现金支付")

    def cooperative_payment_loc(self):
        return self.locate_element(title="合作支付")

    def hanging_orders_loc(self):
        return self.locate_element(title="挂起订单")

    def cancel_payment_loc(self):
        return self.locate_element(title="取消支付")

    def identification_of_areas(self):
        return self.locate_element(auto_id="")

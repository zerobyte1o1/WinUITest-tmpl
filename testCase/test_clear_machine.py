from handlers.meals_pricing_handler import MealsPricingHandler
import allure
import pytest


@allure.epic("清机功能测试")
@allure.feature("场景：操作清机功能")
class TestClearMachine:
    def setup_class(self):
        self.mph = MealsPricingHandler()

    def teardown_class(self):
        self.mph.driver.kill()

    @allure.story("用例-操作并确定清机")
    @allure.title("请求登出接口")
    @allure.description("该用例检查用户登出操作")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.p0
    def test_clear_machine_forward(self):
        with allure.step('点击清机按钮'):
            self.mph.click_clear_machine_loc()
        with allure.step('点击确定'):
            self.mph.clear_machine_yes_loc()

    def test_clear_machine_reverse(self):
        pass

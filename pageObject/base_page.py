from utils.driver_factory import DriverFactory


class BasePage:
    def __init__(self):
        """
        单例模式
        """
        if DriverFactory.driver is None:
            DriverFactory.get_driver()
        self.driver = DriverFactory.driver
        self.log = DriverFactory.log

    def locate_element(
            self,
            class_name=None,
            class_name_re=None,
            title=None,
            title_re=None,
            control_type=None,
            best_match=None,
            auto_id=None):
        """
        封装所有pywinauto定位元素的方法\n
        class_name=None, # 类名\n
        class_name_re=None, # 正则匹配类名\n
        title=None, # 控件的标题文字，对应inspect中Name字段\n
        title_re=None, # 正则匹配文字\n
        control_type=None, # 控件类型，inspect界面LocalizedControlType字段的英文名\n
        best_match=None, #\n
        auto_id=None, # 这个也是固定的可以用，inspect界面AutomationId字段，但是很多控件没有这个属性
        """

        try:
            element = self.driver.window(class_name=class_name,
                                         class_name_re=class_name_re,
                                         title=title,
                                         title_re=title_re,
                                         control_type=control_type,
                                         best_match=best_match,
                                         auto_id=auto_id)
        except Exception as e:
            element = None
            self.log.info(e)
            self.log.error("元素定位输入有误")
        return element


if __name__ == '__main__':
    BasePage()

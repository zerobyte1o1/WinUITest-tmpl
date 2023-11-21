from utils.driver_factory import DriverFactory


class BasePage:
    def __init__(self):
        """
        单例模式
        """
        if DriverFactory.driver is None:
            DriverFactory.get_driver()
        else:
            self.driver=DriverFactory.driver


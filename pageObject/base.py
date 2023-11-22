from utils.driver_factory import DriverFactory


class Base:
    def __init__(self):
        """
        单例模式
        """
        if DriverFactory.driver is None:
            DriverFactory.get_driver()
        else:
            self.driver=DriverFactory.driver

    def locate_element(self, type,locator):
        """
        封装所有pywinauto定位元素的方法
        """
        if type=='name':
            element = self.driver.window(best_match=locator)
            
        
        return element


if __name__ == '__main__':
    Base().locate_element('name','菜品计价')
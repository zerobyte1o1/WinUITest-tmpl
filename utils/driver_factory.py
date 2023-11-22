from pywinauto import Application

from utils.env import Environment


class DriverFactory:
    # 静态属性
    driver = None

    @classmethod
    def get_driver(cls, **kwargs):
        env = Environment()
        app = Application(env.get_type()).start(env.get_location())
        cls.driver = app[env.get_app_name()]


if __name__ == '__main__':
    DriverFactory.get_driver()

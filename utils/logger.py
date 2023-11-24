import logging, time, os

from pywinauto.findwindows import ElementNotFoundError

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        Logger().logger.info(f"Executing function: {func.__name__}")
        try:
            result = func(*args, **kwargs)
        except ElementNotFoundError as e:
            Logger().logger.error(f"Function {func.__name__} executed Failed, Element not found")
        return result
    return wrapper


if __name__ == '__main__':
    logger = Logger().logger
    logger.info("---测试开始---")
    logger.debug("---测试结束---")

import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(BASE_DIR, "../config/env.ini")
cf = configparser.ConfigParser()
cf.read(configPath, encoding='UTF-8')
pick = cf.get("pick", "env")
type = cf.get(pick, "type")
location = cf.get(pick, "location")
app_name = cf.get(pick, "appName")


class Environment:

    def get_type(self):
        return type

    def get_location(self):
        return location

    def get_app_name(self):
        return app_name


if __name__ == "__main__":
    env = Environment()
    # print(env.url(module="flow"))
    print(env.get_location())
    # print(account, password)

import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(BASE_DIR, "../config/env.ini")
cf = configparser.ConfigParser()
cf.read(configPath, encoding='UTF-8')
type = cf.get('test', "type")
location = cf.get('test', "location")
app_name = cf.get('test', "appName")


class Environment:

    def get_type(self):
        return type

    def get_location(self):
        return location

    def get_app_name(self):
        return app_name

    # def get_jenkins_url(self):
    #     return cf.get('jenkins', 'jenkins_url')
    #
    # def get_jenkins_user(self):
    #     return cf.get('jenkins', 'user')
    #
    # def get_jenkins_password(self):
    #     return cf.get('jenkins', 'password')
    #
    def get_report_url(self):
        return cf.get('wechat', 'report_url')

    def get_info_url(self):
        return cf.get('wechat', 'info_url')

    def get_listen_file(self):
        return cf.get('wechat', 'listen_file')


env = Environment()
if __name__ == "__main__":
    # print(env.url(module="flow"))
    print(env.get_location())
    # print(account, password)

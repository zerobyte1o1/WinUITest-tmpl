from utils.env import env
from utils.logger import log
import requests
import os


def send_wechat_message():
    try:
        with open(env.get_listen_file(), "r") as file:
            version = file.readline().strip()
    except FileNotFoundError:
        log.warning("no listen file")

    _directory = os.getcwd()
    result_file = os.path.join(_directory, "result.txt")

    with open(result_file, "r") as fp:
        lines = fp.readlines()
        if lines[5].split("=")[1].strip() == "100%":
            title = "<font  color=\"info\">通过</font>"
        else:
            title = "<font  color=\"warning\">未通过</font>"
        content = ""
        for line in lines:
            content += "" + line.strip() + " \n"

    content = "<font color=\"comment\">" + version + "自动化测试</font>" + title + "\n >[详细报告](" + env.get_report_url() + "\\" + version + "\\complete.html"")\n" + content
    body = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    try:
        response = requests.post(env.get_info_url(), json=body, headers=headers)
        log.info(response.text)
    except Exception as e:
        log.warning("发送企业微信消息出错" + e)
    # print(response.status_code)
    # print(response.content)
    # print(response.text)

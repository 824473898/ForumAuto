import os
import configparser
from selenium import webdriver
import time


# class BrowserEngine(object):
#     #
#     # def __init__(self, driver):
#     #     self.driver = driver
#
#     #  read the browser type from config.ini file, return the driver
#     # 打开浏览器
#     def open_browser(self):
#         filepath = os.path.dirname(os.path.abspath('.')) + r"\Config\browser.ini"
#         config = configparser.ConfigParser()
#         config.read(filepath, encoding='utf-8')
#
#         browser = config.get('browserType', 'browserName')
#
#         if browser == "Chrome":
#             driver = webdriver.Chrome()
#         elif browser == 'Firefox':
#             driver = webdriver.Firefox()
#         elif browser == "IE":
#             driver = webdriver.Ie()

def open_browser():
    driver = None

    filepath = os.path.dirname(os.path.abspath('.')) + r"\Config\browser.ini"
    # config = configparser.ConfigParser()
    config = configparser.RawConfigParser()
    config.read(filepath, encoding='utf-8')

    browser = config.get('browserType', 'browserName')

    if browser == "Chrome":
        driver = webdriver.Chrome()
        # return driver

    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        # return driver

    elif browser == "IE":
        driver = webdriver.Ie()
        # return driver

    url = config.get("testServer", "URL")


    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(2)

    return driver



#
# if __name__ == '__main__':
#     b = BrowserEngine()
#     b.open_browser()
#     time.sleep(2)



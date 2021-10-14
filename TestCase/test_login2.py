import logging
import unittest
from selenium import webdriver
from time import sleep
from Page.login_page import LoginPage
from ddt import ddt, data, unpack
from Base import browser_engine, logger


class LoginTest(unittest.TestCase):
    """登录"""
    log = logger.Log("BrowserEngine").get_log()

    def setUp(self):
        self.driver = browser_engine.open_browser()
        self.log.info('open the browser')

    def tearDown(self):
        self.driver.quit()
        self.log.info('quit the browser')

    def test_success(self):
        # 验证输入正确用户名，密码是否能够登录成功
        self.lg = LoginPage(self.driver)
        self.lg.input_username("3656954720")
        self.log.info("输入用户名")
        self.lg.input_password("......")
        self.log.info("输入密码")
        self.lg.login_button()
        self.log.info("点击登录")
        sleep(2)

        # 获取论坛标签名
        title = self.lg.get_title()
        self.assertIn("论坛首页", title, "标签错误！")


if __name__ == '__main__':
    unittest.main()

from Page.home_page import HomePage
from Page.login_page import LoginPage
from selenium import webdriver
import unittest
from time import sleep


class TestLanguage(unittest.TestCase):
    """切换语言环境"""
    driver = webdriver.Chrome()
    url = "https://www.blockmango.net/#/login?redirect_url=https%3A%2F%2Fcreatorforum.blockmanmobile.com%2Fadd_cookie"
    hp = HomePage(driver)
    lg = LoginPage(driver)

    @classmethod
    def setUpClass(cls):
        cls.hp.open(cls.url)
        cls.lg.login("3656954720", "......")
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.hp.quit()

    def test_switch_english(self):
        """验证是否可以正常切换英文环境"""
        self.hp.switch_english()
        sleep(1)
        # 获取首页按钮文本
        text = self.hp.homepage_text()
        self.assertEqual("Home", text)

    def test_switch_chinese(self):
        """验证是否可以正常切换中文环境"""
        self.hp.switch_chinese()
        sleep(1)
        # 获取首页按钮文本
        text = self.hp.homepage_text()
        self.assertEqual("论坛首页", text)


if __name__ == '__main__':
    unittest.main()

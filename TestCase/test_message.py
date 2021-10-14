from Page.message_page import MessagePage
from Page.login_page import LoginPage
from Page.home_page import HomePage
from selenium import webdriver
import unittest
from time import sleep


class TestMessage(unittest.TestCase):
    """消息页面"""
    driver = webdriver.Chrome()
    url = "https://www.blockmango.net/#/login?redirect_url=https%3A%2F%2Fcreatorforum.blockmanmobile.com%2Fadd_cookie"
    mp = MessagePage(driver)
    lg = LoginPage(driver)
    hp = HomePage(driver)

    @classmethod
    def setUpClass(cls):
        cls.lg.open(cls.url)
        cls.lg.login("3656954720", "......")
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    def test_message_page(self):
        """验证点击消息按钮，是否正确跳转"""
        self.hp.click_message()
        sleep(1)

        # 获取消息页面的“新消息"文本
        text = self.mp.new_message()
        self.assertEqual("新消息", text)

    def test_message_issue(self):
        """验证在消息页面，点击发布话题，是否跳转到创建话题页面"""
        self.hp.click_message()
        sleep(1)
        self.mp.click_issue_button()
        sleep(1)
        # 获取标签名字
        title = self.driver.title
        self.assertIn("创建话题", title)


if __name__ == '__main__':
    unittest.main()
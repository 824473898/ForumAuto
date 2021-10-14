from Page.login_page import LoginPage
from Page.personal_page import Personal
from Page.home_page import HomePage
from Page.grade_page import GradePage
from selenium import webdriver
from time import sleep
import unittest


class TestPersonal(unittest.TestCase):
    """个人主页"""
    driver = webdriver.Chrome()
    ps = Personal(driver)
    lg = LoginPage(driver)
    hp = HomePage(driver)
    gp = GradePage(driver)
    url = "https://www.blockmango.net/#/login?redirect_url=https%3A%2F%2Fcreatorforum.blockmanmobile.com%2Fadd_cookie"

    @classmethod
    def setUpClass(cls):
        cls.ps.open(cls.url)
        cls.lg.login("3656954720", "......")

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    def test_personal_page(self):
        """验证个人主页是否跳转正确"""
        self.hp.click_user()
        sleep(1)

        # 获取用户昵称
        username = self.hp.get_username()
        # 获取个人主页的昵称
        text = self.ps.get_personal_name()
        self.assertEqual(username, text)

    def test_forum_grade(self):
        """点击论坛积分，是否正确跳转"""
        self.hp.click_user()
        sleep(1)
        self.ps.click_forum_grade()
        sleep(1)
        text = self.gp.get_grade_title()
        self.assertEqual("积分榜", text)

    # def test_collect(self):
    #     """点击收藏话题是否正确跳转"""
    #     self.hp.click_user()
    #     sleep(1)
    #     self.ps.click_forum_collect()
    #


if __name__ == '__main__':
    unittest.main()

from selenium import webdriver
import unittest
from Page.login_page import LoginPage
from Page.grade_page import GradePage
from Page.home_page import HomePage
from Page.personal_page import Personal
# from test_homepage import HomePage
from time import sleep


class TestGrade(unittest.TestCase):
    """积分榜"""
    driver = webdriver.Chrome()
    # url = "https://www.blockmango.net/#/login?redirect_url=https%3A%2F%2Fcreatorforum.blockmanmobile.com%2Fadd_cookie"
    lg = LoginPage(driver)
    gd = GradePage(driver)
    hp = HomePage(driver)
    ps = Personal(driver)

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        # cls.gd.open(cls.url)
        cls.lg.login("3656954720", "......")

    @classmethod
    def tearDownClass(cls):
        cls.lg.quit()
        # cls.lg.quit()

    def test_grade_page(self):
        """点击积分榜TOP100，验证是否显示100个用户"""
        self.hp.click_homepage()
        self.hp.click_top100()
        sleep(1)
        # 获取积分榜所有的用户
        number = self.gd.get_top100_number()
        self.assertEqual(100, number)

    def test_click_person(self):
        """随机点击一个用户，验证是否跳转到该用户个人主页 """
        self.hp.click_homepage()
        self.hp.click_top100()
        sleep(1)
        # 随机获取玩家并点击进入该玩家主页
        person = self.gd.click_random_person()
        sleep(1)
        # 获取该玩家的昵称
        nickname = self.ps.get_personal_name()
        self.assertEqual(person, nickname)


if __name__ == '__main__':
    unittest.main()

import unittest
from selenium import webdriver
from time import sleep
from Page.login_page import LoginPage
from ddt import ddt,data,unpack



@ddt
class LoginTest(unittest.TestCase):
    """登录"""
    driver = webdriver.Chrome()
    url = "https://www.blockmango.net/#/login?redirect_url=https%3A%2F%2Fcreatorforum.blockmanmobile.com%2Fadd_cookie"

    user_data = []
    with open("../Data/user.csv", 'r') as file:
        f = file.readlines()

    for line in f:
        l = line[:-1].split(',')
        user_data.append(l)



    @classmethod
    def setUpClass(cls):
        cls.lg = LoginPage(cls.driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    @data(user_data)
    @unpack
    def test_success(self):
        # 验证输入正确用户名，密码是否能够登录成功
        self.lg.open(self.url)
        self.lg.input_username("3656954720")
        self.lg.input_password("......")
        self.lg.login_button()
        sleep(2)

        # 获取论坛标签名
        title = self.lg.get_title()
        self.assertIn("论坛首页", title, "标签错误！")


if __name__ == '__main__':
    unittest.main()

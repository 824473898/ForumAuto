from selenium import webdriver
from Base.base_page import Base
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(Base):
    url = "https://www.blockmango.net/#/login?redirect_url=https%3A%2F%2Fcreatorforum.blockmanmobile.com%2Fadd_cookie"

    def input_username(self, text):
        self.locator_element(By.XPATH, '//input[@placeholder="请输入账号"]').send_keys(text)

    def input_password(self, text):
        self.locator_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys(text)

    def login_button(self):
        self.locator_element(By.XPATH, '//span[contains(text(),"登录")]').click()

    # 封装打开网站并登录的业务逻辑
    def login(self, username, password):
        self.open(self.url)
        self.input_username(username)
        self.input_password(password)
        self.login_button()
        sleep(2)


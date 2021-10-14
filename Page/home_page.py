from Base.base_page import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage(Base):
    # 点击论坛首页按钮
    def click_homepage(self):
        self.locator_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li/a/span').click()

    # 论坛首页文本
    def homepage_text(self):
        return self.locator_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li/a/span').text

    # 点击消息按钮
    def click_message(self):
        self.locator_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a').click()

    # 点击个人主页
    def click_user(self):
        self.locator_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a').click()

    # 用户昵称
    def get_username(self):
        return self.locator_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a').text

    # 点击发布话题按钮
    def click_issue(self):
        self.locator_element(By.XPATH, '//*[@id="goPostTopic"]/button').click()

    # 切换英文环境
    def switch_english(self):
        language = self.locator_element(By.ID, "language-cut")
        Select(language).select_by_value('en-US')

    # 切换中文环境
    def switch_chinese(self):
        language = self.locator_element(By.ID, "language-cut")
        Select(language).select_by_value('zh-CN')

    # 点击Top100
    def click_top100(self):
        self.locator_element(By.CSS_SELECTOR, "#scored-list > div > span.pull-right > a").click()

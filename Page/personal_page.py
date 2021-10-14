from selenium.webdriver.common.by import By
from Base.base_page import Base


class Personal(Base):

    # 返回用户昵称
    def get_personal_name(self):
        return self.locator_element(By.CSS_SELECTOR, ".media-body > div").text

    # 点击论坛积分按钮
    def click_forum_grade(self):
        self.locator_element(By.CSS_SELECTOR, ".media-body > div:nth-child(2) > a:nth-child(1)").click()

    # 点击收餐话题按钮
    def click_forum_collect(self):
        self.locator_element(By.CSS_SELECTOR, ".media-body > div:nth-child(2) > a:nth-child(2)").click()



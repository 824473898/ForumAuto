from selenium.webdriver.common.by import By
from Base.base_page import Base


class MessagePage(Base):

    # 定位并返回新消息文本
    def new_message(self):
        return self.locator_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/div").text

    # 点击消息页面中的发布按钮
    def click_issue_button(self):
        self.locator_element(By.XPATH, '//*[@id="goPostTopic"]/button').click()

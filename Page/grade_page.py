import random
from Base.base_page import Base
from selenium.webdriver.common.by import By


class GradePage(Base):

    # 返回积分页面中的“积分榜”
    def get_grade_title(self):
        return self.locator_element(By.CSS_SELECTOR, "#scored-list > div > span").text

    # 点击积分页面中的发布按钮
    def click_issue_button(self):
        self.locator_element(By.XPATH, '//*[@id="goPostTopic"]/button').click()

    # 获取Top100中随机点击一个用户名字，并且点击
    def click_random_person(self):
        # 随机获取一个玩家并点击
        i = random.randint(2, 101)
        person = self.driver.find_element_by_xpath("//tbody/tr[{0}]/td/a".format(i)).text
        self.driver.find_element_by_xpath("//tbody/tr[{0}]/td/a".format(i)).click()

        return person

    # 返回top100列表的用户数量
    def get_top100_number(self):
        user_number = self.driver.find_elements_by_xpath("//tbody/tr")
        # 删除第一个tr
        del user_number[0]
        return len(user_number)

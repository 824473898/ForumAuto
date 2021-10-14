class Base(object):
    """定义基础类"""

    def __init__(self, driver):
        self.driver = driver

    # 打开网站
    def open(self, url):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver.get(url)

    # 定位元素
    def locator_element(self, *locator):
        return self.driver.find_element(*locator)

    # 退出驱动
    def quit(self):
        return self.driver.quit()

    # 获取标签名
    def get_title(self):
        return self.driver.title


# 定义base类
from selenium.webdriver.support.wait import WebDriverWait
from base.driver import Driver


class Base:

    # 初始化类方法数据
    def __init__(self):
        self.driver = Driver.get_driver_open()

    # 定义当个元素-定位方法
    def search_ele(self, loc, timeout=10, poll_frequency=1.0):
        """
        :param loc: 元素的定位方式 (元祖)
        :param timeout: 显示等待的时间
        :param poll_frequency: 等待的间隔时间
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 定位多个元素-定位方法
    def search_eles(self, loc, timeout=10, poll_frequency=1.0):
        """
        :param loc: 元素的定位方式 (元祖)(By.ID,"ID的值")
        :param timeout: 显示等待的时间
        :param poll_frequency: 等待的间隔时间
        :return:返回一个类
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    # 定义-点击事件方法
    def click_btn(self, loc, timeout=10, poll_frequency=1.0):
        self.search_ele(loc, timeout, poll_frequency).click()

    # 定义发送事件方法
    def send_keys(self, loc, text, timeout=10, poll_frequency=1.0):
        # 定位
        loc_ele = self.search_ele(loc, timeout, poll_frequency)
        # 清空
        loc_ele.clear()
        # 发送数据
        loc_ele.send_keys(text)

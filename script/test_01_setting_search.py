# 定义测试类
import pytest
from selenium.webdriver.common.by import By

from base.base import Base
from base.driver import Driver
from base.page import PageClass


class Test:

    # 定义方法级别销魂driver
    def teardown_class(self):
        # 关闭driver
        Driver.get_driver_quit()

    # 定义点击操作方法
    @pytest.fixture(scope='class', autouse=True)
    def click_btn(self):
        # 点击搜索按钮
        PageClass.get_setting_page().click_search_btn()

    # 定义输入操作方法
    @pytest.mark.parametrize("data,exp_data", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_data(self, data, exp_data):
        # 输入数据
        PageClass.get_search_page().input_data(data)
        # 断言
        rul = PageClass.get_search_page().show_data()
        assert exp_data in rul

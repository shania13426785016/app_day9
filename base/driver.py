from appium import webdriver
from selenium import webdriver

# 定义driver类


class Driver:
    app_driver = None  # 定义空的driver

    # 开启driver方法
    @classmethod
    def get_driver_open(cls):
        # 判断driver是否为空
        if cls.app_driver is None:
            # 启动driver
            devt_app = {
                'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '小米',
                "appPackage": "com.android.settings",
                "appActivity": ".Settings"
            }
            # 声明driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', devt_app)
            return cls.app_driver
        else:
            return cls.app_driver

    # 关闭driver方法
    @classmethod
    def get_driver_quit(cls):
        # 判断app_driver是否有值:
        if cls.app_driver:
            # 关闭app_driver
            cls.app_driver.quit()
            # 清空app_driver的值
            cls.app_driver = None

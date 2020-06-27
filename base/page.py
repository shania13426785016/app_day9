# 统一实例化页面类方便管理
from page.searchpage import SearchPage
from page.settingpage import SettingPage


class PageClass:
    # 返回页面所有实例化对象

    @classmethod  #不用实例化, 直接调用
    def get_search_page(cls):
        # 实例化查找页面
        return SearchPage()

    @classmethod
    def get_setting_page(cls):
        return SettingPage()

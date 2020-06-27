
from base.base import Base
from page.pageelement import PageElement


# 1 导入base类,并集成base
class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def click_search_btn(self):
        # 点击设置收搜按钮
        print("元素:",PageElement.search_btn_loc)
        self.click_btn(PageElement.search_btn_loc)


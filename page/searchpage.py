# 定义搜索页面类,继承base类
from base.base import Base
from page.pageelement import PageElement


class SearchPage(Base):

    # 初始化类方法
    def __init__(self):
        super().__init__()

    # 定义类方法_输入信息搜索
    def input_data(self, rep_text):
        """
        :param text: 要输入的数据
        :return:
        """
        # 输入数据
        self.send_keys(PageElement.search_input_loc, rep_text)

    def show_data(self):
        # _展示信息进行断言
        ret = self.search_eles(PageElement.show_data)
        return [i.text for i in ret]

# 页面元素定位\

# 定义页面元素定位类
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class PageElement:
    # 搜索按钮
    # search_btn_loc = (By.ID, 'com.android.settings:id/search')
    search_btn_loc = (By.XPATH, '//*[contains(@resource-id,"com.android.settings:id/search")]')

    # 搜索输入框定位
    search_input_loc = (By.ID, 'android:id/search_src_text')

    # 展示信息定位
    show_data = (By.CLASS_NAME, 'android.widget.TextView')

import allure


class TestSetp:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是测试步骤的名称1")
    def test_01(self):
        allure.attach("我是附件里面的内容1", "我是附件名称1")
        assert True

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        allure.attach("我是附件里面的内容2", "我是附件名称2")
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        allure.attach("我是附件里面的内容3", "我是附件名称3")
        assert False

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_04(self):
        allure.attach("我是附件里面的内容4", "我是附件名称4")
        assert True
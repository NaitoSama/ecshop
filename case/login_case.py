'''
封装page页面对应的case页面，使用unittest单元测试框架写的用例和断言，需要调用page页面里面的封装的方法
注意：一个page页面都会有一个对应的case页面
'''

import unittest
from page.login_page import LoginPage

class TestLogin(unittest.TestCase):  # 不能够继承LoginPage，因为构造方法会冲突
    def setUp(self):
        self.lp = LoginPage()  # 实例化一个浏览器对象
        self.lp.open()  # 打开网页

    def tearDown(self):
        self.lp.driver.quit()  # 关闭浏览器

    def test_success(self):  # 测试登录成功
        self.lp.login('admin','naito1001')
        result = self.lp.login_check()
        self.assertTrue(result)

    def test_fail(self):  # 测试登录失败
        self.lp.login('admin','naito100')
        result = self.lp.login_check()
        self.assertFalse(result)


if __name__ == '__main__':
    TestLogin()
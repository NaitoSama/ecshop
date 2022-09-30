'''
用户前台登录测试用例
'''

from page.user_login_page import UserLogin
import unittest
from common.connect_db import ConnectDB



class UserLoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.add = UserLogin()
        self.add.switch_to_login_page()

    def tearDown(self) -> None:
        self.add.driver.quit()

    def test_user_login(self):
        self.add.user_login('naitosama','naito1001')
        response = '登录成功'
        result = self.add.user_login_success()
        self.assertEqual(response,result)


if __name__ == '__main__':
    UserLoginTest()




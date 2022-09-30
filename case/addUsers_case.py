'''
从csv添加用户的case
'''

import unittest
from page.addUser_page import AddUserPage
from common.connect_db import ConnectDB
from common.read_excel import ReadExcel
from ddt import ddt,data

file = ReadExcel(r'F:\pythonProject\ecshop\data\adduser_data.csv')
success_data = file.read_to_dict()


@ddt  # 在测试类前面加的ddt装饰
class AddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls):
        cls.db.close_db()

    def setUp(self):
        self.add = AddUserPage()

    def tearDown(self):
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_users where user_name="{self.username}"')

    @data(*success_data)  # 在测试方法前面用data装饰，类似于遍历，*success_data是拆包，拆成一条一条的数据
    def test_success(self,info):
        self.username = info['username']
        self.add.add_user(self.username,info['email'],str(info['password']),str(info['re_password']))  # 数字要转str
        result = self.add.add_user_success()
        self.assertIn(self.add.username,result)
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="{self.username}"')
        self.assertTrue(db_result)


if __name__ == '__main__':
    AddUser()

'''
从csv添加用户的case
'''

import unittest
from page.addUser_page import AddUserPage
from common.connect_db import ConnectDB
from common.read_excel import ReadExcel
from ddt import ddt,data

file = ReadExcel(r'F:\pythonProject\ecshop\data\adduser_data_fail.csv')
success_data = file.read_to_dict()


@ddt  # 在测试类前面加的ddt装饰
class AddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = ConnectDB()
        cls.db.cursor.execute('insert into ecs_users(email,user_name,password) values ("test6@test.com","test6","60452a37bfd651efbcb0b6d7d032adc8")')

    @classmethod
    def tearDownClass(cls):
        cls.db.cursor.execute('delete from ecs_users where user_name="test6"')
        cls.db.close_db()

    def setUp(self):
        self.add = AddUserPage()

    def tearDown(self):
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_users where user_name="{self.username}"')

    @data(*success_data)  # 在测试方法前面用data装饰，类似于遍历，*success_data是拆包，拆成一条一条的数据
    def test_fail(self,info):
        self.username = info['username']
        self.add.add_user(self.username,info['email'],str(info['password']),str(info['re_password']))  # 数字要转str
        result = self.add.add_user_success()
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="{self.username}"')
        self.assertFalse(db_result)

    def test_username_blank(self):
        self.username = ''
        self.add.add_user(self.username,'aaaa@aaa.com','123123','123123')  # 数字要转str
        result = self.add.add_user_success()
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="{self.username}"')
        self.assertFalse(db_result)

    def test_email_blank(self):
        try:
            self.db.execute_sql(f'delete from ecs_users where user_name="test7"')
        except:
            pass
        self.username = 'test7'
        self.add.add_user(self.username, '', '123123', '123123')  # 数字要转str
        result = self.add.add_user_success()
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="{self.username}"')
        self.assertFalse(db_result)

    def test_password_blank(self):
        try:
            self.db.execute_sql(f'delete from ecs_users where user_name="test8"')
        except:
            pass
        self.username = 'test8'
        self.add.add_user(self.username, 'aaaa@aaa.com', '', '123123')  # 数字要转str
        result = self.add.add_user_success()
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="{self.username}"')
        self.assertFalse(db_result)

    def test_re_password_blank(self):
        try:
            self.db.execute_sql(f'delete from ecs_users where user_name="test9"')
        except:
            pass
        self.username = 'test9'
        self.add.add_user(self.username, 'aaaa@aaa.com', '123123', '')  # 数字要转str
        result = self.add.add_user_success()
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="{self.username}"')
        self.assertFalse(db_result)

    def test_username_re(self):
        self.username = 'test6'
        self.add.add_user(self.username, 'test6@test.com', '123123', '123123')  # 数字要转str
        result = self.add.add_user_success()
        self.assertFalse(result)


if __name__ == '__main__':
    AddUser()

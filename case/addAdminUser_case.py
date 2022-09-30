'''
添加管理员账号的测试用例
'''

import unittest
from page.addAdminUser_page import AddAdminUser
from common.connect_db import ConnectDB
from ddt import ddt,data
from common.read_excel import ReadExcel


file = ReadExcel(r'F:\pythonProject\ecshop\data\addadminuser_data.csv')
success_data = file.read_to_dict()
file = ReadExcel(r'F:\pythonProject\ecshop\data\addadminuser_data_fail.csv')
fail_data = file.read_to_dict()


@ddt
class AddAdminUserCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()
        cls.db.execute_sql('insert into ecs_admin_user(user_name,email,password) values("test0","test0@admin.com","ttest0")')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.execute_sql('delete from ecs_admin_user where user_name="test0"')
        cls.db.close_db()

    def setUp(self) -> None:
        self.add = AddAdminUser()
        self.add.switch_to_add_admin_user_window()

    def tearDown(self) -> None:
        self.add.driver.quit()
        try:
            self.db.execute_sql(f'delete from ecs_admin_user where user_name="{self.account}"')
        except:
            pass

    @data(*success_data)
    def test_add_admin_user_from_file_success(self,info):
        self.account = info['username']
        self.add.add_admin_user(self.account,info['email'],str(info['password']),str(info['re_password']))
        result = self.db.execute_sql(f'select * from ecs_admin_user where user_name="{self.account}"')
        self.assertTrue(result)


    @data(*fail_data)
    def test_add_admin_user_from_file_fail(self,info):
        self.account = info['username']
        self.add.add_admin_user(self.account, info['email'], str(info['password']), str(info['re_password']))
        result = self.db.execute_sql(f'select * from ecs_admin_user where user_name="{self.account}"')
        self.assertFalse(result)

    def test_admin_username_blank(self):
        self.account = ''
        self.add.add_admin_user(self.account,'testtest@admin.com','A11111','A11111')
        result = self.db.execute_sql(f'select * from ecs_admin_user where user_name="{self.account}"')
        self.assertFalse(result)

    def test_admin_email_blank(self):
        self.account = 'test123'
        self.add.add_admin_user(self.account, '', 'A11111', 'A11111')
        result = self.db.execute_sql(f'select * from ecs_admin_user where user_name="{self.account}"')
        self.assertFalse(result)

    def test_admin_password_blank(self):
        self.account = 'test123'
        self.add.add_admin_user(self.account, 'testtest@admin.com', '', 'A11111')
        result = self.db.execute_sql(f'select * from ecs_admin_user where user_name="{self.account}"')
        self.assertFalse(result)

    def test_admin_re_password_blank(self):
        self.account = 'test123'
        self.add.add_admin_user(self.account, 'testtest@admin.com', 'A11111', '')
        result = self.db.execute_sql(f'select * from ecs_admin_user where user_name="{self.account}"')
        self.assertFalse(result)


if __name__ == '__main__':
    AddAdminUser()



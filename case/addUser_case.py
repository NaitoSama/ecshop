'''
添加用户的case
'''

import unittest
from page.addUser_page import AddUserPage
from common.connect_db import ConnectDB


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
    def test_success(self):
        self.username = 'test4'
        self.add.add_user('test4','test4@test.com','ttest4','ttest4')
        result = self.add.add_user_success()
        self.assertIn(self.add.username,result)
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="test4"')
        self.assertTrue(db_result)

    def test_account_alpha_success(self):
        self.username = 'testt'
        self.add.add_user('testt', 'testt@test.com', 'ttestt','ttestt')
        result = self.add.add_user_success()
        self.assertIn(self.add.username, result)
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="testt"')
        self.assertTrue(db_result)

    def test_account_alpha_and_number_success(self):
        self.username = 'test5'
        self.add.add_user('test5', 'testt@test.com', 'ttest5','ttest5')
        result = self.add.add_user_success()
        self.assertIn(self.add.username, result)
        db_result = self.db.execute_sql(f'select * from ecs_users where user_name="test5"')
        self.assertTrue(db_result)



if __name__ == '__main__':
    AddUser()

'''
新增用户等级的测试用例
'''


from page.add_user_rank_page import AddUserRankPage
import unittest
from common.connect_db import ConnectDB
from ddt import ddt,data
from common.read_excel import ReadExcel


file = ReadExcel(r'F:\pythonProject\ecshop\data\add_user_rank_success.csv')
success_data = file.read_to_dict()
file = ReadExcel(r'F:\pythonProject\ecshop\data\add_user_rank_fail.csv')
fail_data = file.read_to_dict()


@ddt
class AddUserRankTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()

    def setUp(self) -> None:
        self.add = AddUserRankPage()
        self.add.switch_to_user_rank_page()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_user_rank where rank_name="{self.user_rank}"')

    @data(*success_data)
    def test_add_user_rank_success(self,info):
        self.user_rank = info['user_rank']
        self.add.add_user_rank(self.user_rank,str(info['max_points']),str(info['min_points']),str(info['discount']))
        result = self.db.execute_sql(f'select * from ecs_user_rank where rank_name="{self.user_rank}"')
        self.assertTrue(result)


    @data(*fail_data)
    def test_add_user_rank_fail(self, info):
        self.user_rank = info['user_rank']
        self.add.add_user_rank(self.user_rank, str(info['max_points']), str(info['min_points']), str(info['discount']))
        try:
            result = self.add.driver.switch_to.alert.text
            self.assertTrue(result)
        except:
            result = self.add.add_user_rank_success()
            self.assertFalse(result)

    def test_rank_blank(self):
        self.user_rank = ''
        self.add.add_user_rank(self.user_rank,'100','0','90')
        try:
            result = self.add.driver.switch_to.alert.text
            self.assertTrue(result)
        except:
            result = self.add.add_user_rank_success()
            self.assertFalse(result)

    def test_min_points_blank(self):
        self.user_rank = 'test666'
        self.add.add_user_rank(self.user_rank,'100','','90')
        try:
            result = self.add.driver.switch_to.alert.text
            self.assertTrue(result)
        except:
            result = self.add.add_user_rank_success()
            self.assertFalse(result)

    def test_max_points_blank(self):
        self.user_rank = 'test777'
        self.add.add_user_rank(self.user_rank,'','0','90')
        try:
            result = self.add.driver.switch_to.alert.text
            self.assertTrue(result)
        except:
            result = self.add.add_user_rank_success()
            self.assertFalse(result)

    def test_discount_blank(self):
        self.user_rank = ''
        self.add.add_user_rank(self.user_rank,'100','0','')
        try:
            result = self.add.driver.switch_to.alert.text
            self.assertTrue(result)
        except:
            result = self.add.add_user_rank_success()
            self.assertFalse(result)


if __name__ == '__main__':
    AddUserRankTest()


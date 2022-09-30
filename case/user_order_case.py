'''
用户下单的测试用例
'''


from page.user_order_page import UserOrderPage
from common.connect_db import ConnectDB
import unittest



class UserOrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()


    def setUp(self) -> None:
        self.add = UserOrderPage()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_order_info where order_sn="{self.order_number}"')
        self.db.execute_sql('delete from ecs_order_goods where goods_name="高质感毛呢大衣"')

    def test_user_order(self):
        self.add.place_order()
        self.order_number = self.add.get_order_number_and_quit()
        result = self.db.execute_sql(f'select * from ecs_order_info where order_sn="{self.order_number}"')
        self.assertTrue(result)


if __name__ == '__main__':
    UserOrderTest()


'''
新增一个拍卖的测试用例
'''

from page.add_auction_page import AddAuctionPage
import unittest
from ddt import ddt, data
from common.connect_db import ConnectDB
from common.read_excel import ReadExcel
from time import sleep


file = ReadExcel(r'F:\pythonProject\ecshop\data\add_auction_data.csv')
success_data = file.read_to_dict()


@ddt
class AddAuctionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()

    def setUp(self) -> None:
        self.add = AddAuctionPage()
        self.add.switch_to_auction_page()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_goods_activity where act_name="{self.auction}"')

    @data(*success_data)
    def test_add_auction(self, info):
        self.auction = info['auction']
        self.add.add_auction(self.auction, info['description'], info['goods'], info['bdate'], info['edate'],
                             info['starting_price'], info['price'], info['increase_range'], info['bond'])
        result = self.db.execute_sql(f'select * from ecs_goods_activity where act_name="{self.auction}"')
        self.assertTrue(result)


if __name__ == '__main__':
    AddAuctionTest()
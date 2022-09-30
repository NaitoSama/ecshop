'''
新增快递配送区域测试用例
'''

from common.connect_db import ConnectDB
from common.read_excel import ReadExcel
from ddt import ddt,data
from page.express_delivery_area_page import ExpressDeliveryAreaPage
import unittest

file = ReadExcel(r'F:\pythonProject\ecshop\data\express_delivery_area_data_success.csv')
success_data = file.read_to_dict()


@ddt
class ExpressDeliveryAreaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()


    def setUp(self) -> None:
        self.add = ExpressDeliveryAreaPage()
        self.add.swith_to_area_page()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_shipping_area where shipping_area_name="{self.area}"')

    @data(*success_data)
    def test_add_area(self,info):
        self.area = info['area']
        self.add.add_delivery_area(self.area,info['base_fee'],info['step_fee'],info['free_money'],info['pay_fee'],info['province'],info['city'],info['district'])
        self.add.add_delivery_area_commit()
        result = self.db.execute_sql(f'select * from ecs_shipping_area where shipping_area_name="{self.area}"')
        self.assertTrue(result)


if __name__ == '__main__':
    ExpressDeliveryAreaTest()










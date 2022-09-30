'''
添加商品的测试用例
'''


from page.add_goods_page import AddGoodsPage
import unittest
from common.read_excel import ReadExcel
from common.connect_db import ConnectDB
from ddt import ddt,data


file = ReadExcel(r'F:\pythonProject\ecshop\data\addgoods.csv')
success_data = file.read_to_dict()



@ddt
class AddGoodsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()

    def setUp(self) -> None:
        self.add = AddGoodsPage()
        self.add.switch_to_goods_page()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_goods where goods_name="{self.goods_name}"')

    @data(*success_data)
    def test_add_goods(self,info):
        self.goods_name = info['goods_name']
        self.add.add_goods(self.goods_name,info['goods_classification'],str(info['goods_price']))
        result = self.add.add_goods_success()
        self.assertTrue(result)

    def test_add_goods_with_wrong_classification(self):
        self.goods_name = '红米K30U'
        response = '没有此商品分类'
        result = self.add.add_goods(self.goods_name,'红米手机','666')
        self.assertEqual(response,result)


if __name__ == '__main__':
    AddGoodsTest()













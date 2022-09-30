'''
添加商品类型的测试用例
'''


from page.add_goods_type_page import AddGoodsTypePage
import unittest
from common.connect_db import ConnectDB
from ddt import ddt,data
from common.read_excel import ReadExcel


file = ReadExcel(r'F:\pythonProject\ecshop\data\add_goods_type_success.csv')
success_data = file.read_to_dict()
file = ReadExcel(r'F:\pythonProject\ecshop\data\add_goods_type_fail.csv')
fail_data = file.read_to_dict()



@ddt
class AddGoodsTypeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()

    def setUp(self) -> None:
        self.add = AddGoodsTypePage()
        self.add.swith_to_goods_type_page()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_goods_type where cat_name="{self.goods_type}"')

    @data(*success_data)
    def test_add_goods_type_from_file_success(self,info):
        self.goods_type = info['goods_type']
        self.add.add_goods_type(self.goods_type)
        result = self.db.execute_sql(f'select * from ecs_goods_type where cat_name="{self.goods_type}"')
        self.assertTrue(result)

    @data(*fail_data)
    def test_add_goods_type_from_file_fail(self,info):
        self.goods_type = info['goods_type']
        self.add.add_goods_type(self.goods_type)
        result = self.db.execute_sql(f'select * from ecs_goods_type where cat_name="{self.goods_type}"')
        self.assertFalse(result)

    def test_add_goods_type_existed(self):
        self.goods_type = '重复数据'
        if self.db.execute_sql(f'select * from ecs_goods_type where cat_name="{self.goods_type}"'):
            pass
        else:
            self.db.execute_sql(f'insert into ecs_goods_type(cat_name) values("{self.goods_type}")')
        self.add.add_goods_type(self.goods_type)
        response = '新建商品类型成功'
        result = self.add.add_goods_type_success()
        self.assertIn(response,result)

    def test_add_goods_type_blank(self):
        self.goods_type = ''
        self.add.add_goods_type(self.goods_type)
        response = '不能为空'
        result = self.add.driver.switch_to.alert.text
        self.assertIn(response,result)


if __name__ == '__main__':
    AddGoodsTypeTest()




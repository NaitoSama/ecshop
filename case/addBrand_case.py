'''
后台添加商品品牌的测试用例
'''

from page.addBrand_page import AddBrand
import unittest
from common.connect_db import ConnectDB
from common.read_excel import ReadExcel
from ddt import ddt, data


file = ReadExcel(r'F:\pythonProject\ecshop\data\brand.csv')
data_success = file.read_to_dict()


@ddt
class AddBrandTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()

    def setUp(self) -> None:
        self.add = AddBrand()
        self.add.switch_to_add_brand()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_brand where brand_name="{self.brand}"')

    @data(*data_success)
    def test_add_brand_success(self,info):
        self.brand = info['brand']
        self.add.add_brand(self.brand)
        check = self.add.add_brand_success()
        if check:
            pass
        else:
            self.assertTrue(check)
        result = self.db.execute_sql(f'select * from ecs_brand where brand_name="{self.brand}"')
        self.assertTrue(result)

    def test_brand_blank(self):
        self.brand = ''
        self.add.add_brand(self.brand)
        response = '您必须输入品牌名称'
        result = self.add.driver.switch_to.alert.text
        self.assertIn(response,result)

    def test_brand_existed(self):
        self.brand = '腾讯会议'
        self.db.execute_sql(f'insert into ecs_brand(brand_name) values("{self.brand}")')
        self.add.add_brand(self.brand)
        result = self.add.add_brand_success()
        self.assertFalse(result)


if __name__ == '__main__':
    AddBrandTest()











'''
修改商品分类的信息
'''


import unittest
from page.modify_category_page import ModifyCategoryPage
from common.connect_db import ConnectDB
from ddt import ddt,data
from common.read_excel import ReadExcel


file = ReadExcel(r'F:\pythonProject\ecshop\data\mod_cname.csv')
success_data = file.read_to_dict()


@ddt
class ModifyCategoryCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()


    def setUp(self) -> None:
        self.mod = ModifyCategoryPage()
        self.mod.switch_to_category_page()

    def tearDown(self) -> None:
        self.mod.driver.quit()
        self.db.execute_sql(f'update ecs_category set cat_name="{self.bcname}" where cat_name="{self.acname}"')


    @data(*success_data)
    def test_mod_cname(self,info):
        self.bcname = info['bcname']
        self.acname = info['acname']
        self.mod.modify_category(self.bcname,self.acname)
        response = '商品分类编辑成功!'
        result = self.mod.modify_category_success()
        self.assertEqual(response,result)


if __name__ == '__main__':
    ModifyCategoryCase()
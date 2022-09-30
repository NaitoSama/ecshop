'''
新增用户的收货地址
'''



from page.user_address_page import UserAddressPage
import unittest
from ddt import ddt,data
from common.read_excel import ReadExcel
from common.connect_db import ConnectDB

file = ReadExcel(r'F:\pythonProject\ecshop\data\user_address_success.csv')
success_data = file.read_to_dict()


@ddt
class AddUserAddressTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = ConnectDB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()


    def setUp(self) -> None:
        self.add = UserAddressPage()
        self.add.switch_to_user_address_page()

    def tearDown(self) -> None:
        self.add.driver.quit()
        self.db.execute_sql(f'delete from ecs_user_address where consignee="{self.uname}"')


    @data(*success_data)
    def test_add_user_address_success(self,info):
        self.uname = info['uname']
        self.add.add_user_address(info['province'],info['city'],info['district'],self.uname,info['detailed_address'],info['phone'])
        result = self.db.execute_sql(f'select * from ecs_user_address where consignee="{self.uname}"')
        self.assertTrue(result)


if __name__ == '__main__':
    AddUserAddressTest()





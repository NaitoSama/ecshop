'''
添加商品类型的page
'''

from page.login_page import LoginPage
from selenium.webdriver.common.by import By



class AddGoodsTypePage(LoginPage):
    def swith_to_goods_type_page(self):
        self.open()
        self.login('admin','naito1001')
        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element(By.CSS_SELECTOR,'li[key="02_cat_and_goods"]').click()
        self.driver.find_element(By.LINK_TEXT,'商品类型').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('main-frame')

    def add_goods_type(self,goods_type):
        self.driver.find_element(By.LINK_TEXT,'新建商品类型').click()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="cat_name"]').send_keys(goods_type)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def add_goods_type_success(self):
        try:
            result = self.driver.find_element(By.XPATH,'//td[contains(text(),"新建商品类型成功。")]').text
            return result
        except:
            return False


if __name__ == '__main__':
    add = AddGoodsTypePage()
    add.swith_to_goods_type_page()
    add.add_goods_type('我是战神')
    print(add.add_goods_type_success())




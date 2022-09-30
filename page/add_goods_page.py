'''
添加商品
'''

from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from selenium.webdriver.support.select import Select
from time import sleep


class AddGoodsPage(LoginPage):
    def switch_to_goods_page(self):
        self.open()
        self.login('admin','naito1001')
        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element(By.CSS_SELECTOR,'li[key="02_cat_and_goods"]').click()
        self.driver.find_element(By.LINK_TEXT,'添加新商品').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('main-frame')

    def add_goods(self,goods_name,goods_classification,goods_price):

        self.driver.find_element(By.CSS_SELECTOR,'input[name="goods_name"]').send_keys(goods_name)
        self.driver.find_element(By.CSS_SELECTOR,'select[name="cat_id"]').click()
        try:
            self.driver.find_element(By.XPATH,f'//select[@name="cat_id"]/option[contains(text(),"{goods_classification}")]').click()
        except:
            return '没有此商品分类'
        self.driver.find_element(By.CSS_SELECTOR, 'select[name="cat_id"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="shop_price"]').send_keys(goods_price)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def add_goods_success(self):
        sleep(0.5)
        try:
            result = self.driver.find_element(By.XPATH,'//td[contains(text(),"添加商品成功。")]').text
            return result
        except:
            return False

if __name__ == '__main__':
    add = AddGoodsPage()
    add.switch_to_goods_page()
    print(add.add_goods('罗技g502', '鼠标', '249'))
    print(add.add_goods_success())



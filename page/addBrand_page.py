'''
后台添加商品品牌
'''

from page.login_page import LoginPage
from selenium.webdriver.common.by import By


class AddBrand(LoginPage):
    def switch_to_add_brand(self):
        self.open()
        self.login('admin','naito1001')
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR,'#menu-frame'))
        self.driver.find_element(By.CSS_SELECTOR,'li[key="02_cat_and_goods"]').click()
        self.driver.find_element(By.LINK_TEXT,'商品品牌').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, '#main-frame'))
        self.driver.find_element(By.LINK_TEXT,'添加品牌').click()

    def add_brand(self,brand):
        self.driver.find_element(By.CSS_SELECTOR,'input[name="brand_name"]').send_keys(brand)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def add_brand_success(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, '#main-frame'))
        try:
            result = self.driver.find_element(By.XPATH,'//td[contains(text(),"新品牌添加成功！")]').text
            if result == '新品牌添加成功！':
                return True
            else:
                return False
        except:
            return False

if __name__ == '__main__':
    add = AddBrand()
    add.switch_to_add_brand()
    add.add_brand('双头龙')
    print(add.add_brand_success())

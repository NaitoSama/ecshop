'''
修改指定商品分类的信息
'''


from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class ModifyCategoryPage(LoginPage):
    def switch_to_category_page(self):
        self.open()
        self.login('admin','naito1001')
        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element(By.CSS_SELECTOR,'li[key="02_cat_and_goods"]').click()
        self.driver.find_element(By.LINK_TEXT,'商品分类').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('main-frame')

    def modify_category(self,before_name,after_name):
        path = f'//a[contains(text(),"{before_name}")]/../../../td[8]/a[2]'  # locate target tag
        self.driver.find_element(By.XPATH,path).click()
        length = len(before_name)  # get how many times needed to blackspace
        for i in range(length):
            self.driver.find_element(By.CSS_SELECTOR,'input[name="cat_name"]').send_keys(Keys.RIGHT)  # delete the old category name
            self.driver.find_element(By.CSS_SELECTOR,'input[name="cat_name"]').send_keys(Keys.BACK_SPACE)  # delete the old category name
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="cat_name"]').send_keys(after_name)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def modify_category_success(self):
        try:
            result = self.driver.find_element(By.XPATH,'//td[contains(text(),"商品分类编辑成功!")]').text
            self.driver.find_element(By.LINK_TEXT,'返回分类列表').click()
            return result
        except:
            return False


if __name__ == '__main__':
    mod = ModifyCategoryPage()
    mod.switch_to_category_page()
    mod.modify_category('男装1','男装')
    print(mod.modify_category_success())
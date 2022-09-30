'''
新增快递配送区域
'''


from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class ExpressDeliveryAreaPage(LoginPage):
    def swith_to_area_page(self):
        self.open()
        self.login('admin','naito1001')
        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element(By.CSS_SELECTOR,'li[key="11_system"]').click()
        self.driver.find_element(By.LINK_TEXT,'配送方式').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('main-frame')
        self.driver.find_element(By.XPATH,'//span[text()="圆通速递"]/../../td[@align="center"]/a[text()="设置区域"]').click()
        self.driver.find_element(By.LINK_TEXT, '新建配送区域').click()

    def add_delivery_area(self,area,base_fee,step_fee,free_money,pay_fee,province,city,district):

        self.driver.find_element(By.CSS_SELECTOR,'input[name="shipping_area_name"]').send_keys(area)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="base_fee"]').clear()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="base_fee"]').send_keys(base_fee)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="step_fee"]').clear()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="step_fee"]').send_keys(step_fee)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="free_money"]').clear()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="free_money"]').send_keys(free_money)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="pay_fee"]').clear()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="pay_fee"]').send_keys(pay_fee)
        Select(self.driver.find_element(By.ID,'selProvinces')).select_by_visible_text(province)
        Select(self.driver.find_element(By.ID,'selCities')).select_by_visible_text(city)
        Select(self.driver.find_element(By.ID,'selDistricts')).select_by_visible_text(district)
        self.driver.find_element(By.CSS_SELECTOR,'input[onclick="addRegion()"]').click()

    def add_delivery_area_commit(self):
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def add_delivery_area_success(self):
        try:
            result = self.driver.find_element(By.XPATH,'//td[contains(text(),"添加配送区域成功。")]').text
            self.driver.find_element(By.LINK_TEXT,'返回列表页').click()
            return result
        except:
            return False


if __name__ == '__main__':
    add = ExpressDeliveryAreaPage()
    add.swith_to_area_page()
    add.add_delivery_area('四川资阳雁江区','15','2','0','0','四川','资阳','雁江区')
    add.add_delivery_area_commit()
    print(add.add_delivery_area_success())


























'''
新增用户收货地址
'''

from page.user_login_page import UserLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UserAddressPage(UserLogin):
    def switch_to_user_address_page(self):
        self.switch_to_login_page()
        self.user_login('naitosama','naito1001')
        self.driver.find_element(By.LINK_TEXT,'我的账户').click()
        self.driver.find_element(By.CSS_SELECTOR,'.userMenu>a:nth-child(4)').click()

    def add_user_address(self,province,city,district,uname,detailed_address,phone):
        eles = self.driver.find_elements(By.CSS_SELECTOR,'form[name="theForm"]')
        ele = eles[-1]

        Select(ele.find_element(By.CSS_SELECTOR,'select[name="province"]')).select_by_visible_text(province)
        Select(ele.find_element(By.CSS_SELECTOR,'select[name="city"]')).select_by_visible_text(city)
        Select(ele.find_element(By.CSS_SELECTOR,'select[name="district"]')).select_by_visible_text(district)
        ele.find_element(By.CSS_SELECTOR,'input[name="consignee"]').send_keys(uname)
        ele.find_element(By.CSS_SELECTOR,'input[name="address"]').send_keys(detailed_address)
        ele.find_element(By.CSS_SELECTOR,'input[name="tel"]').send_keys(phone)
        ele.find_element(By.CSS_SELECTOR,'input[name="submit"]').click()

    def add_user_address_success(self):
        try:
            result = self.driver.find_element(By.XPATH,'//p[text()="您的收货地址信息已成功更新！"]').text
            self.driver.find_element(By.LINK_TEXT,'返回地址列表').click()
            return result
        except:
            return False


if __name__ == '__main__':
    add = UserAddressPage()
    add.switch_to_user_address_page()
    add.add_user_address('四川','资阳','雁江区','卡尔','建东市场','13241567934')
    print(add.add_user_address_success())








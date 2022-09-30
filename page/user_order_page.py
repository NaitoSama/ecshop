'''
用户下单
'''


from page.user_login_page import UserLogin
from selenium.webdriver.common.by import By



class UserOrderPage(UserLogin):
    def place_order(self):
        self.switch_to_login_page()
        self.user_login('naitosama','naito1001')
        self.driver.find_element(By.CSS_SELECTOR,'.menu>a:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR,'img[alt="高质感毛呢大衣"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'.padd>a').click()
        self.driver.find_element(By.CSS_SELECTOR,'img[alt="checkout"]').click()
        self.driver.find_element(By.XPATH,'//strong[text()="圆通速递"]/../../td/input').click()
        self.driver.find_element(By.XPATH,'//strong[text()="余额支付"]/../../td/input').click()
        eles = self.driver.find_elements(By.CSS_SELECTOR,'div[align="center"]')
        eles[-2].find_element(By.CSS_SELECTOR,'input').click()
        try:
            self.tempele = self.driver.find_element(By.XPATH,'//h6[text()="感谢您在本店购物！您的订单已提交成功，请记住您的订单号: "]')
            result = self.tempele.text
            return result
        except:
            return False

    def get_order_number_and_quit(self):
        order_number = self.tempele.find_element(By.CSS_SELECTOR,'font').text
        self.driver.find_element(By.LINK_TEXT,'返回首页').click()
        return order_number


if __name__ == '__main__':
    add = UserOrderPage()
    print(add.place_order())
    print(add.get_order_number_and_quit())









'''
前台用户登录
'''

from common.get_driver import Driver
from selenium.webdriver.common.by import By


class UserLogin(Driver):
    def switch_to_login_page(self):
        self.driver.get('http://localhost/ecshop/')
        self.driver.find_element(By.LINK_TEXT,'登录').click()

    def user_login(self,username,password):
        self.driver.find_element(By.CSS_SELECTOR,'input[name="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="submit"]').click()


    def user_login_success(self):

        try:
            result = self.driver.find_element(By.XPATH,'//p[contains(text(),"登录成功")]').text
            self.driver.find_element(By.LINK_TEXT, '返回上一页').click()
            return result
        except:
            return False


if __name__ == '__main__':
    login = UserLogin()
    login.switch_to_login_page()
    login.user_login('naitosama','naito1001')
    print(login.user_login_success())








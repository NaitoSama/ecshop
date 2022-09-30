'''
添加一个user账号
'''
# from common.get_driver import Driver
from selenium.webdriver.common.by import By
from page.login_page import LoginPage  # 需要登录才能添加会员账号
import time
from common.Log import Logging

class AddUserPage(LoginPage):
    def add_user(self,username,mail,password,re_password):
        self.username = username
        self.open()  # 用self调用父类的方法
        self.login('admin','naito1001')
        # 在这里打个日志
        Logging('登录 success')


        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, '#menu-frame'))
        self.driver.find_element(By.CSS_SELECTOR,'li[key="08_members"]').click()
        self.driver.find_element(By.LINK_TEXT,'添加会员').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR,'#main-frame'))
        self.driver.find_element(By.CSS_SELECTOR,'input[name="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="email"]').send_keys(mail)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="confirm_password"]').send_keys(re_password)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

        Logging('add user success')

    def add_user_success(self):
        # self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, '#main-frame'))
        try:
            result = self.driver.find_element(By.XPATH,f'//td[contains(text(),"{self.username}")]').text
            return result
        except:
            return False

if __name__ == '__main__':
    add = AddUserPage()
    add.add_user('test3','test3@test.com','ttest3','ttest3')
    print(add.add_user_success())

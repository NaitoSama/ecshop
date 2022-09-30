'''
添加管理员账号
'''
from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep


class AddAdminUser(LoginPage):
    def switch_to_add_admin_user_window(self):
        # login
        self.open()
        self.login('admin','naito1001')
        # locate admin user manager
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR,'#menu-frame'))
        self.driver.find_element(By.CSS_SELECTOR,'li[key="10_priv_admin"]').click()
        self.driver.find_element(By.LINK_TEXT,'管理员列表').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR,'#main-frame'))
        # to add admin user window
        self.driver.find_element(By.LINK_TEXT,'添加管理员').click()

    def add_admin_user(self,account,email,password,re_password):
        self.account = account
        self.driver.find_element(By.CSS_SELECTOR,'input[name="user_name"]').send_keys(account)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="email"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="pwd_confirm"]').send_keys(re_password)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def add_admin_user_success(self):
        sleep(1)
        try:
            result = self.driver.find_element(By.XPATH,f'//td[contains(text(),"{self.account}")]').text
            if self.account in result:
                return True
            else:
                return False
        except:
            return False

if __name__ == '__main__':
    add = AddAdminUser()
    add.switch_to_add_admin_user_window()
    add.add_admin_user('test321','test321@admin.com','A11111','A11111')
    print(add.add_admin_user_success())







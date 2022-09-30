'''
封装后台的登录的page页面
'''
from common.get_driver import Driver  # 将driver类导入
from selenium.webdriver.common.by import By


class LoginPage(Driver):  # 继承driver
    # 一个动作封装成一个方法
    def open(self):
        self.driver.get('http://localhost/ecshop/admin')

    def login(self, username, password):  # 把账号密码都定义为形参
        '''
        登录的流程
        :param username: 账号
        :param password: 密码
        :return: None
        '''
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="进入管理中心"]').click()

    def login_check(self):
        try:
            self.driver.switch_to.frame('header-frame')
            result = self.driver.find_element(By.XPATH, '//span[text()="退出"]')
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    lp = LoginPage()
    lp.open()
    lp.login('admin', 'naito1001')
    print(lp.login_check())
    lp.driver.quit()

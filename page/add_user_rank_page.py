'''
新增用户等级
'''


from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from selenium.webdriver.common.keys import Keys


class AddUserRankPage(LoginPage):
    def switch_to_user_rank_page(self):
        self.open()
        self.login('admin','naito1001')
        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element(By.CSS_SELECTOR,'li[key="08_members"]').click()
        self.driver.find_element(By.LINK_TEXT,'会员等级').click()
        self.driver.switch_to.default_content()

    def add_user_rank(self,user_rank,max_points,min_points,discount):
        self.driver.switch_to.frame('main-frame')
        self.driver.find_element(By.LINK_TEXT,'添加会员等级').click()
        self.driver.find_element(By.CSS_SELECTOR,'input[name="rank_name"]').send_keys(user_rank)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="min_points"]').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="min_points"]').send_keys(min_points)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="max_points"]').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="max_points"]').send_keys(max_points)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="discount"]').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="discount"]').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="discount"]').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR,'input[name="discount"]').send_keys(discount)
        self.driver.find_element(By.CSS_SELECTOR,'input[value=" 确定 "]').click()

    def add_user_rank_success(self):
        try:
            result = self.driver.find_element(By.XPATH,'//td[contains(text(),"会员等级已经添加成功。")]').text
            return result
        except:
            return False


if __name__ == '__main__':
    add = AddUserRankPage()
    add.switch_to_user_rank_page()
    add.add_user_rank('23','45','12','90')
    print(add.add_user_rank_success())

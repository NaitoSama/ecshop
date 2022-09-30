'''
新增一个拍卖
'''

from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


class AddAuctionPage(LoginPage):
    def switch_to_auction_page(self):
        self.open()
        self.login('admin', 'naito1001')
        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element(By.CSS_SELECTOR, 'li[key="03_promotion"]').click()
        self.driver.find_element(By.LINK_TEXT, '拍卖活动').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('main-frame')

    # def month_select(self, ele, date_month):
    #     for i in range(12):
    #         try:
    #             ele.find_element(By.XPATH, f'//td[contains(text(),"{date_month}")]')
    #             break
    #         except:
    #             ele.find_element(By.CSS_SELECTOR, '.headrow>td:nth-child(2)').click()
    #         if i == 11:
    #             print('Cant find month')
    #             return False
    #
    # def year_select(self, ele, year):
    #     temp = ele.find_element(By.XPATH, '//td[contains(text(),"月")]').text
    #     temp_list = temp.split(',')
    #     a_year = int(temp_list[1])
    #     while True:
    #         if a_year < year:
    #             ele.find_element(By.CSS_SELECTOR, '.headrow>td:nth-child(5)').click()
    #         elif a_year > year:
    #             ele.find_element(By.CSS_SELECTOR, '.headrow>td:nth-child(1)').click()
    #         else:
    #             break
    #
    # def day_select(self, ele, day):
    #     ele.find_element(By.XPATH, f'//td[text()="{day}"]').click()
    #     ele.find_element(By.XPATH, f'//td[text()="{day}"]').click()

    def add_auction(self, auction, description, goods, bdate, edate, starting_price, price, increase_range, bond):
        # bdate_list = bdate.split('-')
        # edate_list = edate.split('-')
        # month_chinese_list = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月',
        #                       '十二月', ]
        # bdate_month = month_chinese_list[int(bdate_list[1]) - 1]
        # edate_month = month_chinese_list[int(edate_list[1]) - 1]

        bdate = bdate.replace(r'/', '-')
        edate = edate.replace(r'/', '-')

        self.driver.find_element(By.LINK_TEXT, '添加拍卖活动').click()
        self.driver.find_element(By.CSS_SELECTOR, '#act_name').send_keys(auction)
        self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="act_desc"]').send_keys(description)
        self.driver.find_element(By.CSS_SELECTOR, '#search').click()
        sel = Select(self.driver.find_element(By.CSS_SELECTOR, '#goods_id'))
        sel.select_by_visible_text(goods)

        js = "document.getElementById('start_time').removeAttribute('readonly')"
        self.driver.execute_script(js)
        js = f'document.getElementById("start_time").value = "{bdate}"'
        self.driver.execute_script(js)

        js = "document.getElementById('end_time').removeAttribute('readonly')"
        self.driver.execute_script(js)
        js = f'document.getElementById("end_time").value = "{edate}"'
        self.driver.execute_script(js)

        # self.driver.find_element(By.CSS_SELECTOR, '#selbtn1').click()
        # sleep(0.5)
        # ele = self.driver.find_element(By.XPATH,'//div[@class="calendar"][1]')
        #
        # self.month_select(ele, bdate_month)
        # self.year_select(ele,int(bdate_list[0]))
        # self.day_select(ele,int(bdate_list[2]))
        #
        # self.driver.find_element(By.CSS_SELECTOR, '#selbtn2').click()
        # sleep(0.5)
        # ele = self.driver.find_element(By.CSS_SELECTOR,'div[class="calendar"]:nth-child(2)')
        #
        # self.month_select(ele, edate_month)
        # self.year_select(ele, int(edate_list[0]))
        # self.day_select(ele, int(edate_list[2]))

        self.driver.find_element(By.CSS_SELECTOR, '#start_price').send_keys(Keys.RIGHT)
        self.driver.find_element(By.CSS_SELECTOR, '#start_price').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR, '#start_price').send_keys(starting_price)

        self.driver.find_element(By.CSS_SELECTOR, '#end_price').send_keys(Keys.RIGHT)
        self.driver.find_element(By.CSS_SELECTOR, '#end_price').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR, '#end_price').send_keys(price)

        self.driver.find_element(By.CSS_SELECTOR, '#amplitude').send_keys(Keys.RIGHT)
        self.driver.find_element(By.CSS_SELECTOR, '#amplitude').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR, '#amplitude').send_keys(increase_range)

        self.driver.find_element(By.CSS_SELECTOR, '#deposit').send_keys(Keys.RIGHT)
        self.driver.find_element(By.CSS_SELECTOR, '#deposit').send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR, '#deposit').send_keys(bond)

        self.driver.find_element(By.CSS_SELECTOR, 'input[value=" 确定 "]').click()

    def add_auction_success(self):
        try:
            result = self.driver.find_element(By.XPATH, '//td[text()="添加拍卖活动成功"]').text
            return result
        except:
            return False


if __name__ == '__main__':
    add = AddAuctionPage()
    add.switch_to_auction_page()
    add.add_auction('213', 'rewewr', '罗技g502', '2022/05/25', '2022-10-25', '50', '200', '10', '10')
    print(add.add_auction_success())

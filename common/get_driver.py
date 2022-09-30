'''
封装获取driver对象的公共方法
'''


class Driver:
    def __init__(self):  # 把获取driver对象的代码封装在构造方法里面
        # 代表只要实例化这个类的对象就会自动调用构造方法，获取到driver对象
        from selenium import webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def driver_quit(self):
        self.driver.quit()


if __name__ == '__main__':  # 每次写完一个页面，都必须要调用一次
    Driver()

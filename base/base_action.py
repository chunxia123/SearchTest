from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    #初始化，打开浏览器，最大化浏览器
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://cn.student.com")
    #查找一个元素
    def base_find_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
    #查找多个元素
    def base_find_elements(self, loc):
        return self.driver.find_elements(*loc)
    #点击
    def base_click(self, loc):
        self.base_find_element(loc).click()
    #输入框输入值
    def base_input(self, loc, txt):
        el = self.base_find_element(loc)
        print(loc)
        el.clear()
        el.send_keys(txt)





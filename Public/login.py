from selenium import webdriver
import time
from xybao.Public.basepage import BasePage
from selenium.webdriver.common.by import By

class login(BasePage):

    username_loc = (By.ID, 'username')
    pwd_loc = (By.ID, 'pwd')
    click_loc = (By.ID, 'a_regist')
    text_loc = (By.ID, 'span_error')

    def __init__(self,selenium_driver,base_url):
        BasePage.__init__(self, selenium_driver, base_url)
        self.open_web(base_url)

    def input_name(self,username):
        self.send_keys(username, *self.username_loc)

    def input_pwd(self,pwd):
        self.send_keys(pwd,*self.pwd_loc)

    def click_login(self):
        self.click(*self.click_loc)

    def login_result_text(self):
        return  self.find_element(*self.text_loc).text

    def xybaologin(self,username,pwd):
        self.send_keys(username,*self.username_loc)
        self.send_keys(pwd,*self.pwd_loc)
        self.click(*self.click_loc)

    def xybaologin_text(self,username,pwd):
        self.send_keys(username,*self.username_loc)
        self.send_keys(pwd,*self.pwd_loc)
        self.click(*self.click_loc)
        time.sleep(1)
        result_text=self.find_element(*self.text_loc).text
        return result_text


# def login(selenium_driver,username,pwd):
#     driver=selenium_driver
#     driver.find_element_by_id("username").clear()
#     driver.find_element_by_id("username").send_keys(username)
#     driver.find_element_by_id("pwd").clear()
#     driver.find_element_by_id("pwd").send_keys(pwd)
#     driver.find_element_by_id('a_regist').click()
#     time.sleep(1)
#     result_text=driver.find_element_by_id("span_error").text
#     return result_text


if __name__=="__main__":
    driver = webdriver.Chrome()
    url="http://xyb.test.xybao.com/login"
    username="18650794798"
    pwd="123"
    x=login(driver,url)
    y=x.xybaologin(username,pwd)
    print(y)

    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("http://xyb.test.xybao.com/login")
    # x=login(driver,"18650794798","123")
    # print("a"+x+"b")

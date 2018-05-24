from selenium import webdriver
import time
from xybao.Public.basepage import BasePage
from selenium.webdriver.common.by import By
from xybao.Public.login import login

class bbgpage(login):

    find_loc  = (By.XPATH, "/html/body/div[3]/div/div[2]/ul/li[2]/a")
    find_loc1 = (By.XPATH, "/html/body/div[5]/div/div[2]/a")
    find_loc2 = (By.XPATH, "/html/body/div[5]/div[2]/table/tbody/tr[2]/td[6]/a")
    find_loc3 = (By.ID, "amount")
    find_loc4 = (By.ID, "invest_now")
    find_loc5 = (By.ID, "agree")
    find_loc6 = (By.ID, "trade_val")
    find_loc7 = (By.ID, "trade_confirm")
    find_loc8= (By.CLASS_NAME, "title-h2")

    def __init__(self, selenium_driver, base_url):
        login.__init__(self, selenium_driver, base_url)
        self.open_web(base_url)
        #
        # self.name="18650794798"
        self.pwd="123456"
    def bbglogin(self,name,pwd):
        self.xybaologin(name,pwd)

    def invest(self,amount):
        self.click(*self.find_loc)
        self.click(*self.find_loc1)
        self.click(*self.find_loc2)
        self.send_keys(amount,*self.find_loc3)
        self.click(*self.find_loc5)
        self.click(*self.find_loc4)

    def send_tradepwd(self):
        self.send_keys(self.pwd,*self.find_loc6)
        self.click(*self.find_loc7)

    def text(self):
        return self.find_element(*self.find_loc8).text

if __name__=="__main__":
    driver = webdriver.Firefox()
    url="http://xyb.test.xybao.com/login"
    amount=1000
    t=bbgpage(driver,url)
    t.bbglogin()
    time.sleep(2)
    t.invest(amount)



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xybao.Public import  logshow
from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

class BasePage(object):

    def __init__(self, selenium_driver, base_url="", page_title=""):
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title
        self.mylog = logshow.log()
        self.img_path=r"C:\Users\admin\PycharmProjects\python\xybao\Screenshot\Screenshot"

    def open_web(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except:
            self.mylog.error(u'未能正确打开页面:' + url)

#     def open_web(self, url, page_title):
#         try:
#             self.driver.get(url)
#             self.driver.maximize_window()
# #           通过断言输入的title是否在当前title中
#             assert page_title in self.driver.title, u'打开页面失败：%s' % url
#         except:
#             self.mylog.error(u'未能正确打开页面:'+url)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.mylog.error(u'找不到元素:'+str(loc))


    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except :
            self.mylog.error(u'输入失败,loc='+str(loc)+u';value='+value)

    def click(self, *loc):
        try:
            self.find_element(*loc).click()
        except :
            self.mylog.error(u'点击失败,loc='+str(loc))

    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(self.img_path+img_name+'.png')
        except:
            self.mylog.error(u'截图失败：'+img_name)

if __name__=="__main__":
    driver=webdriver.Chrome()
    url="https://www.baidu.com/"
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    img_name=now
    print(img_name)
    keywords_loc = (By.ID, 'kw')
    click_loc = (By.ID, 'su1')
    t=BasePage(driver,url)
    t.open_web(url)
    t.send_keys("python",*keywords_loc)
    t.click(*click_loc)
    t.img_screenshot(img_name)
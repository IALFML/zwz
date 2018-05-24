import unittest
from selenium import webdriver
import time
from HTMLTestRunner  import HTMLTestRunner
from xybao.Public import readexcel
from xybao.Public.basepage import BasePage
from selenium.webdriver.common.by import By
listdata=readexcel.excel_data(r"C:\Users\admin\PycharmProjects\python\xybao\Datebase\logindata.xlsx", 0)
from xybao.Public import basepage
from xybao.Public import login

class Xybaologin(unittest.TestCase):
    # username_loc = (By.ID, 'username')
    # pwd_loc = (By.ID, 'pwd')
    # click_loc = (By.ID, 'a_regist')
    # text_loc = (By.ID, 'span_error')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url="http://xyb.test.xybao.com/login"
        cls.login=login.login(cls.driver,cls.url)

    def test_001(cls):
        """正确的用户名和错误的密码"""
        result_text=cls.login.xybaologin_text(listdata[0]['username'],listdata[0]['password'])
        cls.assertEqual(result_text,listdata[0]["expectedresult"])

    def test_002(cls):
        """错误的用户名和正确的密码"""
        result_text=cls.login.xybaologin_text(listdata[1]['username'],listdata[1]['password'])
        cls.assertEqual(result_text,listdata[1]["expectedresult"])

    def test_003(cls):
        """错误的用户名和错误的密码"""
        result_text=cls.login.xybaologin_text(listdata[2]['username'],listdata[2]['password'])
        cls.assertEqual(result_text,listdata[2]["expectedresult"])

    def test_004(cls):
        """正确的用户名和空的密码"""
        result_text=cls.login.xybaologin_text(listdata[3]['username'],listdata[3]['password'])
        cls.assertEqual(result_text,listdata[3]["expectedresult"])

    def test_005(cls):
        """空的用户名和正确的密码"""
        result_text=cls.login.xybaologin_text(listdata[4]['username'],listdata[4]['password'])
        cls.assertEqual(result_text,listdata[4]["expectedresult"])

    def test_006(cls):
        """空的用户名和空的密码"""
        result_text=cls.login.xybaologin_text(listdata[5]['username'],listdata[5]['password'])
        cls.assertEqual(result_text,listdata[5]["expectedresult"])

    def test_007(cls):
        """正确的用户名和正确的密码"""
        cls.login.input_name(listdata[6]['username'])
        cls.login.input_pwd(listdata[6]['password'])
        cls.login.click_login()
        time.sleep(1)
        result_text=cls.driver.current_url
        cls.assertEqual(result_text,listdata[6]["expectedresult"])

    # def test_007(cls):
    #     """正确的用户名和正确的密码"""
    #     cls.login.send_keys(listdata[6]['username'],*cls.username_loc)
    #     cls.login.send_keys(listdata[6]['password'],*cls.pwd_loc)
    #     cls.login.click(*cls.click_loc)
    #     time.sleep(1)
    #     result_text=cls.driver.current_url
    #     cls.assertEqual(result_text,listdata[6]["expectedresult"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    # username_loc = (By.ID, 'username')
    # pwd_loc = (By.ID, 'pwd')
    # click_loc = (By.ID, 'a_regist')
    # text_loc = (By.ID, 'span_error')
    #
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.login=BasePage(cls.driver)
    #     cls.login.open_web("http://xyb.test.xybao.com/login")
    #
    # def test_001(cls):
    #     """正确的用户名和错误的密码"""
    #     cls.login.send_keys(listdata[0]['username'],*cls.username_loc)
    #     cls.login.send_keys(listdata[0]['password'],*cls.pwd_loc)
    #     cls.login.click(*cls.click_loc)
    #     time.sleep(1)
    #     result_text=cls.login.find_element(*cls.text_loc).text
    #     cls.assertEqual(result_text,listdata[0]["expectedresult"])
    #
    # def test_007(cls):
    #     """正确的用户名和正确的密码"""
    #     cls.login.send_keys(listdata[6]['username'],*cls.username_loc)
    #     cls.login.send_keys(listdata[6]['password'],*cls.pwd_loc)
    #     cls.login.click(*cls.click_loc)
    #     time.sleep(1)
    #     result_text=cls.driver.current_url
    #     cls.assertEqual(result_text,listdata[6]["expectedresult"])
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.login=BasePage(self.driver)
    #     self.login.open_web("http://xyb.test.xybao.com/login")
    #
    # def test_001(self):
    #     """正确的用户名和错误的密码"""
    #     self.login.send_keys(listdata[0]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[0]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(1)
    #     result_text=self.login.find_element(*self.text_loc).text
    #     self.assertEqual(result_text,listdata[0]["expectedresult"])

    # def test_002(self):
    #     """错误的用户名和正确的密码"""
    #     self.login.send_keys(listdata[1]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[1]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(1)
    #     result_text=self.login.find_element(*self.text_loc).text
    #     self.assertEqual(result_text,listdata[1]["expectedresult"])
    #
    # def test_003(self):
    #     """错误的用户名和错误的密码"""
    #     self.login.send_keys(listdata[2]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[2]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(1)
    #     result_text=self.login.find_element(*self.text_loc).text
    #     self.assertEqual(result_text,listdata[2]["expectedresult"])
    #
    # def test_004(self):
    #     """正确的用户名和空的密码"""
    #     self.login.send_keys(listdata[3]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[3]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(3)
    #     result_text=self.login.find_element(*self.text_loc).text
    #     self.assertEqual(result_text,listdata[3]["expectedresult"])
    #
    #
    # def test_005(self):
    #     """空的用户名和正确的密码"""
    #     self.login.send_keys(listdata[4]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[4]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(1)
    #     result_text=self.login.find_element(*self.text_loc).text
    #     self.assertEqual(result_text,listdata[4]["expectedresult"])
    #
    # def test_006(self):
    #     """空的用户名和空的密码"""
    #     self.login.send_keys(listdata[5]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[5]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(1)
    #     result_text=self.login.find_element(*self.text_loc).text
    #     self.assertEqual(result_text,listdata[5]["expectedresult"])

    # def test_007(self):
    #     """正确的用户名和正确的密码"""
    #     self.login.send_keys(listdata[6]['username'],*self.username_loc)
    #     self.login.send_keys(listdata[6]['password'],*self.pwd_loc)
    #     self.login.click(*self.click_loc)
    #     time.sleep(1)
    #     result_text=self.driver.current_url
    #     self.assertEqual(result_text,listdata[6]["expectedresult"])
    #
    # def tearDown(self):
    #     self.driver.close()


if __name__=="__main__":
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Xybaologin("test_001"))
    suite.addTest(Xybaologin("test_002"))
    suite.addTest(Xybaologin("test_003"))
    suite.addTest(Xybaologin("test_004"))
    suite.addTest(Xybaologin("test_005"))
    suite.addTest(Xybaologin("test_006"))
    suite.addTest(Xybaologin("test_007"))
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    filename = r'C:\Users\admin\PycharmProjects\python\xybao\Report\Report' + now + '-testresult.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
    runner.run(suite)
    fp.close()

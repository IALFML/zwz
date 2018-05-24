import unittest
from selenium import webdriver
import time
from HTMLTestRunner  import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xybao.Public import login
from xybao.Public import bbgpage




class Xybaobbg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url="http://xyb.test.xybao.com/login"
        cls.login=bbgpage.bbgpage(cls.driver,cls.url)
        cls.name="15479479474"
        cls.pwd="123456"

    def test_001(cls):
        """投资1000元"""
        amount=1000
        cls.login.bbglogin(cls.name,cls.pwd)
        time.sleep(1)
        cls.login.invest(amount)
        time.sleep(1)
        cls.login.send_tradepwd()
        time.sleep(1)
        x=cls.login.text()
        cls.assertEqual(x,"出借成功,正在匹配项目")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Xybaologin("test_001"))
    # suite.addTest(Xybaologin("test_002"))
    # suite.addTest(Xybaologin("test_003"))
    # suite.addTest(Xybaologin("test_004"))
    # suite.addTest(Xybaologin("test_005"))
    # suite.addTest(Xybaologin("test_006"))
    # suite.addTest(Xybaologin("test_007"))
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # filename = r'C:\Users\admin\PycharmProjects\python\xybao\Report\Report' + now + '-testresult.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    # runner.run(suite)
    # fp.close()

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

def createsuite():
    test_dir=r"C:\Users\admin\PycharmProjects\python\xybao\Testcase"
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py",top_level_dir=None)
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_bbg.py", top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit

if __name__=="__main__":

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # filename = 'D:\\' + now + '-testresult.html'
    filename = r'C:\Users\admin\PycharmProjects\python\xybao\Report\Report' + now + '-testresult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(createsuite())
    fp.close()
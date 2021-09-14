from tools.test_http_request import TestHttpRequest
from tools.project_path import *
import unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open(test_report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='接口测试报告',description='这是诺的报告',tester='诺')
    runner.run(suite)
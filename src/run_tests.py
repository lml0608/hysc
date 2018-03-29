# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest
import os
import time
from HTMLTestRunner import HTMLTestRunner

#用例路径

case_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'testcase')
print(case_path)
#报告存放路径
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_report")
print(report_path)


now = time.strftime("%Y_%m_%d %H_%M_%S")

report_abspath=os.path.join(report_path, now+"report.html")


#返回所有用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)

    return discover


all_case()
if __name__ == '__main__':


    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner(
        stream=fp,
        title='这是我的自动化测试报告',
        description='用例执行情况：'
    )
    runner.run(all_case())
    #runner.run(testunit)
    fp.close()

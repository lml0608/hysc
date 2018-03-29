# -*- coding:utf-8 -*-
'''
__author__:liubin

'''
from selenium import webdriver
import time
import logging
import unittest

from src.common.browser import browser

class test001(unittest.TestCase):

    # def __init__(self):
    #
    #     self.logger = logging.getLogger(__name__)

    def setUp(self):

        #self.driver = browser('firefox')
        # binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        # browser = webdriver.Firefox(firefox_binary=binary)
        self.driver =  webdriver.Firefox(executable_path = "D:\\app\\hysc\\src\\tools\\geckodriver.exe")


        self.driver.get("http://www.baidu.com")

        self.driver.implicitly_wait(20)


    def test001(self):


        #self.logger.info("---测试用例开始----")

        self.driver.find_element_by_id("kw").send_keys("selemiu")

        #self.logger.info("输入内容：selenium")

        self.driver.find_element_by_id("su").click()

       # self.logger.info("点击按钮：id=su")

        time.sleep(2)

        t = self.driver.title

        #self.logger.info("获取title内容：%s" % t)

        #self.assertIn("百度搜索",t)
        #assert t == "selemiu_百度搜索"


    def tearDown(self):
        #self.logger.info("-----用例测试结束--------")

        self.driver.quit()



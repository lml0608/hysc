# -*- coding:utf-8 -*-
'''
__author__:liubin

'''
import unittest
from src.pages import login_page
import logging
from src.common.screen import Screen
from src.common.browser import browser

class testlogin(unittest.TestCase):

    driver = browser()

    def __init__(self, *args, **kwargs):
        super(testlogin, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)



    def setUp(self):
        #self.logger.info("---测试用例开始----")

        #self.driver =  webdriver.Firefox(executable_path = "D:\\app\\hysc\\src\\tools\\geckodriver.exe")


        # self.driver.get("http://www.baidu.com")
        #
        # self.driver.implicitly_wait(20)
        #self.driver.save_screenshot('screenshot.png')

        self.url = 'http://portaltest.wgmf.com/index.html'



    @Screen(driver)
    def testlogin01(self):

        login = login_page.LoginPage(self.driver)

        login.open(self.url)
        login.login()

        #assert t == "selemiu_百度搜索"


    def tearDown(self):
        self.logger.info("-----用例测试结束--------")

        self.driver.quit()

#
# if __name__ == "__main__":
#
#     unittest.main()




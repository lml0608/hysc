# -*- coding:utf-8 -*-
'''
__author__:liubin

'''
import traceback
import unittest
import logging
from src.pages import login_page
from src.common.browser import browser

class testlogin(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(testlogin, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    def setUp(self):
        self.logger.info("---测试用例开始----")

        self.driver = browser('chrome')

        self.url = 'http://portaltest.wgmf.com/index.html'


    def testlogin01(self):
        try:
            login = login_page.LoginPage(self.driver)
            login.open()
            login.login()
            self.logger.info(login.user_name.text)
            self.assertEqual(login.user_name.text, '向玉清')
        except Exception:
            traceback.print_exc()
            login.get_scrennshot()

    def tearDown(self):
        self.logger.info("-----用例测试结束--------")
        self.driver.quit()


if __name__ == "__main__":

    unittest.main()




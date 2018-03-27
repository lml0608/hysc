# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from  src.common import browser

from src.pages.xianshi_page import XianShi

from src.pages.login_page import LoginPage

import time


class testxianshi(object):



    def setUp(self):


        self.driver = browser.browser('firefox')

        time.sleep(5)



    def test003(self):


        login = LoginPage(self.driver)
        time.sleep(3)
        xs = XianShi(self.driver)

        login.get_url()
        time.sleep(2)
        login.login()
        time.sleep(5)

        xs.add_xiashi()


        time.sleep(10)






    def tearDown(self):
        self.driver.quit()




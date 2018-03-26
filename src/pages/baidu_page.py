# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from .base import BasePage

from selenium.webdriver.common.by import By
import logging


class BaiduPage(BasePage):



    def __init__(self,driver):

        BasePage.__init__(self, driver)

        #self.logger = logging.getLogger(__name__)



    search_box = (By.ID,'kw')

    search_ok = (By.ID,'su')


    def open_url(self):
        self.open(self.url)


    def input_search(self,key_word):

        self.send_keys(self.search_box,key_word)
        #self.logger.info("输入内容：%s" % key_word)

    def click_search(self):

        self.click(self.search_ok)

        #self.logger.info("点击按钮：id=su")




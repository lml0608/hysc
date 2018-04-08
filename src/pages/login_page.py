# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from selenium.webdriver.common.by import By
from .basepage import BasePage
import time
import logging


class LoginPage(BasePage):
    ''''登录'''



    # #登陆元素
    # login_button = (By.ID, "loginShow")
    #
    # staff_input = (By.ID, "staff_id1")
    #
    # password_input = (By.ID, "password")
    #
    # sub_button = (By.CLASS_NAME, "sub1")
    #
    # #进入商城管理
    # manager_button = (By.XPATH, "//div[@class='my_nav']/div/ul/li[4]/a")



    def __init__(self,driver):

        BasePage.__init__(self, driver)

        self.logger = logging.getLogger(__name__)

    locator_dictionary = {
        "login_button": (By.ID, 'loginShow'),
        "staff": (By.ID, 'staff_id1'),
        "passwd": (By.ID, 'password'),
        "sub_button": (By.CLASS_NAME, 'sub'),
        "manager_button":(By.XPATH,"//div[@class='my_nav']/div/ul/li[4]/a")
    }


    #打开浏览器
    def get_url(self):

        self.open()
        time.sleep(5)


    def login(self,staff_id='449',password='449'):
        '''
        登陆并切换到运营商城
        :param staff_id: 
        :param password: 
        :return: 
        '''
        # 弹出登陆框


        self.click(self.locator_dictionary['login_button'])
        self.logger.info("-----------点击登陆商城----------------")



        # 输入工号
        self.send_keys(self.locator_dictionary['staff'], staff_id)
        self.logger.info("-----------输入员工工号----------------")


        # 输入密码
        self.send_keys(self.locator_dictionary['passwd'], password)
        self.logger.info("-----------输入登陆密码----------------")


        # 点击登陆按钮

        self.click(self.locator_dictionary['sub_button'])
        self.logger.info("-----------点击登陆按钮----------------")

        #打开运营管理中心
        self.click(self.locator_dictionary['manager_button'])
        #self.log.info("------------切换到运营商城---------------")


        time.sleep(10)



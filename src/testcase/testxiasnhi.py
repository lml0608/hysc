# # -*- coding:utf-8 -*-
# '''
# __author__:liubin
#
# '''
# import time
# import unittest
# import logging
# from src.common import browser
# from src.pages.xianshi_page import XianShi
# from src.pages.login_page import LoginPage
#
#
#
# class testxianshi(unittest.TestCase):
#
#     def __init__(self, *args, **kwargs):
#         super(testxianshi, self).__init__(*args, **kwargs)
#         self.logger = logging.getLogger(__name__)
#
#     def setUp(self):
#         self.driver = browser.browser('chrome')
#
#     def test003(self):
#
#         login = LoginPage(self.driver)
#         time.sleep(3)
#         xs = XianShi(self.driver)
#         #打开ULR
#         login.get_url()
#         time.sleep(2)
#         #登陆
#         login.login()
#         time.sleep(5)
#         #添加秒杀
#         xs.add_xiashi()
#
#
#         time.sleep(10)
#
#
#
#
#
#
#     def tearDown(self):
#         self.driver.quit()
#
#
#

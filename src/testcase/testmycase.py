#
# from testconfig import config
#
# import logging
#
# from src.common.screen import Screen
# from selenium import webdriver
#
# class testMyCase(object):
#
#     driver = webdriver.Firefox(executable_path='D:\\app\\hysc\\src\\tools\\geckodriver.exe')
#
#     def __init__(self):
#
#         self.logger = logging.getLogger(__name__)
#
#     def setUp(self):
#
#         self.package = config['appPackage']
#
#         self.logger.debug('setup---15')
#
#         print('setup function')
#
#     def tearDown(self):
#         self.logger.debug('teardown---20')
#
#         print(self.package)
#         print('teardown function')
#     @Screen(driver)
#     def testcase(self):
#
#         self.logger.debug('test----25')
#
#         assert 1==1
#
#     def testcase2(self):
#
#         #packageName = config['appPackage']
#         #print(packageName)
#         self.logger.warning('test2----33')
#         assert 2==2
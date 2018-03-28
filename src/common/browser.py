# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import os

from selenium import webdriver


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ChromePath = os.path.join(BASE_DIR,'tools/chromedriver.exe')

FireFoxPath = os.path.join(BASE_DIR,'tools/geckodriver.exe')


def browser(browser='firefox'):
    ''''打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"'''

    try:

        if browser == "firefox":

            driver = webdriver.Firefox(executable_path=FireFoxPath)
            return driver

        elif browser == "chrome":

            driver = webdriver.Chrome(executable_path=ChromePath)
            return driver

        elif browser == "ie":
            driver = webdriver.Ie()
            return driver

        elif browser == "phantomjs":

            driver = webdriver.PhantomJS()
            return driver

        else:

            print("Not found this browser, You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:

        print("%s" % msg)




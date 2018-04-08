# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from src.common.browser import browser


from src.pages.login_page1 import LoginPage1

def test_login1():

    url = "http://automationpractice.com/index.php"
    br = browser("chrome")
    page = LoginPage1(br)
    page.visit(url)

    page.email.send_keys("abc@xyz.com")
    page.password.send_keys("Test@123")
    page.signin_button.click()

    print(page.email)

test_login1()
__author__ = 'pmacharl'
from selenium.webdriver.common.by import By
from src.pages.base_page_object import BasePage


class LoginPage1(BasePage):
    def __init__(self,browser):
        BasePage.__init__(
            self,
            browser)

    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "signin_button": (By.ID, 'SubmitLogin')
    }


    # def login(self,username="abc@xyz.com",passwd="Test@123"):
    #     self.find_element(*self.locator_dictionary['email']).send_keys(username)
    #     self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
    #     self.find_element(*self.locator_dictionary['signin_button']).click()


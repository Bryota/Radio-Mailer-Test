import time

from termcolor import colored

import chromedriver_binary
from selenium import webdriver


class LoginTest(object):
    def __init__(self, driver='', current_url=''):
        self.driver = webdriver.Chrome()
        self.driver.get('https://radiomailapp.web.app/login')
        self.current_url = self.driver.current_url
        self.login()


    def login(self):
        self.driver.find_element_by_id('email').send_keys('test13@test.com')
        self.driver.find_element_by_id('password').send_keys('password123')
        self.driver.find_element_by_css_selector('.login_btn').click()
        time.sleep(5)

    def get_current_url(self):
        self.current_url = self.driver.current_url

    def check_login_url(self):
        self.get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/'):
            print(colored('テストに成功しました。', 'green'))
        else:
            print(colored('テストに失敗しました。', 'red'))
            print(self.current_url)


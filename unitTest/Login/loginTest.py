import time

from termcolor import colored

import chromedriver_binary
from selenium import webdriver

from unitTest.Base import Base


class LoginTest(Base):
    def __init__(self, driver='', current_url=''):
        super().__init__()

    def check_login_url(self):
        super().get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/'):
            print(colored('テストに成功しました。', 'green'))
        else:
            print(colored('テストに失敗しました。', 'red'))
            print(self.current_url)


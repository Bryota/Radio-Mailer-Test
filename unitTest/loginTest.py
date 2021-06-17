import time

from termcolor import colored

import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://radiomailapp.web.app/login')


def loginTest():
    driver.find_element_by_id('email').send_keys('test13@test.com')
    driver.find_element_by_id('password').send_keys('password123')
    driver.find_element_by_css_selector('.login_btn').click()
    time.sleep(5)
    current_url = driver.current_url
    if (current_url == 'https://radiomailapp.web.app/'):
        print(colored('テストに成功しました。', 'green'))
    else:
        print(colored('テストに失敗しました。', 'red'))
        print(current_url)

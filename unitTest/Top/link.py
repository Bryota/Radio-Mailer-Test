import time
import chromedriver_binary
from termcolor import colored
from selenium import webdriver


class Link(object):
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

    def check_page(self, link_text, slug):
        self.driver.find_element_by_link_text(link_text).click()
        self.get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/{}'.format(slug)):
            print('{}ページのテストに成功しました'.format(slug))
            self.driver.back()
        else:
            print('{}ページのテストに失敗しました'.format(slug))
            print(self.current_url)
            exit()

    def check_pages(self):
        self.check_page('投稿する', 'mail')
        self.check_page('未送信のメール', 'save')
        self.check_page('過去の投稿', 'list')
        self.check_page('番組表', 'program')
        self.check_page('設定', 'setting')
        self.check_page('お問い合わせ', 'request')




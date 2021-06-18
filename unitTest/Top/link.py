import time
import chromedriver_binary
from termcolor import colored
from selenium import webdriver

from unitTest.Base import Base


class Link(Base):
    def __init__(self):
        super().__init__()

    def check_page(self, link_text, slug):
        self.driver.find_element_by_link_text(link_text).click()
        super().get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/{}'.format(slug)):
            print(colored('{}ページのテストに成功しました'.format(slug), 'green'))
            self.driver.back()
        else:
            print(colored('{}ページのテストに失敗しました'.format(slug), 'red'))
            print(self.current_url)
            exit()

    def check_pages(self):
        self.check_page('投稿する', 'mail')
        self.check_page('未送信のメール', 'save')
        self.check_page('過去の投稿', 'list')
        self.check_page('番組表', 'program')
        self.check_page('設定', 'setting')
        self.check_page('お問い合わせ', 'request')




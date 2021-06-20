import time

from termcolor import colored

from unitTest.Base import Base


class UserInfo(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('設定').click()
        self.driver.find_element_by_css_selector('.setting_user_btn_wrap').click()

    def check_form_navigation(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        test_text = self.driver.find_element_by_css_selector('#name-label').text
        if (test_text != '本名'):
            print(colored('1ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.next_btn').click()
        test_text = self.driver.find_element_by_css_selector('#portalCode-label').text
        if (test_text != '郵便番号（ハイフン無し）'):
            print(colored('2ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        test_text = self.driver.find_element_by_css_selector('#name-label').text
        if (test_text != '本名'):
            print(colored('3ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        test_text = self.driver.find_element_by_css_selector('#radioName-label').text
        if (test_text != 'ラジオネーム'):
            print(colored('2ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        print(colored('フォームの遷移ボタンのテストに成功しました', 'green'))

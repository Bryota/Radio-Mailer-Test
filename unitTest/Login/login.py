import time

from termcolor import colored
import chromedriver_binary
from selenium import webdriver

from unitTest.Base import Base


class Login(Base):
    def __init__(self, driver='', current_url=''):
        self.driver = webdriver.Chrome()
        self.driver.get('https://radiomailapp.web.app/login')
        self.current_url = self.driver.current_url

    def check_login(self):
        self.driver.find_element_by_id('email').send_keys('test13@test.com')
        self.driver.find_element_by_id('password').send_keys('password123')
        self.driver.find_element_by_css_selector('.login_btn').click()
        time.sleep(5)
        super().get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/'):
            print(colored('ログインテストに成功しました。', 'green'))
        else:
            print(colored('ログインテストに失敗しました。', 'red'))
            print(self.current_url)

    def check_validation(self):
        self.driver.find_element_by_css_selector('.login_btn').click()
        time.sleep(3)
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'メールアドレスを正しく入力してください'):
            print(colored('メールアドレスのバリデーションが正しく機能していません', 'red'))
            exit()
        self.driver.find_element_by_id('email').send_keys('testtest@test.com')
        self.driver.find_element_by_id('password').send_keys('password')
        self.driver.find_element_by_css_selector('.login_btn').click()
        time.sleep(2)
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'アカウントが存在しません。メールアドレスとパスワードをご確認ください'):
            print(colored('登録されていないメールアドレスのバリデーションが正しく機能していません', 'red'))
            exit()
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_id('email').send_keys('test13@test.com')
        self.driver.find_element_by_css_selector('.login_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'パスワードを正しく入力してください'):
            print(colored('パスワードのバリデーションが正しく機能していません', 'red'))
            exit()
        print(colored('バリデーションテストが完了しました', 'green'))

    def check_link(self):
        self.driver.find_element_by_link_text('パスワードを忘れた方').click()
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/resetPassword'):
            print(colored('リセットパスワードのページが正しく機能していません', 'red'))
            exit()
        self.driver.back()
        self.driver.find_element_by_link_text('Sign Up').click()
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/register'):
            print(colored('登録ページが正しく機能していません', 'red'))
            exit()
        self.driver.back()
        print(colored('リンクテストが完了しました', 'green'))







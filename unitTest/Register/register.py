import time

from termcolor import colored
import chromedriver_binary
from selenium import webdriver

from unitTest.Base import Base


class Register(Base):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://radiomailapp.web.app/register')
        self.current_url = self.driver.current_url

    def check_form_navigation(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        text = self.driver.find_element_by_css_selector('#addressForRadio-label').text
        if (text != '住所（読まれる用）'):
            print(colored('1ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.next_btn').click()
        text = self.driver.find_element_by_css_selector('#tel-label').text
        if (text != '電話番号'):
            print(colored('2ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        text = self.driver.find_element_by_css_selector('#addressForRadio-label').text
        if (text != '住所（読まれる用）'):
            print(colored('3ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        text = self.driver.find_element_by_css_selector('#radioName-label').text
        if (text != 'ラジオネーム'):
            print(colored('2ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        print(colored('ページネーションテストが完了しました', 'green'))

    def check_register(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.submit_btn').click()
        time.sleep(3)
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'メールアドレスを正しく入力してください'):
            print(colored('メールアドレスのバリデーションが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        self.driver.find_element_by_css_selector('.back_btn').click()
        self.driver.find_element_by_css_selector('#email').send_keys('test13@test.com')
        self.driver.find_element_by_css_selector('#password').send_keys('test')
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.submit_btn').click()
        time.sleep(3)
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'パスワードは6文字以上設定してください'):
            print(colored('パスワードのバリデーションが正しく動いていません', 'red'))
            exit()
        self.driver.refresh()
        self.driver.find_element_by_css_selector('#email').send_keys('test13@test.com')
        self.driver.find_element_by_css_selector('#password').send_keys('testpassword')
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.submit_btn').click()
        time.sleep(3)
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'メールアドレスが既に使われています'):
            print(colored('登録済のメールアドレスのバリデーションが正しく動いていません', 'red'))
            exit()
        print(colored('登録テストが完了しました', 'green'))

    def check_link(self):
        self.driver.find_element_by_link_text('Sign In').click()
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/login'):
            print(colored('ログインページが正しく機能していません', 'reIn'))
            exit()
        self.driver.back()
        print(colored('リンクテストが完了しました', 'green'))






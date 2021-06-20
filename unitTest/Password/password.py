import time

from termcolor import colored

from unitTest.Base import Base


class Password(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('設定').click()
        self.driver.find_element_by_css_selector('.setting_password_btn_wrap').click()

    def check_form_navigation(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        test_text = self.driver.find_element_by_css_selector('#newPassword-label').text
        if (test_text != '新しいパスワード *'):
            print(colored('1ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        test_text = self.driver.find_element_by_css_selector('#oldEmail-label').text
        if (test_text != '現在のメールアドレス *'):
            print(colored('2ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        print(colored('フォームの遷移ボタンのテストに成功しました', 'green'))

    def check_validation(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.change_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'メールアドレスを正しく入力してください(現在のメールアドレス・パスワード)'):
            print(colored('現在のメールアドレスのバリデーションが正しく機能していません（無記入）', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        self.driver.find_element_by_id('oldEmail').send_keys('test')
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.change_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'メールアドレスを正しく入力してください(現在のメールアドレス・パスワード)'):
            print(colored('現在のメールアドレスのバリデーションが正しく機能していません（不当なメールアドレス）', 'red'))
            exit()
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_id('oldEmail').send_keys('test13@test.com')
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.change_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'パスワードを正しく入力してください(現在のメールアドレス・パスワード)'):
            print(colored('現在のパスワードのバリデーションが正しく機能していません（不当なパスワード）', 'red'))
            exit()
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_id('oldEmail').send_keys('test13@test.com')
        self.driver.find_element_by_id('oldPassword').send_keys('password123')
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.change_btn').click()
        time.sleep(2)
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'パスワードは6文字以上設定してください(新しいパスワード）'):
            print(colored('新しいパスワードのバリデーションが正しく機能していません（不当なパスワード）', 'red'))
            exit()
        print(colored('バリデーションのテストが完了しました', 'green'))






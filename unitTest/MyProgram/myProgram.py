import time

from termcolor import colored

from unitTest.Base import Base


class MyProgram(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('設定').click()
        self.driver.find_element_by_css_selector('.myprogram_btn_wrap').click()

    def check_validation(self):
        self.driver.find_element_by_css_selector('.myProgram_set_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != '番組名は必須です'):
            print(colored('番組名のバリデーションが正しく機能していません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('#programName').send_keys('test')
        self.driver.find_element_by_css_selector('.myProgram_set_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'メールアドレスを正しく入力してください'):
            print(colored('番組メールアドバイスのバリデーションが正しく機能していません', 'red'))
            exit()
        print(colored('バリデーションテストが完了しました', 'green'))






import time

from termcolor import colored

from unitTest.Base import Base


class Template(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('設定').click()
        self.driver.find_element_by_css_selector('.template_btn_wrap').click()

    def check_validation(self):
        self.driver.find_element_by_css_selector('.template_set_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'テンプレート名を入力して下さい'):
            print(colored('テンプレート名のバリデーションが正しく機能していません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('#templateName').send_keys('test')
        if (self.driver.find_elements_by_css_selector('.error')):
            print(colored('テンプレート名の入力バリデーションが正しく機能していません', 'red'))
        self.driver.find_element_by_css_selector('.template_set_btn').click()
        error_text = self.driver.find_element_by_css_selector('.error').text
        if (error_text != 'テンプレート内容を入力して下さい'):
            print(colored('テンプレート内容のバリデーションが正しく機能していません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('#template').send_keys('test')
        if (self.driver.find_elements_by_css_selector('.error')):
            print(colored('テンプレート内容の入力バリデーションが正しく機能していません', 'red'))
        print(colored('バリデーションテストが完了しました', 'green'))






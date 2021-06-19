import time

from termcolor import colored

from unitTest.Base import Base


class Setting(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('設定').click()

    def check_link(self, class_name, slug):
        self.driver.find_element_by_css_selector('.{}'.format(class_name)).click()
        super().get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/{}'.format(slug)):
            print(colored('{}ページのテストに成功しました'.format(slug), 'green'))
            self.driver.back()
        else:
            print(colored('{}ページのテストに失敗しました'.format(slug), 'red'))
            print(self.current_url)
            exit()

    def check_links(self):
        self.check_link('setting_user_btn_wrap', 'user')
        self.check_link('setting_password_btn_wrap', 'password')
        self.check_link('template_btn_wrap', 'template')
        self.check_link('myprogram_btn_wrap', 'myprogram')

    def check_logout(self):
        self.driver.find_element_by_css_selector('.setting_logout_btn_wrap').click()
        time.sleep(3)
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/login'):
            print(colored('ログアウトが正しく機能していません', 'red'))
            exit()
        print(colored('ログアウトテストが完了しました', 'green'))

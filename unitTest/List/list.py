import time

from termcolor import colored

from unitTest.Base import Base


class List(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('過去の投稿').click()
        time.sleep(3)

    def check_single_page(self):
        self.driver.find_element_by_css_selector('.program_listnav_item').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.arrow_icon').click()
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/single/RFRhNBSrvB88jUsKLelF'):
            print(colored('個別ページへのリンクが正しく機能していません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.single_btn').click()
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/list'):
            print(colored('個別ページの戻るボタンが正しく機能していません', 'red'))
            exit()
        print(colored('個別ページへのリンクテストが完了しました', 'green'))

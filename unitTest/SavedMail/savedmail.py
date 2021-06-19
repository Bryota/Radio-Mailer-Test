import time

from termcolor import colored

from unitTest.Base import Base


class SavedMail(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('未送信のメール').click()
        time.sleep(3)

    def check_single_page(self):
        self.driver.find_element_by_css_selector('.arrow_icon').click()
        super().get_current_url()
        if (self.current_url != 'https://radiomailapp.web.app/single/H3d5KiZHleSmvRC1LWLg'):
            print(colored('個別ページへのリンクが正しく機能していません', 'red'))
            exit()
        print(colored('個別ページへのリンクテストが完了しました', 'green'))

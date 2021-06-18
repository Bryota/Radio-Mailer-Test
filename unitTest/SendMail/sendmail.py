from termcolor import colored

from unitTest.Base import Base


class SendMail(Base):
    def __init__(self):
        super().__init__()

    def check_to_form_page(self):
        self.driver.find_element_by_link_text('投稿する').click()
        self.driver.find_element_by_link_text('入力する').click()
        super().get_current_url()
        if (self.current_url == 'https://radiomailapp.web.app/form'):
            print(colored('sendmailのテストに成功しました。', 'green'))
        else:
            print(colored('sendmailのテストに失敗しました。', 'red'))
            print(self.current_url)

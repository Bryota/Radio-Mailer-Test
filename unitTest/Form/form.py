import time

from termcolor import colored
from selenium.webdriver.support.select import Select

from unitTest.Base import Base


class Form(Base):
    def __init__(self):
        super().__init__()
        self.go_to_page()

    def go_to_page(self):
        self.driver.find_element_by_link_text('投稿する').click()
        self.driver.find_element_by_link_text('入力する').click()

    def check_btn_pagination(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        title = self.driver.find_element_by_css_selector('.form_title').text
        if (title != '投稿情報'):
            print(colored('1ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.next_btn').click()
        title = self.driver.find_element_by_css_selector('.form_title').text
        if (title != '投稿内容'):
            print(colored('2ページ目のnextボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        title = self.driver.find_element_by_css_selector('.form_title').text
        if (title != '投稿情報'):
            print(colored('3ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.back_btn').click()
        title = self.driver.find_element_by_css_selector('.form_title').text
        if (title != 'ユーザー個人情報'):
            print(colored('2ページ目のbackボタンが正しく動いていません', 'red'))
            exit()
        print(colored('フォームの遷移ボタンのテストに成功しました', 'green'))

    def check_set_user_info(self):
        self.driver.find_element_by_css_selector('.set_info_btn').click()
        time.sleep(3)
        name = self.driver.find_element_by_css_selector('#name').get_attribute("value")
        if (name != 'テスト'):
            print(colored('氏名がセットされていません', 'red'))
            exit()
        portalCode = self.driver.find_element_by_css_selector('#portalCode').get_attribute("value")
        if (portalCode != '1111111'):
            print(colored('郵便番号がセットされていません', 'red'))
            exit()
        address = self.driver.find_element_by_css_selector('#address').get_attribute("value")
        if (address != '東京都港区港'):
            print(colored('住所がセットされていません', 'red'))
            exit()
        tel = self.driver.find_element_by_css_selector('#tel').get_attribute("value")
        if (tel != '0000000000'):
            print(colored('電話番号がセットされていません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.next_btn').click()
        mail = self.driver.find_element_by_css_selector('#mail').get_attribute("value")
        if (mail != 'test13@test.com'):
            print(colored('メールアドレスがセットされていません', 'red'))
            exit()
        radioName = self.driver.find_element_by_css_selector('#radioName').get_attribute("value")
        if (radioName != 'テストイヤー'):
            print(colored('ラジオネームがセットされていません', 'red'))
            exit()
        addressForRadio = self.driver.find_element_by_css_selector('#addressForRadio').get_attribute("value")
        if (addressForRadio != '東京都新宿区'):
            print(colored('住所（読まれる用）がセットされていません', 'red'))
            exit()
        age = self.driver.find_element_by_css_selector('#age').get_attribute("value")
        if (age != '26'):
            print(colored('年齢がセットされていません', 'red'))
            exit()
        print(colored('ユーザー情報セットのテストが完了しました', 'green'))

    def check_program_btn(self):
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.set_info_btn').click()
        program_type = self.driver.find_element_by_css_selector('#program').text
        if (program_type != 'マイ番組'):
            print(colored('マイ番組に切り替えができません', 'red'))
            exit()
        self.driver.find_element_by_css_selector('.set_info_btn').click()
        program_type = self.driver.find_element_by_css_selector('#program').text
        if (program_type != '番組'):
            print(colored('標準番組に切り替えができません', 'red'))
            exit()
        print(colored('番組切り替えのテストが完了しました', 'green'))

    def check_validation(self):
        # メールアドレス未入力
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.set_info_btn').click()
        validation_text = self.driver.find_element_by_css_selector('.error').text
        if (validation_text != 'メールアドレスを正しく入力してください'):
            print(colored('メールアドレスのバリデーションが正しく表示されません', 'red'))
            exit()
        # 番組未入力
        self.driver.find_element_by_css_selector('.back_btn').click()
        self.driver.find_element_by_css_selector('.back_btn').click()
        self.driver.find_element_by_css_selector('.set_info_btn').click()
        self.driver.find_element_by_css_selector('.next_btn').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('.next_btn').click()
        self.driver.find_element_by_css_selector('.set_info_btn').click()
        validation_text = self.driver.find_element_by_css_selector('.error').text
        if (validation_text != '番組を選択してください'):
            print(colored('番組のバリデーションが正しく表示されません', 'red'))
            exit()
        # 番組以降の入力もどうにかしたい
        print(colored('フォームバリデーションのテストが完了しました', 'green'))


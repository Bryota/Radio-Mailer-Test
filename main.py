from selenium import webdriver

from unitTest.Login import loginTest
from unitTest.Top import link
from unitTest.SendMail import sendmail
from unitTest.Form import form
from unitTest.SavedMail import savedmail
from unitTest.List import list

def main():
    # ログイン画面
    # login = loginTest.LoginTest()
    # login.check_login_url()

    # トップ画面
    # Top = link.Link()
    # Top.check_pages()

    # メール送信ページ
    # sendmailTest = sendmail.SendMail()
    # sendmailTest.check_to_form_page()

    # フォームページ
    # formTest = form.Form()
    # formTest.check_btn_pagination()
    # formTest.check_set_user_info()
    # formTest.check_program_btn()
    # formTest.check_validation()

    # 未送信のメールページ
    # savedMailTest = savedmail.SavedMail()
    # savedMailTest.check_single_page()

    # 過去の投稿ページ
    listTest = list.List()
    listTest.check_single_page()


if __name__ == '__main__':
    main()

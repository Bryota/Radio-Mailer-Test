from selenium import webdriver

from unitTest.Login import login
from unitTest.Top import link
from unitTest.SendMail import sendmail
from unitTest.Form import form
from unitTest.SavedMail import savedmail
from unitTest.List import list
from unitTest.Setting import setting
from unitTest.UserInfo import userInfo
from unitTest.Password import password
from unitTest.Template import template
from unitTest.MyProgram import myProgram

def main():
    # ログイン画面
    loginTest = login.Login()
    # loginTest.check_login()
    # loginTest.check_validation()
    loginTest.check_link()

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
    # listTest = list.List()
    # listTest.check_single_page()

    # 設定ページ
    # settingTest = setting.Setting()
    # settingTest.check_links()
    # settingTest.check_logout()

    # ユーザー情報ページ
    # userInfoTest = userInfo.UserInfo()
    # userInfoTest.check_form_navigation()

    # パスワード変更ページ
    # passwordTest = password.Password()
    # passwordTest.check_form_navigation()
    # passwordTest.check_validation()

    # テンプレートページ
    # templateTest = template.Template()
    # templateTest.check_validation()

    # マイ番組ページ
    # myProgramTest = myProgram.MyProgram()
    # myProgramTest.check_validation()


if __name__ == '__main__':
    main()

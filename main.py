from unitTest.Login import loginTest
from unitTest.Top import link

from selenium import webdriver


def main():
    # ログイン画面
    # login = loginTest.LoginTest()
    # login.check_login_url()

    # トップ画面
    Top = link.Link()
    Top.check_pages()


if __name__ == '__main__':
    main()

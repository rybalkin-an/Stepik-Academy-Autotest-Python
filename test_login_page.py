from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_user_can_register(browser,):
    login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage( browser, login_link )
    login_page.open()
    login_page.register_new_user()
    login_page.should_be_authorized_user()
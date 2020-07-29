import pytest
from pages.login_page import LoginPage, path
from constants import BASE_URL


def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, BASE_URL+path)
    page.open()
    page.should_be_login_page()


def test_user_can_register(browser):
    login_page = LoginPage(browser, BASE_URL+path)
    login_page.open()
    login_page.register_new_user()
    login_page.should_be_authorized_user()


# V. Регистрация нового пользователя с некорректным форматом почтового ящика, с адресом не содержащим @
@pytest.mark.need_review_custom_scenarios
def test_user_cant_register_with_not_valid_email(browser):
    login_page = LoginPage(browser, BASE_URL+path)
    login_page.open()
    login_page.register_new_user_with_not_valid_email()

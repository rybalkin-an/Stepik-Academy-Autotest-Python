import pytest
from pages.product_page import ProductPage, path
from pages.login_page import LoginPage
from pages.main_page import MainPage
from helper import setup_user_register
from constants import BASE_URL


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, BASE_URL+path)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, BASE_URL+path)
    product_page.open()
    product_page.product_can_be_added_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, BASE_URL+path)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


@pytest.mark.need_review_custom_scenarios
def test_user_can_add_product_to_basket(browser):
    setup_user_register(browser)
    product_page = ProductPage(browser, BASE_URL+path)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


@pytest.mark.xfail
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, BASE_URL+path)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


# IV. Написание отзыва в карточке товара
@pytest.mark.xfail
@pytest.mark.need_review_custom_scenarios
def test_guest_can_write_a_review(browser):
    product_page = ProductPage(browser, BASE_URL+path)
    product_page.open()
    product_page.should_be_write_a_review_button()
    product_page.click_add_review_button()
    product_page.fill_up_a_review_form()
    product_page.should_be_thanks_for_the_review()

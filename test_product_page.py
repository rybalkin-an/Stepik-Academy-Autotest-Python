import pytest
from pages.product_page import ProductPage
from test_login_page import test_user_can_register


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.product_can_be_added_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    test_user_can_register(browser)
    product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


# def test_guest_cant_see_product_in_basket_opened(browser):

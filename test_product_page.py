import pytest
from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page_link = link
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.product_can_be_added_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page_link = link
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


@pytest.mark.need_review_custom_scenarios
def test_user_can_add_product_to_basket(browser):
    product_page_link = link
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.click_add_to_basket_button()


# def test_guest_cant_see_product_in_basket_opened(browser):
#    product_page_link = link
#    product_page = ProductPage(browser, product_page_link)
#    product_page.open()

# IV. Написание отзыва в карточке товара
@pytest.mark.xfail
@pytest.mark.need_review_custom_scenarios
def test_guest_can_write_a_review(browser):
    product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.should_be_write_a_review_button()
    product_page.click_add_review_button()
    product_page.fill_up_a_review_form()
    product_page.should_be_thanks_for_the_review()

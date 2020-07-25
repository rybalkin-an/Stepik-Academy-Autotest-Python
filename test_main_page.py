import pytest
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


# I. Элементы главного меню должны отображаться на языке, выбранном в меню выбора языка
@pytest.mark.need_review_custom_scenarios
def test_main_menu_should_be_in_selected_language(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = MainPage(browser, link)
    page.open()
    page.guest_select_ru_language()
    page.should_be_menu_in_ru_language()


# II. При добавлении товара с типом Книга в корзину из каталога,
# под заголовком “Все товары” появляется сообщение %itemname% был добавлен в вашу корзину
@pytest.mark.need_review_custom_scenarios
def test_user_add_item_to_basket_from_catalogue(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = MainPage(browser, link)
    page.open()
    page.add_item_to_basket_from_catalogue()
    page.should_be_item_is_added_basket_message()

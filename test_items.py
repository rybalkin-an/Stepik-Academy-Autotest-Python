import time


def test_customer_should_see_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    language_actual_result = browser.find_element_by_xpath(
    "//form[@id='add_to_basket_form']//button[contains(@type,'submit')]")
    time.sleep(10)
    add_to_basket_button_is_active = language_actual_result.is_enabled()
    assert add_to_basket_button_is_active == True, \
            f"Such an error, 'add to basket' is not rendered"


def test_customer_should_see_add_to_basket_button_2(browser):
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/")
    language_actual_result = browser.find_element_by_xpath(
    "//form[@id='add_to_basket_form']//button[contains(@type,'submit')]")
    time.sleep(10)
    add_to_basket_button_is_active = language_actual_result.is_enabled()
    assert add_to_basket_button_is_active == True, \
            f"Such an error, 'add to basket' is not rendered"
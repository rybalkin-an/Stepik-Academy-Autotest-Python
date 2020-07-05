import time


def test_customer_should_see_add_to_basket_button(browser):
    browser.find_element_by_xpath("//form[@id='add_to_basket_form']//button[contains(@type,'submit')]")
    time.sleep(30)
    language_actual_result = browser.find_element_by_xpath(
        "//form[@id='add_to_basket_form']//button[contains(@type,'submit')]").text
    assert language_actual_result == "Añadir al carrito"
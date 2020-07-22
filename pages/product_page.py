from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def product_can_be_added_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()
        self.should_be_item_is_added_basket_message()

    def should_be_login_or_register_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_PAGE_URL), "Login or register link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*ProductPageLocators.LOGIN_PAGE_URL)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "Add to basket button is not presented"

    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_item_is_added_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_PAGE_URL), \
            "Item is added to basket link is not presented"

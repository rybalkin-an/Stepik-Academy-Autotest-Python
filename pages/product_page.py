import allure
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators
from constants import PRODUCT_PAGE_URL

path = PRODUCT_PAGE_URL


class ProductPage(BasePage):
    @allure.step('Add product to basket')
    def product_can_be_added_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()
        self.should_be_item_is_added_basket_message()

    def should_be_login_or_register_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_PAGE_URL), "Login or register link is not presented"

    @allure.step('Go to login page')
    def go_to_login_page(self):
        link = self._browser.find_element(*ProductPageLocators.LOGIN_PAGE_URL)
        link.click()
        return LoginPage(self._browser, self._browser.current_url)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "Add to basket button is not presented"

    def click_add_to_basket_button(self):
        self.click(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def click_add_review_button(self):
        self.click(*ProductPageLocators.WRITE_A_REVIEW_BUTTON)

    def should_be_item_is_added_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE), \
            "Item is added to basket message is not presented"

    def item_is_added_basket_message_is_no_appears(self):
        assert self.is_not_element_present(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE), \
            "Item is added to basket message is not presented"

    def should_be_thanks_for_the_review(self):
        assert self.is_element_present(*ProductPageLocators.THX_FOR_REVIEW_MESSAGE), \
            "Thanks for review message is not presented"

    def should_be_write_a_review_button(self):
        assert self.is_element_present(*ProductPageLocators.WRITE_A_REVIEW_BUTTON),\
            "Write a review button is not presented"

    @allure.step('Verify the presence of a review form')
    def should_be_write_a_review_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_A_REVIEW_FORM),\
            "Add a review form is not presented"
        assert self.is_element_present(*ProductPageLocators.LEAVE_A_REVIEW_TITLE_FIELD),\
            "Title field is not presented"
        assert self.is_element_present(*ProductPageLocators.LEAVE_A_REVIEW_SCORE_FIELD),\
            "Score field is not presented"
        assert self.is_element_present(*ProductPageLocators.LEAVE_A_REVIEW_BODY_FIELD),\
            "Body field is not presented"
        assert self.is_element_present(*ProductPageLocators.LEAVE_A_REVIEW_EMAIL_FIELD),\
            "Email field is not presented"
        assert self.is_element_present(*ProductPageLocators.SAVE_REVIEW_BUTTON),\
            "Save review button is not presented"

    @allure.step('Write a review of a product')
    def fill_up_a_review_form(self):
        self.write_field(*ProductPageLocators.LEAVE_A_REVIEW_TITLE_FIELD, "REVIEW_TITLE_FIELD")
        self.click(*ProductPageLocators.LEAVE_A_REVIEW_SCORE_FIELD)
        self.write_field(*ProductPageLocators.LEAVE_A_REVIEW_BODY_FIELD, "REVIEW_BODY_FIELD")
        self.write_field(*ProductPageLocators.LEAVE_A_REVIEW_NAME_FIELD, "REVIEW_NAME_FIELD")
        self.write_field(*ProductPageLocators.LEAVE_A_REVIEW_EMAIL_FIELD, "EMAIL@GG.WP")
        self.click(*ProductPageLocators.SAVE_REVIEW_BUTTON)

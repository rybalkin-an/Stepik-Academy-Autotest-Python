import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    _base_path = None

    def go_to_login_page(self):
        self.click(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_language_selection_form(self):
        assert self.is_element_present(*MainPageLocators.LANGUAGE_SELECT_MENU), "Language select menu is not presented"
        assert self.is_element_present(*MainPageLocators.LANGUAGE_SELECT_SUBMIT_BUTTON), \
            "Language select submit is not presented"

    @allure.step('Guest select RU language')
    def guest_select_ru_language(self):
        self.click(*MainPageLocators.LANGUAGE_SELECT_MENU)
        self.click(*MainPageLocators.LANGUAGE_RU_SELECTION)
        self.click(*MainPageLocators.LANGUAGE_SELECT_SUBMIT_BUTTON)

    def should_be_menu_in_ru_language(self):
        assert self.is_element_present(*MainPageLocators.RU_CATALOG_MENU_ALL_ITEMS), \
            "All items in RU catalog menu is not presented"
        assert self.is_element_present(*MainPageLocators.RU_CATALOG_MENU_CLOTHING), \
            "Clothing in RU catalog menu is not presented"
        assert self.is_element_present(*MainPageLocators.RU_CATALOG_MENU_BOOKS), \
            "Books in RU catalog menu is not presented"
        assert self.is_element_present(*MainPageLocators.RU_CATALOG_MENU_OFFERS), \
            "Offers in RU catalog menu is not presented"

    @allure.step('Add item to basket from catalogue')
    def add_item_to_basket_from_catalogue(self):
        self.is_element_present(*MainPageLocators.BOOK_ITEM_IN_CATALOG)
        self.click(*MainPageLocators.BOOK_ITEM_IN_CATALOG_ADD_BASKET_BUTTON)

    def should_be_item_is_added_basket_message(self):
        assert self.is_element_present(*MainPageLocators.BUY_BOOK_ITEM_FROM_CATALOG_CONFIRM_MSG), \
            "Item has been added to basket message is not presented"

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from pages.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except ElementNotInteractableException:
            return False
        return True

    def write_field(self, how, what, keys):
        try:
            self.browser.find_element(how, what).send_keys(keys)
        except ElementNotInteractableException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

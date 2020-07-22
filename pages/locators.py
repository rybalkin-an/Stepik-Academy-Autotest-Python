from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_COMPLETE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")


class ProductPageLocators():
    LOGIN_PAGE_URL = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']//button[contains(@type,'submit')]")
    HAS_BEEN_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//div[contains(@class,'success')]")

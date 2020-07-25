from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LANGUAGE_SELECT_MENU = (By.XPATH, "//select[@name='language']")
    LANGUAGE_RU_SELECTION = (By.XPATH, "//option[contains(@value,'ru')]")
    LANGUAGE_SELECT_SUBMIT_BUTTON = (By.XPATH, "//form[@id='language_selector']//button[@type='submit']")
    CATALOG_MENU_ALL_ITEMS = (By.XPATH, "//ul[@id='browse']//a[@href='/ru/catalogue/']")
    CATALOG_MENU_CLOTHING = (By.XPATH, "//ul[@id='browse']//a[@href='/ru/catalogue/category/clothing_1/']")
    CATALOG_MENU_BOOKS = (By.XPATH, "//ul[@id='browse']//a[@href='/ru/catalogue/category/books_2/']")
    CATALOG_MENU_OFFERS = (By.XPATH, "//ul[@id='browse']//a[@href='/ru/offers/']")
    BOOK_ITEM_IN_CATALOG = (By.LINK_TEXT, "The shellcoder's handbook")
    BOOK_ITEM_IN_CATALOG_ADD_BASKET_BUTTON = (By.XPATH, "//form[contains(@action,'/ru/basket/add/209/')]//button[contains(@type,'submit')]")
    BUY_BOOK_ITEM_FROM_CATALOG_CONFIRM_MSG = (By.XPATH, "//div[contains(@class,'alertinner')]//strong[contains(text(),'The shellcoder')]")


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
    THX_FOR_REVIEW_MESSAGE = (By.XPATH, "//div[@id='messages']//div[contains(@class,'success')]")
    WRITE_A_REVIEW_BUTTON = (By.ID, "write_review")
    ADD_A_REVIEW_FORM = (By.ID, "add_review_form")
    LEAVE_A_REVIEW_TITLE_FIELD = (By.ID, "id_title")
    LEAVE_A_REVIEW_SCORE_FIELD = (By.XPATH, "//select[@id='id_score']//option[contains(@value,'1')]")
    LEAVE_A_REVIEW_BODY_FIELD = (By.ID, "id_body")
    LEAVE_A_REVIEW_NAME_FIELD = (By.ID, "id_name")
    LEAVE_A_REVIEW_EMAIL_FIELD = (By.ID, "id_email")
    SAVE_REVIEW_BUTTON = (By.XPATH, "//form[@id='add_review_form']//button[contains(@type,'submit')]")

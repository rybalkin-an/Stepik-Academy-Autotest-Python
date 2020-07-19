import random
from selenium.webdriver.common.by import By


BASE_URL = "http://selenium1py.pythonanywhere.com/"


def test_customer_should_see_enter_or_register_link(browser):
    browser.get(BASE_URL)
    login_link = browser.find_elements(By.ID, "login_link")
    browser.implicitly_wait(10)
    assert len(login_link) > 0, "Login link is not rendered"


def test_register_page_form(browser):
    browser.get(BASE_URL + "/accounts/login/")
    browser.find_element(By.ID, "id_registration-email").send_keys(str(random.getrandbits(25)) + "@fakemail.org")
    browser.find_element(By.ID, "id_registration-password1").send_keys('Testpass1123')
    browser.find_element(By.ID, "id_registration-password2").send_keys('Testpass1123')
    browser.find_element(By.NAME, "registration_submit").click()
    browser.implicitly_wait(10)
    thanks_for_registration_message = browser.find_elements(By.CSS_SELECTOR, "#messages .alert")
    assert len(thanks_for_registration_message) > 0, "registration message is not rendered"







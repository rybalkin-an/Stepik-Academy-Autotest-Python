from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/"

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)
current_url = browser.current_url
print('current url:', current_url, type(current_url))
browser.close()


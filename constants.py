from os import getenv

BASE_URL = getenv('BASE_URL', 'http://selenium1py.pythonanywhere.com/')
LOGIN_PAGE_URL = '/accounts/login/'
PRODUCT_PAGE_URL = 'catalogue/coders-at-work_207/'

IMPLICIT_WAIT = 2
EXPLICIT_WAIT = 4
WINDOW_SIZE = ('1280', '1024')
PASSWORD = 'Testpass1123'

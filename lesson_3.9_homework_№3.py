from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/ru/"

def check_basket_2():
    """
    II. При добавлении товара с типом Книга в корзину из каталога, под заголовком
    “Все товары” появляется сообщение %itemname% был добавлен в вашу корзину

    Шаги:
    1. Кликаем  “Просмотр магазина” в главном меню
    2. Находим в каталоге товар книгу
    3. Добавляем в корзину, кликая кнопку “Добавить в корзину”
    ОР:
    Под заголовком “Все товары” появляется сообщение: “%itemname% был добавлен в вашу корзину”
    """
    browser = None
    try:
        browser = webdriver.Chrome()
        browser.set_window_size(width=1366, height=768)
        browser.get(link)

        browser.find_element_by_xpath("//ul[@id='browse']//a[contains(text(),'Все товары')]").click()
        #1. Кликаем  “Просмотр магазина” в главном меню

        browser.find_element_by_link_text("The shellcoder's handbook")
        #2. Находим в каталоге товар книгу

        browser.find_element_by_xpath("//form[contains(@action,'/ru/basket/add/209/')]//button[contains(@class,'btn btn-primary btn-block')]").click()
        #3. Находим в каталоге товар книгу

        confirmation_text = browser.find_element_by_xpath("//div[contains(@class,'alertinner')]//strong[contains(text(),'The shellcoder')]")
        confirmation_text = confirmation_text.text
        #4 проверяем, что под заголовком “Все товары” появляется сообщение: “%itemname% был добавлен в вашу корзину”
        assert "The shellcoder's handbook" == confirmation_text

    finally:
        time.sleep(1)
        browser.close()

def check_basket_1():
    """
    I. Элементы главного меню должны отображаться на языке, выбранном в меню выбора языка

    Steps
    1. Выбираем русский язык в меню выбора языка
    2. Кликаем выполнить
    3. Кликаем в главном меню “Просмотр магазина”

    ОР:
    Появляется выпадающий список на русском языке:
    Все товары
    Одежда
    Книги
    Предложения
    """
    browser = None
    try:
        browser = webdriver.Chrome()
        browser.set_window_size(width=1366, height=768)
        browser.get(link)

        browser.find_element_by_xpath("//select[contains(@name,'language')]").click()
        browser.find_element_by_xpath("//option[contains(@value,'ru')]").click()
        #1. Выбираем русский язык в меню выбора языка

        browser.find_element_by_xpath("//button[contains(@type,'submit')]").click()
        #2. Кликаем выполнить

        browser.find_element_by_xpath("//a[contains(@class,'dropdown-toggle')]").click()
        #3. Кликаем в главном меню “Просмотр магазина”

        catalog_all_items = browser.find_element_by_xpath("//ul[@id='browse']//a[@href='/ru/catalogue/']")
        catalog_all_items = catalog_all_items.text
        assert catalog_all_items == "Все товары", \
            f"Wrong language, got {catalog_all_items} instead of 'Все товары'"
        #Проверка "Все товары" в списке меню на русском языке

        catalog_clothing = browser.find_element_by_xpath("//ul[@id='browse']//a[@href='/ru/catalogue/category/clothing_1/']")
        catalog_clothing = catalog_clothing.text
        assert catalog_clothing == "Одежда", \
            f"Wrong language, got {catalog_clothing} instead of 'Одежда'"
        #Проверка "Одежда" в списке меню на русском языке

        catalog_books = browser.find_element_by_xpath("//ul[@id='browse']//a[@href='/ru/catalogue/category/books_2/']")
        catalog_books = catalog_books.text
        assert catalog_books == "Книги", \
            f"Wrong language, got {catalog_books} instead of 'Книги'"
        #Проверка "Книги" в списке меню на русском языке

        catalog_offers = browser.find_element_by_xpath("//ul[@id='browse']//a[@href='/ru/offers/']")
        catalog_offers = catalog_offers.text
        assert catalog_offers == "Предложения", \
            f"Wrong language, got {catalog_offers} instead of 'Предложения'"
        # Проверка "Предложения" в списке меню на русском языке

    finally:
        # успеваем скопировать код за 10 секунд
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.close()

def check_basket_5():
    """
    V. Регистрация нового пользователя с некорректным форматом почтового ящика, с адресом не содержащим @
    1. Кликаем по ссылке “Войти или зарегистрироваться”
    2. Находим форму “Зарегистрироваться”
    3. Заполняем поле “Адрес электронной почты” некорректным форматом почтового ящика, не содержащий @
    4. Заполняем поле “Пароль” Testpass123
    5. Заполняем поле “Повторите пароль” Testpass123
    6. Кликаем кнопку “Зарегистрироваться”
    OP
    Появление всплывающего сообщения в поле “Адрес электронной почты” с текстом: “Некорректный электронный адрес. Отсутствует @”
    """

    browser = None
    try:

        browser = webdriver.Chrome()
        browser.set_window_size(width=1366, height=768)
        browser.get(link)
        browser.find_element_by_id("login_link").click()

        browser.find_element_by_xpath("//form[@id='register_form']//h2[contains(text(),'Зарегистрироваться')]")
        # 1. Кликаем по ссылке “Войти или зарегистрироваться”

        confirmation_registration_text = browser.find_element_by_xpath("//form[@id='register_form']//h2[contains(text(),'Зарегистрироваться')]")
        confirmation_registration_text = confirmation_registration_text.text
        assert "Зарегистрироваться" == confirmation_registration_text
        # 2. Находим форму “Зарегистрироваться”
        # проверяем, что ожидаемый текст совпадает

        input_email = browser.find_element_by_id('id_registration-email')
        input_email.send_keys("testemail.ru")
        # 3. Заполняем поле “Адрес электронной почты” некорректным форматом почтового ящика, не содержащий @

        input_email = browser.find_element_by_id('id_registration-password1')
        input_email.send_keys("Testpass123")
        # 4. Заполняем поле “Пароль” Testpass123

        input_email = browser.find_element_by_id('id_registration-password2')
        input_email.send_keys("Testpass123")
        # 5. Заполняем поле “Повторите пароль” Testpass123

        browser.find_element_by_xpath("//button[contains(@name,'registration_submit')]").click()
        # 6. Кликаем кнопку “Зарегистрироваться”
        # не получается нагуглить, как проводить валидацию тултипов =/

    finally:
        time.sleep(3)
        browser.close()

def check_basket_4():
    """
    IV. Написание отзыва в карточке товара
    1. Кликаем “Просмотр магазина” в главном меню
    2. Находим в каталоге любой товар
    3. Открываем карточку товара переходя по ссылке с названием товара или изображением товара
    4. Кликаем кнопку “Написать отзыв”
    5. Заполняем поля формы с заголовком “Оставить отзыв о товаре”
    “Заголовок”, “Сообщение”, “Название”, “Адрес электронной почты”
    Выставляем оценку в поле “Оценка”, кликнув на иконку звезды от 1 до 5
    Кликаем на кнопку “Сохранить отзыв”
    ОР:
    Появление сообщения: “Спасибо за Ваш отзыв!” над формой с заголовком “Оставить отзыв о товаре”
    Написанный отзыв отобразиться в поле ниже заголовка “Отзывы Клиентов”

    Появление всплывающего сообщения в поле “Адрес электронной почты” с текстом: “Некорректный электронный адрес. Отсутствует @”
    """
    browser = None
    try:
        browser = webdriver.Chrome()
        browser.set_window_size(width=1366, height=768)
        browser.get(link)
        browser.find_element_by_xpath("//a[contains(@class,'dropdown-toggle')]").click()
        #1. Кликаем в главном меню “Просмотр магазина”

        browser.find_element_by_xpath("//ul[@id='browse']//a[contains(text(),'Все товары')]").click()
        #2. Кликаем в главном меню “Все товары”

        browser.find_element_by_link_text("The shellcoder's handbook").click()
        #3. Находим в каталоге товар книгу и открываем карточку товара переходя по ссылке с названием товара

        browser.find_element_by_id("write_review").click()
        #4. Кликаем кнопку “Написать отзыв”

        browser.implicitly_wait(2)
        input_title = browser.find_element_by_id("id_title")
        input_title.send_keys("Лучший товар")
        #Заполняем поле "Заголовок"

        #browser.find_element_by_xpath("//select[contains(@id='id_score')]//*[7]").click()
        #Кликаем на оценку(Тест падает, нет элемента)

        input_body = browser.find_element_by_id("id_name")
        input_body.send_keys("Хвалебный отзыв")
        # Заполняем поле "Сообщение"

        input_name = browser.find_element_by_id("id_body")
        input_name.send_keys("Супер книга")
        # Заполняем поле "Название"

        input_email = browser.find_element_by_id("id_email")
        input_email.send_keys("testemail@mail.ru")
        # Заполняем поле "Aдрес электронной почты"

        browser.find_element_by_xpath("//button[contains(text(),'Сохранить отзыв')]").click()
        # Кликаем кнопку "Сохранить отзыв"

    finally:
        time.sleep(1)
        browser.close()

def check_basket_3():
    """
    III. При добавлении товара с типом Книга в корзину из карточки товара, под навигационной цепочкой
    появляется сообщение %itemname% был добавлен в вашу корзину

    Шаги:
    1.Кликаем “Просмотр магазина” в главном меню
    2.Находим в каталоге товар книгу
    3.Открываем карточку товара переходя по ссылке с названием товара или изображением товара
    4.Добавляем в корзину, кликая кнопку “Добавить в корзину”
    ОР:
    Под заголовком “Все товары” появляется сообщение: %itemname% был добавлен в вашу корзину
    """
    browser = None
    try:
        browser = webdriver.Chrome()
        browser.set_window_size(width=1366, height=768)
        browser.get(link)
        browser.find_element_by_xpath("//a[contains(@class,'dropdown-toggle')]").click()
        #1. Кликаем в главном меню “Просмотр магазина”

        browser.find_element_by_xpath("//ul[@id='browse']//a[contains(text(),'Все товары')]").click()
        #2. Кликаем в главном меню “Все товары”

        browser.find_element_by_link_text("The shellcoder's handbook").click()
        #3. Находим в каталоге товар книгу и открываем карточку товара переходя по ссылке с названием товара

        browser.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-primary btn-add-to-basket')]").click()
        confirmation_text = browser.find_element_by_xpath("//div[contains(@class,'alertinner')]//strong[contains(text(),'The shellcoder')]")
        confirmation_text = confirmation_text.text
        assert "The shellcoder's handbook" == confirmation_text
        #проверяем, что ожидаемый текст совпадает с текстом на странице сайта

    finally:
        time.sleep(1)
        browser.close()

if __name__ == "__main__":
    check_basket_2()
    check_basket_3()
    check_basket_4()
    check_basket_5()
    check_basket_1()
    browser.quit()
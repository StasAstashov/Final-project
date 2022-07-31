from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
#     login_page = LoginPage(browser,url=browser.current_url) 
#     login_page.should_be_login_page

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()    

# def test_find_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
#     page1 = LoginPage(browser,link)  # инициализируем класс логин
#     page1.should_be_login_form()     # выполняем метод поиска формы логина
    
# def test_find_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
#     page1 = LoginPage(browser,link)  # инициализируем класс логин
#     page1.should_be_register_form()     # выполняем метод поиска формы регистрации

# def test_correct_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
#     page1 = LoginPage(browser,link)  # инициализируем класс логин
#     page1.should_be_login_url()     # выполняем метод проверки страницы   

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_basket()
    page1 = BasketPage(browser,link)
    page1.item_basket_check()
    page1.spisok_basket_check()
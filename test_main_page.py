from pages.main_page import MainPage
from pages.login_page import LoginPage

#def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу 

#def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
   # page = MainPage(browser, link)
    #page.open()
    #page.should_be_login_link()    

def test_find_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
    page1 = LoginPage(browser,link)  # инициализируем класс логин
    page1.should_be_login_form()     # выполняем метод поиска формы логина
    
def test_find_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
    page1 = LoginPage(browser,link)  # инициализируем класс логин
    page1.should_be_register_form()     # выполняем метод поиска формы регистрации

def test_correct_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу
    page1 = LoginPage(browser,link)  # инициализируем класс логин
    page1.should_be_login_url()     # выполняем метод проверки страницы    
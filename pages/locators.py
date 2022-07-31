from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    Login_Form = (By.ID, "login_form")
    Register_Form = (By.ID, "register_form")

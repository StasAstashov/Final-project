from os import link
from .base_page import BasePage
from .locators  import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Login_Form), "Login form is not presented"
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Register_Form), "Register form is not presented"

    def register_new_user(self,email,password):
        self.browser.find_element(*LoginPageLocators.Register_Line).send_keys(email)
        self.browser.find_element(*LoginPageLocators.Register_Password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.Register_Password_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.Button_Register).click()
        
from sre_constants import SUCCESS
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    Login_Form = (By.ID, "login_form")
    Register_Form = (By.ID, "register_form")
    Register_Line = (By.ID, "id_registration-email")
    Register_Password = (By.ID, "id_registration-password1")
    Register_Password_2 = (By.ID, "id_registration-password2")
    Button_Register = (By.CSS_SELECTOR, "#register_form > button")
class ProductPageLocators():
    Cart_Button = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    Product_Name = (By.CSS_SELECTOR, "div.product_main h1")
    Product_Name_Cart = (By.CSS_SELECTOR, "div.alertinner strong")
    Product_Price = (By.CSS_SELECTOR, ".product_main .price_color")
    Product_Price_Cart = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") 
    Busket_Button = (By.CSS_SELECTOR, " div.basket-mini.pull-right.hidden-xs  span  a")  
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():

 Busket_Item = (By.CSS_SELECTOR, "#content_inner p a")
 Busket_Item1 = (By.CSS_SELECTOR,"div.sub-header h2" )

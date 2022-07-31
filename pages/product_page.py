
from .base_page import BasePage
from .locators  import ProductPageLocators
import time

class ProductPage (BasePage):
    
    def check_names(self):  
        Prod_Name = self.browser.find_element(*ProductPageLocators.Product_Name)
        PN = Prod_Name.text
        Prod_Name_Cart = self.browser.find_element(*ProductPageLocators.Product_Name_Cart)
        PNC = Prod_Name_Cart.text
        assert PN == PNC, "Имена совпадают" 

    def go_to_cart(self):    
        cart_button = self.browser.find_element(*ProductPageLocators.Cart_Button)
        cart_button.click()
        
    def math_checking(self):    
        self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
         assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"    
    
    def message_is_disappearing(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared after adding product to basket"
    
    def price_chechking(self):    
        Prod_Price = self.browser.find_element(*ProductPageLocators.Product_Price)
        PP = Prod_Price.text
        Prod_Price_Cart = self.browser.find_element(*ProductPageLocators.Product_Price_Cart)
        PPC = Prod_Price_Cart.text
        assert PP == PPC, "Цена совпадает"
   
        
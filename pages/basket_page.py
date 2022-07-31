from .base_page import BasePage
from .locators import BasketLocators
class BasketPage (BasePage):
    def item_basket_check(self):
        assert self.is_not_element_present(*BasketLocators.Busket_Item1), "Your basket is not empty."
    def spisok_basket_check(self):
        assert self.is_element_present(*BasketLocators.Busket_Item), "Your basket is empty."

        
            
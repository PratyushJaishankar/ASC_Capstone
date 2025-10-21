from idlelib import query

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class SearchPage(BasePage):
    SEARCH_BUTTON =(By.XPATH, "//*[@id='NavStandard']/div[5]/search-popdown/details/summary")
    SEARCH_BOX=(By.ID,"searchInput-desktop")
    PRODUCT_LOCATOR = (By.CSS_SELECTOR, "div.product-title")
    COUPON = (By.ID, "cpnCode")
    COUPON_COPY_BUTTON = (By.ID, "cpnBtn")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "button[class='select-popout__toggle']")

    RESULT_EMAIL = (By.XPATH, "//div[contains(@class, 'customer-email')]")
    RESULT_NAME = (By.XPATH, "//div[contains(@class, 'customer-name')]")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[name='add']")
    VERIFY_CART_QUANTITY=(By.XPATH,"//*[@id='cart-drawer']/div[2]/h3/span")
    def open_search(self):
        self.click(self.SEARCH_BUTTON)

    # Renamed from `search_product` to `search_customer` to match tests
    def search_product(self, query):
        self.enter_text(self.SEARCH_BOX, query)
        # send RETURN to the specific search input element
        self.send_keys(Keys.RETURN, by_locator=self.SEARCH_BOX)

    def get_result(self, query):
        for element in self.find_elements(self.PRODUCT_LOCATOR):
            if query in element.text.lower():
                element.click()
                break

    def add_product_to_cart(self,quantity):
        quantity_locator = (By.XPATH, f"//a[@data-value='{quantity}']")
        self.cart_dropdown(self.QUANTITY_INPUT, quantity_locator)
        self.click(self.ADD_TO_CART_BUTTON)


    def copy_code(self):
        self.double_click(self.COUPON)
        time.sleep(2)
        self.click(self.COUPON_COPY_BUTTON)

    def paste_code(self):
        self.click(self.SEARCH_BUTTON)
        time.sleep(2)
        self.paste_text(self.SEARCH_BOX)

    def verify_cart(self):
        quantity = self.get_text(self.VERIFY_CART_QUANTITY)
        return quantity




#     def get_result_name(self):
#         return self.get_text(self.RESULT_NAME)
# import csv
#
# def get_search_data(csv_path):
#     with open(csv_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         return [row for row in reader]

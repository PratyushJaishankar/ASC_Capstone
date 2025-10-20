from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, "summary.search-popdown__toggle[data-popdown-toggle]")
    SEARCH_INPUT = (By.ID, "searchInput-desktop")
    RESULT_EMAIL = (By.XPATH, "//div[contains(@class, 'customer-email')]")
    RESULT_NAME = (By.XPATH, "//div[contains(@class, 'customer-name')]")

    def open_search(self):
        self.click(self.SEARCH_ICON)

    # Renamed from `search_product` to `search_customer` to match tests
    def search_customer(self, query):
        self.enter_text(self.SEARCH_INPUT, query)
        # send RETURN to the specific search input element
        self.send_keys(Keys.RETURN, by_locator=self.SEARCH_INPUT)

    def get_result_email(self):
        return self.get_text(self.RESULT_EMAIL)

    def get_result_name(self):
        return self.get_text(self.RESULT_NAME)
import csv

def get_search_data(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

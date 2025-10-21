import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class AddressPage(BasePage):
    MY_ACCOUNT_ICON = (By.XPATH, "//*[@id='NavStandard']/div[5]/div[1]/a")
    VIEW_ADDRESS = (By.CSS_SELECTOR, 'a[href="/account/addresses"]')
    ADD_ADDRESS = (By.CSS_SELECTOR, "a.btn.btn--primary.btn--solid[data-button-new]")
    FIRST_NAME_INPUT = (By.ID, "AddressFirstNameNew")
    LAST_NAME_INPUT = (By.ID, "AddressLastNameNew")
    COMPANY_FIELD = (By.ID, "AddressCompanyNew")
    ADDRESS_LINE_1 = (By.ID, "AddressAddress1New")
    ADDRESS_LINE_2 = (By.ID, "AddressAddress2New")
    CITY = (By.ID, "AddressCityNew")
    PROVINCE = (By.NAME, "address[province]")
    POSTAL_CODE = (By.ID, "AddressZipNew")
    PHONE_NUMBER = (By.ID, "AddressPhoneNew")
    DEFAULT_ADDRESS_CHECKBOX = (By.NAME, "address[default]")
    ADD_ADDRESS_CONFIRM = (By.XPATH, "//*[@id='address_form_new']/p[2]/button")
    RESULT_ADDRESS = (By.CSS_SELECTOR, "div.address p")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def new_address(self, first_name, last_name, company_field, province,address_line_1, address_line_2, city, postal_code, phone_number):

        self.click(self.MY_ACCOUNT_ICON)
        self.click(self.VIEW_ADDRESS)
        self.click(self.ADD_ADDRESS)
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.COMPANY_FIELD, company_field)
        self.enter_text(self.ADDRESS_LINE_1, address_line_1)
        self.enter_text(self.ADDRESS_LINE_2, address_line_2)
        self.enter_text(self.CITY, city)
        self.enter_text(self.POSTAL_CODE, postal_code)
        self.enter_text(self.PHONE_NUMBER, phone_number)
        self.select_from_dropdown(self.PROVINCE, province)
        self.click(self.DEFAULT_ADDRESS_CHECKBOX)
        time.sleep(2)
        self.click(self.DEFAULT_ADDRESS_CHECKBOX)
        self.click(self.ADD_ADDRESS_CONFIRM)

    def isSuccessfullyAdded(self, first_name):
        try:
            # Collect all <p> inside address divs
            address_blocks = self.driver.find_elements(By.CSS_SELECTOR, "div.address p")
            print(f"DEBUG: Found {len(address_blocks)} address blocks")

            for block in address_blocks:
                text = block.text.strip()
                print("DEBUG BLOCK TEXT:\n", text)
                if first_name.lower() in text.lower():
                    print(f"Found matching address for '{first_name}'")
                    return True

            print(f"No address block contains '{first_name}'")
            return False

        except Exception as e:
            print("DEBUG ERROR:", e)
            return False

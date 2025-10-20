import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_ICON = (By.CSS_SELECTOR, "a[href='/account']")
    EMAIL_INPUT = (By.ID, "CustomerEmail")
    PASSWORD_INPUT = (By.ID, "CustomerPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space(text())='Sign In']")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def open_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_ICON)).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "loginWithEmailButton"))).click()

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='NavStandard']/div[5]/div[1]/a"))).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK  )).click()



def get_login_data(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

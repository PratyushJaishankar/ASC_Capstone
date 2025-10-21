import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def cart_dropdown(self, by_locator, option_locator):
        dropdown_toggle = self.wait.until(EC.element_to_be_clickable(by_locator))
        dropdown_toggle.click()
        # 2️⃣ Select the quantity '6'
        option = self.wait.until(EC.element_to_be_clickable(option_locator))
        option.click()

    def paste_text(self, by_locator):
        elem = self.wait.until(EC.visibility_of_element_located(by_locator))
        elem.clear()
        elem.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        elem.send_keys(Keys.ESCAPE)
        time.sleep(2)

    def double_click(self, by_locator):
        elem = self.wait.until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.double_click(elem).perform()

    def get_color(self, by_locator, css_property):
        elem = self.wait.until(EC.visibility_of_element_located(by_locator))
        return elem.value_of_css_property(css_property)

    def mouse_hover(self, by_locator):
        elem = self.wait.until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(by_locator))
        elem.clear()
        elem.send_keys(text)

    def find_elements(self, by_locator):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))


    def select_from_dropdown(self, by_locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(by_locator))
        select = Select(elem)
        select.select_by_visible_text(text)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    # Added helper to execute JavaScript on the page
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    # Added helper to send keys to the active element or to a specific locator
    def send_keys(self, keys, by_locator=None):
        if by_locator:
            elem = self.wait.until(EC.visibility_of_element_located(by_locator))
            elem.send_keys(keys)
        else:
            # send to the currently focused element
            self.driver.switch_to.active_element.send_keys(keys)

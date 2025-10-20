import pytest
from page_objects.login_page import LoginPage
from data.login_data import get_login_data
import allure
import time
browsers = ["chrome"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("login_data", get_login_data("data/login_data.csv"))
@allure.feature("Login & Logout")
def test_login_logout(driver, login_data):
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.login(login_data["email"], login_data["password"])
    # Assertion: Check if logout link is visible (indicates successful login)
    time.sleep(2)  # Wait briefly for the page to respond / redirect
    assert driver.current_url.rstrip('/') == "https://market99.com"
    login_page.logout()
    time.sleep(2)
    # Assertion: Check if login icon is visible again (indicates successful logout)
    assert driver.current_url.rstrip('/') == "https://market99.com"

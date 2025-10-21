import pytest
from page_objects.login_page import LoginPage
from data.Complete_Test_Data.login_data import get_login_data
import allure
import time
browsers = ["chrome"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("login_data", get_login_data("data/Complete_Test_Data/login_data.csv"))
@allure.feature("Login & Logout")
def test_login_logout(driver, login_data):
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    mouse_hover_result = login_page.mouse_hover_perform()
    assert mouse_hover_result == True
    login_page.login(login_data["email"], login_data["password"])
    # Wait briefly for the page to respond / redirect
    time.sleep(2)

    # New behavior: CSV may include a 'result' column with 'success' or 'failed'
    result = (login_data.get("result") or "success").strip().lower()
    if result == "success":
        # Positive test: expect to be logged in
        assert login_page.is_logged_in(), f"Expected login to succeed for {login_data}, but logout link not found (url={driver.current_url})"
        # Perform logout and verify logged-out state
        login_page.logout()
        time.sleep(2)
    else:
        # Negative test: expect login to fail (login form still present and not logged in)
        assert not login_page.is_logged_in(), f"Expected login to fail for {login_data}, but user appears logged in (url={driver.current_url})"
        assert login_page.is_login_page_loaded(), f"Expected login page/form to remain after failed login for {login_data}"

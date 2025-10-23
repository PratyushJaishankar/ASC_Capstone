import pytest
from page_objects.login_page import LoginPage
from data.Complete_Test_Data.data_loader import get_data
import time

browsers = ["chrome", "edge"]

# Load test data once at module level
positive_login_data = get_data("data/Complete_Test_Data/login_data.csv")
negative_login_data = get_data("data/Failed_Test_Data/negative_login_data.csv")


@pytest.mark.feature("Login & Logout")
@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("login_data", positive_login_data)
def test_login_logout(driver, login_data):
    """Positive login tests - each CSV row is a separate test"""
    print(f"Starting positive login test for: {login_data.get('email', 'unknown')}")
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    mouse_hover_result = login_page.mouse_hover_perform()
    assert mouse_hover_result == True

    print(f"Attempting login for: {login_data.get('email', 'unknown')}")
    login_page.login(login_data["email"], login_data["password"])
    time.sleep(2)
    assert login_page.is_logged_in(), f"Expected login to succeed for {login_data}, but logout link not found (url={driver.current_url})"
    print("Login successful, proceeding to logout")
    login_page.logout()
    time.sleep(2)
    print(f"Completed positive login/logout test for: {login_data.get('email', 'unknown')}")


@pytest.mark.feature("Login & Logout")
@pytest.mark.negativecases
@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("login_data", negative_login_data)
def test_login_logout_negative(driver, login_data):
    """Negative login tests - each CSV row is a separate test"""
    print(f"Starting negative login test for: {login_data.get('email', 'unknown')}")
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    mouse_hover_result = login_page.mouse_hover_perform()
    assert mouse_hover_result == True

    print(f"Attempting negative login for: {login_data.get('email', 'unknown')}")
    login_page.login(login_data["email"], login_data["password"])
    time.sleep(2)
    assert not login_page.is_logged_in(), f"Expected login to fail for {login_data}, but user appears logged in (url={driver.current_url})"
    assert login_page.is_login_page_loaded(), f"Expected login page/form to remain after failed login for {login_data}"
    print(f"Completed negative login test for: {login_data.get('email', 'unknown')}")

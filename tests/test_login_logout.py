import pytest
from page_objects.login_page import LoginPage
from data.Complete_Test_Data.data_loader import get_data
import allure
import time

browsers = ["chrome"]

@pytest.mark.feature("Login & Logout")
@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_login_logout(driver):
    """Positive login tests using positive_login_data.csv"""
    # Simple log for humans: indicate which test started
    print("Starting positive login/logout tests")
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    mouse_hover_result = login_page.mouse_hover_perform()
    assert mouse_hover_result == True

    # Load positive test data
    positive_data = get_data("data/Complete_Test_Data/positive_login_data.csv")
    # iterate rows and validate login then logout
    for login_data in positive_data:
        print(f"Attempting login for: {login_data.get('email', 'unknown')}")
        login_page.login(login_data["email"], login_data["password"])
        time.sleep(2)
        assert login_page.is_logged_in(), f"Expected login to succeed for {login_data}, but logout link not found (url={driver.current_url})"
        print("Login successful, proceeding to logout")
        login_page.logout()
        time.sleep(2)
    print("Completed positive login/logout tests")


@pytest.mark.feature("Login & Logout")
@pytest.mark.negativecases
@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_login_logout_negative(driver):
    """Negative login tests using negative_login_data.csv"""
    # Brief run-time log for clarity
    print("Starting negative login/logout tests")
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    mouse_hover_result = login_page.mouse_hover_perform()
    assert mouse_hover_result == True

    # Load negative test data
    negative_data = get_data("data/Failed_Test_Data/negative_login_data.csv")
    # try invalid credentials and assert failure
    for login_data in negative_data:
        print(f"Attempting negative login for: {login_data.get('email', 'unknown')}")
        login_page.login(login_data["email"], login_data["password"])
        time.sleep(2)
        assert not login_page.is_logged_in(), f"Expected login to fail for {login_data}, but user appears logged in (url={driver.current_url})"
        assert login_page.is_login_page_loaded(), f"Expected login page/form to remain after failed login for {login_data}"
    print("Completed negative login/logout tests")

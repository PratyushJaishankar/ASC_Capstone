import pytest
from page_objects.delete_address import AddressPage
from page_objects.login_page import LoginPage
from data.Complete_Test_Data.data_loader import get_data
import allure
import time

browsers = ["chrome", "edge"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("address_data", get_data("data/Complete_Test_Data/delete_address.csv"))
@pytest.mark.parametrize("login_data", get_data("data/Complete_Test_Data/login_data.csv"))
@allure.feature("Delete Address")
def test_delete_address(driver, address_data, login_data):
    print(f"\nStarting test with login: {login_data['email']}")
    print(f"Address data: {address_data}")
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.login(login_data["email"], login_data["password"])
    print("Login submitted.")
    assert "Market99" in driver.title, f"Unexpected page title after login: {driver.title}"
    address_page = AddressPage(driver)

    address_page.delete_address_by_name(address_data["first_name"], address_data["last_name"])
    time.sleep(3)
    deleted = address_page.is_address_deleted(address_data["first_name"], address_data["last_name"])
    assert deleted, f"Address for {address_data['first_name']} {address_data['last_name']} was not deleted!"
    print("Test completed successfully.")

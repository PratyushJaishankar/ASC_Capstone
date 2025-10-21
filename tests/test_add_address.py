import pytest
from page_objects.add_address import AddressPage
from page_objects.login_page import LoginPage
from data.Complete_Test_Data.add_address import get_address
from data.Complete_Test_Data.login_data import get_login_data
import allure
import time

browsers = ["chrome"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("address_data", get_address("data/Complete_Test_Data/add_address.csv"))
@pytest.mark.parametrize("login_data", get_login_data("data/Complete_Test_Data/login_data.csv"))
@allure.feature("Add Address")
def test_add_customer(driver, address_data, login_data):
    driver.get("https://market99.com/")
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.login(login_data["email"], login_data["password"])
    add_address_page = AddressPage(driver)
    add_address_page.new_address(
        address_data["first_name"],
        address_data["last_name"],
        address_data["company_field"],
        address_data["province"],
        address_data["address_line_1"],
        address_data["address_line_2"],
        address_data["city"],
        address_data["postal_code"],
        address_data["phone_number"]
    )
    # Wait briefly for the page to respond / redirect
    time.sleep(5)

    assert add_address_page.isSuccessfullyAdded(address_data["first_name"]) is True
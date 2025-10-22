import pytest
from page_objects.Signup import AddCustomerPage
from data.Complete_Test_Data.data_loader import get_data
import allure
import time

browsers = ["chrome", "edge"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("customer_data", get_data("data/Complete_Test_Data/add_customer_data.csv"))
@allure.feature("Add Customer")
def test_add_customer(driver, customer_data):
    driver.get("https://market99.com/")
    add_customer_page = AddCustomerPage(driver)
    add_customer_page.open_registration()
    add_customer_page.add_customer(
        customer_data["first_name"],
        customer_data["last_name"],
        customer_data["email"],
        customer_data["password"]
    )
    # Wait briefly for the page to respond / redirect
    time.sleep(2)

    # New behavior: CSV has a 'result' column with values 'success' or 'failed'.
    result = (customer_data.get("result") or "success").strip().lower()
    if result == "success":
        # Positive test: expect redirect to homepage (registration successful)
        assert add_customer_page.is_registration_successful(), \
            f"Expected registration to succeed for {customer_data}, but current_url={driver.current_url}"
    else:
        # Negative test: expect registration to fail (form still present or not redirected)
        assert add_customer_page.is_registration_page_loaded() or driver.current_url.strip("/") != "https://market99.com", \
            f"Expected registration to fail for {customer_data}, but it appears to have succeeded (url={driver.current_url})"

from itertools import product

import pytest
from page_objects.search_page import SearchPage
import allure
from data.Complete_Test_Data.data_loader import get_data
browsers = ["chrome"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("search_data", get_data("data/Complete_Test_Data/search_data.csv"))
@allure.feature("Search Page")
def test_search_customer(driver):
    driver.get("https://market99.com/")
    search_page = SearchPage(driver)
    # Search by email
    search_page.open_search()
    search_query="bottle"
    search_page.search_product(search_query)
    current_url = driver.current_url
    assert "search" in current_url, f"'search' not found in URL after searching: {current_url}"
    assert "bottle" in current_url, f"'bottle' not found in URL after searching: {current_url}"
    search_page.get_result(search_query)
    current_url = driver.current_url
    assert "products" in current_url, f"'search' not found in URL after opening result: {current_url}"
    assert "bottle" in current_url, f"'bottle' not found in URL after opening result: {current_url}"
    search_page.copy_code()
    search_page.paste_code()
    quantity_query=6
    search_page.add_product_to_cart(str(quantity_query))
    cart_quantity=search_page.verify_cart()
    assert str(quantity_query) in cart_quantity


    # assert search_data["email"] in search_page.get_result_email()
    # # Search by first name
    # search_page.search_customer(search_data["first_name"])
    # assert search_data["first_name"] in search_page.get_result_name()
    # # Search by last name
    # search_page.search_customer(search_data["last_name"])
    # assert search_data["last_name"] in search_page.get_result_name()

import pytest
from page_objects.search_page import SearchPage
from data.data_loader import get_data as get_search_data
import allure

browsers = ["chrome", "firefox", "edge"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("search_data", get_search_data("data/search_data.csv"))
@allure.feature("Search Customer")
def test_search_customer(driver, search_data):
    driver.get("https://market99.com/")
    search_page = SearchPage(driver)
    search_page.open_search()
    # Search by email
    search_page.search_customer(search_data["email"])
    assert search_data["email"] in search_page.get_result_email()
    # Search by first name
    search_page.search_customer(search_data["first_name"])
    assert search_data["first_name"] in search_page.get_result_name()
    # Search by last name
    search_page.search_customer(search_data["last_name"])
    assert search_data["last_name"] in search_page.get_result_name()

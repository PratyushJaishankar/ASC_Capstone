import pytest
from page_objects.search_page import SearchPage
import allure
from data.Complete_Test_Data.data_loader import get_data

browsers = ["chrome"]

@pytest.mark.parametrize("driver", browsers, indirect=True)
@pytest.mark.parametrize("search_data", get_data("data/Complete_Test_Data/search_data.xlsx"))
@allure.feature("Search Page")
def test_search_customer(driver, search_data):
    driver.get("https://market99.com/")
    search_page = SearchPage(driver)

    product_name = search_data["product"]

    search_page.open_search()
    search_page.search_product(product_name)

    current_url = driver.current_url
    assert "search" in current_url, f"'search' not found in URL: {current_url}"
    assert product_name in current_url, f"'{product_name}' not found in URL: {current_url}"

    search_page.get_result(product_name)

    current_url = driver.current_url
    assert "products" in current_url, f"'products' not found in URL: {current_url}"
    assert product_name in current_url, f"'{product_name}' not found in URL: {current_url}"

    search_page.copy_code()
    search_page.paste_code()

    quantity_query = 6
    search_page.add_product_to_cart(str(quantity_query))
    cart_quantity = search_page.verify_cart()
    assert str(quantity_query) in cart_quantity

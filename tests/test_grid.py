import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from page_objects.home_page import HomePage

# Configure your Selenium Grid URL here
GRID_URL = "http://localhost:4444"  # Replace with your Grid URL

browsers = [ "chrome","edge","firefox"]


@pytest.fixture
def driver(request):
    """
    Independent fixture for Selenium Grid testing.
    Does not depend on conftest.py driver fixture.
    """
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        grid_driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        grid_driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        grid_driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
    grid_driver.maximize_window()
    yield grid_driver

    try:
        grid_driver.quit()
    except Exception as e:
        print(f"Error quitting driver: {e}")


@pytest.fixture
def home_page(driver):
    driver.get("https://market99.com/")
    return HomePage(driver)


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_page_up(driver, home_page):
    print("[Test] Starting test_page_up...")
    print("Scrolling down using page_down...")
    home_page.page_down()
    time.sleep(2)
    print("Scrolling up using page_up...")
    home_page.page_up()
    time.sleep(2)
    print("[Test] Finished test_page_up.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_page_down(driver, home_page):
    print("[Test] Starting test_page_down...")
    print("Scrolling down using page_down...")
    home_page.page_down()
    time.sleep(2)
    print("[Test] Finished test_page_down.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_scroll_by_pixel(driver, home_page):
    print("[Test] Starting test_scroll_by_pixel...")
    print("Scrolling by 300 pixels...")
    home_page.scroll_by_pixel(300)
    time.sleep(2)
    print("[Test] Finished test_scroll_by_pixel.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_scroll_to_top(driver, home_page):
    print("[Test] Starting test_scroll_to_top...")
    print("Scrolling to top of page...")
    home_page.scroll_to_top()
    time.sleep(2)
    print("[Test] Finished test_scroll_to_top.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_scroll_to_bottom(driver, home_page):
    print("[Test] Starting test_scroll_to_bottom...")
    print("Scrolling to bottom of page...")
    home_page.scroll_to_bottom()
    time.sleep(2)
    print("[Test] Finished test_scroll_to_bottom.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_zoom_in_js(driver, home_page):
    print("[Test] Starting test_zoom_in_js...")
    print("Zooming in using JavaScript...")
    home_page.zoom_in_js()
    time.sleep(2)
    print("[Test] Finished test_zoom_in_js.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_zoom_out_js(driver, home_page):
    print("[Test] Starting test_zoom_out_js...")
    print("Zooming out using JavaScript...")
    home_page.zoom_out_js()
    time.sleep(2)
    print("[Test] Finished test_zoom_out_js.")


@pytest.mark.parametrize("driver", browsers, indirect=True)
def test_mouse_scroll(driver, home_page):
    print("[Test] Starting test_mouse_scroll...")
    print("Scrolling using mouse simulation by 200 pixels...")
    home_page.mouse_scroll(200)
    time.sleep(2)
    print("[Test] Finished test_mouse_scroll.")


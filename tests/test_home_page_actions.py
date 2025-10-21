import pytest
import time
from selenium import webdriver
from page_objects.home_page import HomePage

@pytest.fixture(scope="module")
def driver():
    print("[Setup] Launching browser and opening test page...")
    driver = webdriver.Chrome()
    driver.get("https://market99.com/")  # Use a page with enough content to scroll/zoom
    yield driver
    print("[Teardown] Quitting browser...")
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

def test_page_up(home_page):
    print("[Test] Starting test_page_up...")
    print("Scrolling down using page_down...")
    home_page.page_down()
    time.sleep(2)
    print("Scrolling up using page_up...")
    home_page.page_up()
    time.sleep(2)
    print("[Test] Finished test_page_up.")

def test_page_down(home_page):
    print("[Test] Starting test_page_down...")
    print("Scrolling down using page_down...")
    home_page.page_down()
    time.sleep(2)
    print("[Test] Finished test_page_down.")

def test_scroll_by_pixel(home_page):
    print("[Test] Starting test_scroll_by_pixel...")
    print("Scrolling by 300 pixels...")
    home_page.scroll_by_pixel(300)
    time.sleep(2)
    print("[Test] Finished test_scroll_by_pixel.")

def test_scroll_to_top(home_page):
    print("[Test] Starting test_scroll_to_top...")
    print("Scrolling to top of page...")
    home_page.scroll_to_top()
    time.sleep(2)
    print("[Test] Finished test_scroll_to_top.")

def test_scroll_to_bottom(home_page):
    print("[Test] Starting test_scroll_to_bottom...")
    print("Scrolling to bottom of page...")
    home_page.scroll_to_bottom()
    time.sleep(2)
    print("[Test] Finished test_scroll_to_bottom.")

def test_zoom_in_js(home_page):
    print("[Test] Starting test_zoom_in_js...")
    print("Zooming in using JavaScript...")
    home_page.zoom_in_js()
    time.sleep(2)
    print("[Test] Finished test_zoom_in_js.")

def test_zoom_out_js(home_page):
    print("[Test] Starting test_zoom_out_js...")
    print("Zooming out using JavaScript...")
    home_page.zoom_out_js()
    time.sleep(2)
    print("[Test] Finished test_zoom_out_js.")

def test_mouse_scroll(home_page):
    print("[Test] Starting test_mouse_scroll...")
    print("Scrolling using mouse simulation by 200 pixels...")
    home_page.mouse_scroll(200)
    time.sleep(2)
    print("[Test] Finished test_mouse_scroll.")

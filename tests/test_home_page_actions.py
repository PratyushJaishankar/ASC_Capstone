import pytest
import time
from page_objects.home_page import HomePage

@pytest.fixture
def home_page(driver):
    driver.get("https://market99.com/")
    return HomePage(driver)

def test_page_up(driver, home_page):
    print("[Test] Starting test_page_up...")
    print("Scrolling down using page_down...")
    home_page.page_down()
    time.sleep(2)
    print("Scrolling up using page_up...")
    home_page.page_up()
    time.sleep(2)
    print("[Test] Finished test_page_up.")

def test_page_down(driver, home_page):
    print("[Test] Starting test_page_down...")
    print("Scrolling down using page_down...")
    home_page.page_down()
    time.sleep(2)
    print("[Test] Finished test_page_down.")

def test_scroll_by_pixel(driver, home_page):
    print("[Test] Starting test_scroll_by_pixel...")
    print("Scrolling by 300 pixels...")
    home_page.scroll_by_pixel(300)
    time.sleep(2)
    print("[Test] Finished test_scroll_by_pixel.")

def test_scroll_to_top(driver, home_page):
    print("[Test] Starting test_scroll_to_top...")
    print("Scrolling to top of page...")
    home_page.scroll_to_top()
    time.sleep(2)
    print("[Test] Finished test_scroll_to_top.")

def test_scroll_to_bottom(driver, home_page):
    print("[Test] Starting test_scroll_to_bottom...")
    print("Scrolling to bottom of page...")
    home_page.scroll_to_bottom()
    time.sleep(2)
    print("[Test] Finished test_scroll_to_bottom.")

def test_zoom_in_js(driver, home_page):
    print("[Test] Starting test_zoom_in_js...")
    print("Zooming in using JavaScript...")
    home_page.zoom_in_js()
    time.sleep(2)
    print("[Test] Finished test_zoom_in_js.")

def test_zoom_out_js(driver, home_page):
    print("[Test] Starting test_zoom_out_js...")
    print("Zooming out using JavaScript...")
    home_page.zoom_out_js()
    time.sleep(2)
    print("[Test] Finished test_zoom_out_js.")

def test_mouse_scroll(driver, home_page):
    print("[Test] Starting test_mouse_scroll...")
    print("Scrolling using mouse simulation by 200 pixels...")
    home_page.mouse_scroll(200)
    time.sleep(2)
    print("[Test] Finished test_mouse_scroll.")

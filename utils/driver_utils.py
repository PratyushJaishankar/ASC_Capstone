import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def _local_driver(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome()
    elif browser_name == "firefox":
        return webdriver.Firefox()
    elif browser_name == "edge":
        return webdriver.Edge()
    else:
        raise ValueError(f"Unsupported local browser: {browser_name}")


def _remote_driver(browser_name, remote_url, capabilities_overrides=None):
    caps = None
    if browser_name == "chrome":
        caps = DesiredCapabilities.CHROME.copy()
    elif browser_name == "firefox":
        caps = DesiredCapabilities.FIREFOX.copy()
    elif browser_name == "edge":
        caps = DesiredCapabilities.EDGE.copy()
    else:
        raise ValueError(f"Unsupported remote browser: {browser_name}")

    if capabilities_overrides:
        caps.update(capabilities_overrides)

    # Use positional args for Remote to avoid static analysis warning about keyword names
    return webdriver.Remote(remote_url, caps)


def get_driver(browser: str = "chrome", remote_url: str | None = None, capabilities_overrides: dict | None = None):
    """
    Return a WebDriver instance.

    - If `remote_url` is provided (or environment variable SELENIUM_REMOTE_URL is set), a Remote WebDriver is created.
    - Otherwise a local WebDriver is created.

    Args:
        browser: "chrome" | "firefox" | "edge"
        remote_url: selenium hub/grid URL (optional)
        capabilities_overrides: extra desired capabilities for remote hubs
    """
    # allow environment override
    env_remote = os.environ.get("SELENIUM_REMOTE_URL")
    if remote_url is None and env_remote:
        remote_url = env_remote

    if remote_url:
        return _remote_driver(browser, remote_url, capabilities_overrides)
    else:
        return _local_driver(browser)

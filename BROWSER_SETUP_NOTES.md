# Multi-Browser Test Configuration

## Overview
The test suite now runs automatically on both **Chrome** and **Edge** browsers.

## Changes Made
All test files have been updated to include both browsers in the parametrization:

```python
browsers = ["chrome", "edge"]
```

### Updated Test Files:
1. `tests/test_login_logout.py` - Login/logout tests on both browsers
2. `tests/test_add_address.py` - Add address tests on both browsers
3. `tests/test_add_customer.py` - Customer registration tests on both browsers
4. `tests/test_delete_address.py` - Delete address tests on both browsers
5. `tests/test_search_product.py` - Product search tests on both browsers
6. `tests/test_home_page_actions.py` - Home page interaction tests on both browsers

## Prerequisites
Make sure you have the Edge WebDriver installed:
- **Windows**: Edge WebDriver is typically installed with Microsoft Edge browser
- The `msedgedriver.exe` should be in your PATH or Selenium will manage it automatically

## Running Tests

### Run all tests on both browsers:
```bash
pytest tests/
```

### Run specific test file on both browsers:
```bash
pytest tests/test_login_logout.py
```

### Run tests on only Chrome:
```bash
pytest tests/ -k chrome
```

### Run tests on only Edge:
```bash
pytest tests/ -k edge
```

### Generate Allure Report:
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## How It Works
Each test function decorated with `@pytest.mark.parametrize("driver", browsers, indirect=True)` will:
1. Run first with Chrome browser
2. Run again with Edge browser
3. Each browser run is tracked separately in test reports

## CI/CD Considerations
- Tests run in headless mode when `CI=true` environment variable is set
- Both browsers are configured to support headless execution
- The `driver_utils.py` already supports Edge with proper options

## Troubleshooting

### Edge driver not found:
If you get an error about Edge driver not being found:
1. Make sure Microsoft Edge browser is installed
2. Selenium Manager (built into Selenium 4.6+) should auto-download the driver
3. Or manually download from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

### Tests failing on Edge only:
- Check if there are browser-specific behaviors in the application
- Verify wait times are sufficient for Edge's rendering speed
- Review any JavaScript interactions that might behave differently


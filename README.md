Capstone_Selenium - Test Automation Project

Quick start (Windows cmd.exe)

1) Create and activate a virtual environment (optional but recommended):

    python -m venv .venv
    .venv\Scripts\activate

2) Install dependencies:

    python -m pip install -r requirements.txt

3) Run tests (examples):

- Run all tests with pytest (single process):

    pytest tests

- Run tests in parallel (requires pytest-xdist):

    pytest tests -n auto

- Run tests and collect Allure results:

    pytest tests -n auto --alluredir=reports/allure-results

4) Serve Allure report (requires Allure CLI installed and on PATH):

    allure serve reports/allure-results

If you don't have the Allure CLI, install it from https://docs.qameta.io/allure/

5) Run tests against a Selenium Grid or cloud provider:

- Set the SELENIUM_REMOTE_URL environment variable to your grid/hub URL (example):

    set SELENIUM_REMOTE_URL=http://localhost:4444/wd/hub
    set BROWSER=chrome
    pytest tests -n 1 --alluredir=reports/allure-results

- For cloud providers, set SELENIUM_REMOTE_URL to the provider URL and configure desired capabilities via environment variables or extend `utils/driver_utils.py`.

6) Data sources

- Tests support CSV and Excel (.xlsx) data files (data/*.csv by default). The centralized loader is `data/data_loader.py`.
- Example: `data/add_customer_data.csv`, `data/login_data.csv`, `data/search_data.csv`.
- New: `add_customer_data.csv` supports an optional `result` column. Use `result` with values `success` or `failed` to mark the expected outcome for that row — tests will treat `failed` rows as negative tests (expect validation errors / no redirect) and `success` rows as positive tests (expect successful registration and redirect).
- Example CSV row:

    first_name,last_name,email,password,result
    Jane,Doe,jane.doe+1@example.com,Pass@1234,success

7) Keyword-driven execution

- A simple keyword engine exists at `utils/keyword_engine.py`. Example steps CSV: `data/keywords.csv`.
- To run keywords manually from a script:

    from utils.keyword_engine import load_keywords, run_keywords
    from utils.driver_utils import get_driver

    driver = get_driver('chrome')
    steps = load_keywords('data/keywords.csv')
    run_keywords(driver, steps)
    driver.quit()

Notes & next steps

- Page Factory pattern was intentionally excluded per request.
- Allure decorators are present in tests; consider adding more attachments and step annotations.
- If you plan to use Excel data, ensure `pandas` and `openpyxl` are installed.

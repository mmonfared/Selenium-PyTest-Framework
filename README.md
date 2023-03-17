# PyTest/Selenium Framework

This is a PyTest/Selenium framework template with GitHub Actions integration, Allure report, parallel execution, and multibrowser support.

## Installation

1. Clone this repository.
2. Install the required packages: `pip install -r requirements.txt`.

## Usage

1. To run the test suite: `pytest`.
2. To run the test suite with parallel execution and multibrowser support: `pytest -n 2 --browser chrome,firefox`.
3. To generate the Allure report: `pytest --alluredir=./reports/allure-report && allure serve ./reports/allure-report`.

## Directory Structure

- `tests`: Contains the test files.
- `pages`: Contains the page object model classes.
- `helpers`: Contains the utility functions.
- `drivers`: Contains the web driver executables.
- `logs`: Contains the execution log files.
- `reports`: Contains the Allure report.
- `.github/workflows`: Contains the GitHub Actions configuration file.

### Hierarchy

```
project
│   README.md
│   requirements.txt
│
└───tests
│   │   conftest.py
│   │   test_example.py
│
└───pages
│   │   base_page.py
│   │   home_page.py
│
└───helpers
│   │   utils.py
│
└───drivers
│   │   chromedriver.exe
│   │   geckodriver.exe
│
└───logs
│   │   execution.log
│
└───reports
│   └───allure-report
│
└───.github/workflows
    │   pytest.yml
```

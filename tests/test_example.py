import pytest
from pages.home_page import HomePage


@pytest.mark.parametrize("query", ["pytest", "selenium", "allure"])
def test_search(browser, query):
    home_page = HomePage(browser)
    home_page.load()
    home_page.search(query)
    assert query in home_page.get_title()

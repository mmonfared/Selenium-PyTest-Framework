import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import configs


@pytest.mark.parametrize(("username", "password", "name"),
                         [(configs.credentials['user1']['email'], configs.credentials['user1']['pass'],
                           configs.credentials['user1']['name']),
                          (configs.credentials['user2']['email'], configs.credentials['user2']['pass'],
                           configs.credentials['user2']['name'])])
def test_user_login(init_driver, username, password, name):
    login_page = LoginPage(init_driver)
    home_page = HomePage(init_driver)
    login_page.open_login_page()
    login_page.login(username, password)
    assert name in home_page.get_workspace_text()

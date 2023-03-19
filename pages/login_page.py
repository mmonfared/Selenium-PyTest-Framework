from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class LoginPage(BasePage):
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN_URL = configs.base_url + '/en/login'

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, email, password):
        self.fill_input(self.EMAIL_FIELD, email)
        self.fill_input(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)



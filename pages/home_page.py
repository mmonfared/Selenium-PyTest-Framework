from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    search_box = (By.NAME, "q")

    def load(self):
        self.driver.get("https://www.google.com")

    def search(self, query):
        self.find_element(self.search_box).send_keys(query)
        self.find_element(self.search_box).submit()

    def get_title(self):
        return self.driver.title

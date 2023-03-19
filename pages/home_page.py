from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    WORKSPACE_NAME = (By.CSS_SELECTOR, "[data-cy='workspace-dropdown']")

    def get_workspace_text(self):
        return self.find_element(self.WORKSPACE_NAME).text



import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

load_dotenv()


class DashboardPage(BasePage):

    URL = os.getenv("BASE_URL") + "/dashboard"

    def is_loaded(self):
        return "dashboard" in self.driver.current_url.lower()
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class BasePage:

    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_LINK).click()
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

load_dotenv()


class LoginPage(BasePage):

    URL = os.getenv("BASE_URL") + "/login"

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")

    def open(self):
        self.driver.get(self.URL)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class CreateReportPage(BasePage):

    URL = os.getenv("BASE_URL") + "/new-report"

    SUMMARY_INPUT = (By.NAME, "summary")
    TYPE_DROPDOWN = (By.NAME, "type")
    SEVERITY_DROPDOWN = (By.NAME, "severity")
    PRIORITY_DROPDOWN = (By.NAME, "priority")
    REPRODUCTION_STEP_INPUT = (By.NAME, "step-0")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    SUCCESS_TOAST = (By.XPATH, "//div[@role='alert' and contains(text(), 'Report created successfully')]")

    def open(self):
        self.driver.get(self.URL)

    def enter_summary(self, summary):
        self.driver.find_element(*self.SUMMARY_INPUT).send_keys(summary)

    def select_type(self, type_value):
        dropdown = Select(self.driver.find_element(*self.TYPE_DROPDOWN))
        dropdown.select_by_visible_text(type_value)

    def select_severity(self, severity_value):
        dropdown = Select(self.driver.find_element(*self.SEVERITY_DROPDOWN))
        dropdown.select_by_visible_text(severity_value)

    def select_priority(self, priority_value):
        dropdown = Select(self.driver.find_element(*self.PRIORITY_DROPDOWN))
        dropdown.select_by_visible_text(priority_value)

    def enter_reproduction_step(self, step_text):
        self.driver.find_element(*self.REPRODUCTION_STEP_INPUT).send_keys(step_text)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def create_report(self, summary, type_value, severity_value, priority_value, step_text):
        self.open()
        self.enter_summary(summary)
        self.select_type(type_value)
        self.select_severity(severity_value)
        self.select_priority(priority_value)
        self.enter_reproduction_step(step_text)
        self.click_submit()
        
    def is_success_toast_visible(self):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.SUCCESS_TOAST))
        return True
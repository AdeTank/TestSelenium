import os
import sys
import random
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages.login_page import LoginPage
from pages.report_page import CreateReportPage

load_dotenv()


def test_create_report_happy_path(driver):
    login_page = LoginPage(driver)
    login_page.login(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))

    random_number = random.randint(0, 100000)
    summary = f"Automation Report {random_number}"

    create_report_page = CreateReportPage(driver)
    create_report_page.create_report(
        summary=summary,
        type_value="Bug",
        severity_value="High",
        priority_value="Major",
        step_text="Automation reproduction step"
    )

    assert create_report_page.is_success_toast_visible()
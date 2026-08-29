import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

load_dotenv()


def test_dashboard(driver):
    login_page = LoginPage(driver)
    login_page.login(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_loaded()
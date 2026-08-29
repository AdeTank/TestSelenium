import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages.login_page import LoginPage

load_dotenv()


def test_login_happy_path(driver):
    login_page = LoginPage(driver)
    login_page.login(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))

    assert "dashboard" in driver.current_url.lower()
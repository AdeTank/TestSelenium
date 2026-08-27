import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()
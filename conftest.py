import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests in: chrome, firefox or edge"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    try:
        if browser == "chrome":
            drv = webdriver.Chrome()
        elif browser == "firefox":
            drv = webdriver.Firefox()
        elif browser == "edge":
            drv = webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    except Exception as e:
        pytest.fail(f"Failed to start browser '{browser}': {e}")

    yield drv
    drv.quit()
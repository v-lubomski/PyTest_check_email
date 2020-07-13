from selenium import webdriver
import pytest


@pytest.fixture
def browser(file_name):
    print("\n========== Start browser for test ==========")
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(15)
    yield browser
    print("\n========== Quit browser ==========")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--log", action="store", default="log.txt", help="Write log to file"
    )


@pytest.fixture
def log_file_name(request):
    return request.config.getoption("--log")

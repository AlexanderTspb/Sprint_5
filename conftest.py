import pytest
from selenium import webdriver
from url import Urls

@pytest.fixture(scope="function")
def init_browser():
    driver = webdriver.Chrome()
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()

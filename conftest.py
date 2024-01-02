import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilibox import Toolbox


class TestLandingPage(Toolbox):

    def test_landing_page(self):
        self.test_url()
        expected_landing_page = self.driver.find_element(By.CSS_SELECTOR, '.brand').text
        print(expected_landing_page)
        assert expected_landing_page == "Zero Bank"

    def test_search_box(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, '#searchTerm')
        search_box.send_keys("faketest")
        search_box.send_keys(Keys.ENTER)
        search_res = self.driver.find_element(By.CSS_SELECTOR, '.top_offset > h2').text
        assert search_res == "Search Results:"
        time.sleep(5)
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from utilibox import Toolbox


class TestLogin(Toolbox):
    load_dotenv()
    secret_username = os.getenv('UNAME')
    secret_password = os.getenv('PWORD')
    invalid_password = os.getenv('INPWORD')

    def test_url(self):
        time.sleep(5)
        self.driver.get(os.getenv('BASE_URL'))
        page_url = self.driver.current_url
        print(page_url)
        assert os.getenv('BASE_URL') in page_url

    def test_title(self):
        assert self.driver.title == "Zero - Personal Banking - Loans - Credit Cards"

    def test_login_with_valid_creds(self):
        time.sleep(5)
        self.login(self.secret_username, self.secret_password)
        self.driver.back()
        time.sleep(2)
        assert self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[1].text == self.secret_username

        # for element in driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle'):
        #    print(element.text)

        list_of_elements = [element.text for element in self.driver.find_elements(By.CSS_SELECTOR, 'dropdown-toggle')]
        print(list_of_elements)

        self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-toggle')[1].click()
        self.driver.find_element(By.CSS_SELECTOR, '#logout_link').click()
        time.sleep(2)

    def test_login_with_invalid_creds(self):
        self.login(self.secret_username, self.invalid_password)
        expected_error = 'Login and/or password are wrong.'
        # assert expected_error in driver.find_element(By.CSS_SELECTOR, '.alert-error').text
        assert expected_error in self.driver.find_element(By.XPATH, "//div[@class='alert alert-error']").text

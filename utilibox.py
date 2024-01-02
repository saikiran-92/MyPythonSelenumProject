import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


class Toolbox:
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

    def login(self, uname, pword):
        self.driver.find_element(By.CSS_SELECTOR, '#signin_button').click()
        self.driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys(uname)
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys(pword)
        self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="Sign in"]').click()

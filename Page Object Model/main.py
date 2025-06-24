# Page Object Model

# https://www.tutorialspoint.com/selenium/practice/login.php
# https://www.tutorialspoint.com/selenium/practice/text-box.php

import time
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Pages.test_login import test_login
from Pages.test_text_box import test_text_box

class Website_Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        
    def test_login_page(self):
        driver = self.driver
        test_login_1 = test_login(driver)
        test_login_1.open_page("https://www.tutorialspoint.com/selenium/practice/login.php")
        test_login_1.enter_email("email@email.com")
        test_login_1.enter_password("password")
        test_login_1.click_login_button()
        time.sleep(2)
        
    def test_text_box_page(self):
        driver = self.driver
        test_text_box_1 = test_text_box(driver)
        test_text_box_1.open_page("https://www.tutorialspoint.com/selenium/practice/text-box.php")
        test_text_box_1.enter_fullname("Full Name")
        test_text_box_1.enter_email("email@email.com")
        test_text_box_1.enter_address("Address")
        test_text_box_1.enter_password("Password")
        test_text_box_1.click_submit_button()
        
        time.sleep(2)
        
        
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
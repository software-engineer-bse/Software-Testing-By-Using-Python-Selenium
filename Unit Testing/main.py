# Unit testing
# https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Registration Form
class unit_test_registration_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        cls.driver.maximize_window()
        
    def test_registration_page(self):
        driver = self.driver
        driver.find_element(By.ID, "name").send_keys("Name")
        driver.find_element(By.ID, "email").send_keys("Email@email.com")
        driver.find_element(By.ID, "gender").click()
        driver.find_element(By.ID, "mobile").send_keys("0123456789")
        driver.find_element(By.ID, "dob").send_keys("2002-05-11")
        driver.find_element(By.ID, "subjects").send_keys("Subject")
        driver.find_element(By.ID, "hobbies").click()
        
        
        driver.find_element(By.ID, "state").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[10]/div/div[1]/select/option[4]").click()
        driver.find_element(By.ID, "state").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[10]/div/div[2]/select/option[3]").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[11]/input").click()
        
        time.sleep(2)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()


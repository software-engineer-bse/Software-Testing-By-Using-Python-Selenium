from selenium.webdriver.common.by import By
class test_login:
    def __init__(self, driver):
        self.driver = driver
        self.email_id = "email"
        self.password_id = "password"
        self.button_XPath = "/html/body/main/div/div/div[2]/form/div[3]/input"
        
    def open_page(self, link):
        self.driver.get(link)
        self.driver.maximize_window()
        
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        
    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_XPath).click()
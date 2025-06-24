from selenium.webdriver.common.by import By

class test_text_box:
    def __init__(self, driver):
        self.driver = driver
        self.fullname_id = "fullname"
        self.email_id = "email"
        self.address_id = "address"
        self.password_id = "password"
        self.button_XPath = "/html/body/main/div/div/div[2]/form/div[5]/input"
        
    def open_page(self, link):
        self.driver.get(link)
        self.driver.maximize_window()
        
    def enter_fullname(self, fullname):
        self.driver.find_element(By.ID, self.fullname_id).send_keys(fullname)
        
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
        
    def enter_address(self, address):
        self.driver.find_element(By.ID, self.address_id).send_keys(address)
        
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        
    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.button_XPath).click()
        
        
    
        
        
    
        
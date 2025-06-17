from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.base import BasePage

class AddEmployeePage(BasePage):
    #定位器
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")
        self.FIRST_NAME_INPUT = (By.NAME, "firstName")
        self.MIDDLE_NAME_INPUT =(By.NAME, "middleName")
        self.LAST_NAME_INPUT =(By.NAME, "lastName")
        self.SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")


    def switch_to_add(self):
        self.wait_for_element(self.ADD_BUTTON)
        self.click(self.ADD_BUTTON)

    #等待加载
        self.wait_for_element(self.FIRST_NAME_INPUT)
    def add_employee(self, firstName, middleName, lastName):
        self.wait_for_element((By.NAME, "firstName"))
        self.send_keys(self.FIRST_NAME_INPUT, firstName)
        self.send_keys(self.MIDDLE_NAME_INPUT, middleName)
        self.send_keys(self.LAST_NAME_INPUT, lastName)
        self.click(self.SAVE_BUTTON)

 












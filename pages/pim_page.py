from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.base import BasePage

class PimPage(BasePage):
    #定位器
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.EMPLOYEE_NAME = (By.CSS_SELECTOR, ".oxd-autocomplete-text-input.oxd-autocomplete-text-input--active")
        self.SEARCH_BUTTON = (By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")

    def search_employee(self,employeename):
        self.send_keys(self.EMPLOYEE_NAME, employeename)
        self.click(self.SEARCH_BUTTON)














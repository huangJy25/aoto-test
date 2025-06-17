from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.base import BasePage

class LoginPage(BasePage):
    #定位器
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.USERNAME_INPUT = (By.NAME, "username")
        self.PASSWORD_INPUT = (By.NAME, "password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")

    def login(self, username, password):
        self.wait_for_element((By.NAME, "username"))
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)










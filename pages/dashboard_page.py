from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.base import BasePage

class DashboardPage(BasePage):
    #定位器
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.SWITCH_TO_PIM_BUTTON = (By.LINK_TEXT, "PIM")

    def navigate_to_pim(self):
        self.wait_for_element((By.LINK_TEXT, "PIM"))
        self.click(self.SWITCH_TO_PIM_BUTTON)










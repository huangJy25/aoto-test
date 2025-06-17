import selenium
from selenium import webdriver
import unittest
from common.base import BasePage
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage


class Test_Orange_HRM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_search_and_add(self):
        # 登录功能
        Login_page = LoginPage(self.driver)
        Login_page.login("admin", "admin123")

        # 切换到PIM
        dashboard = DashboardPage(self.driver)
        dashboard.navigate_to_pim()
        #添加员工
        Add_Page = AddEmployeePage(self.driver)
        Add_Page.switch_to_add()
        Add_Page.add_employee("s", "h", "h")



if __name__ == '__main__':
    unittest.main()




# base.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        """
        初始化基础页面类
        :param driver: 已初始化的WebDriver实例
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)  # 默认等待3秒

    # def get_driver():
    #     options = webdriver.chromeOptions()
    #     options.add_argument("--start-maximized")
    #     driver = webdriver.Chrome(options=options)
    #     driver.implicitly_wait(10)
    #     return driver

    def open(self, url):
        """打开指定URL"""
        self.driver.get(url)

    def find_element(self, locator):
        """查找单个元素"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"元素 {locator} 未找到")

    def find_elements(self, locator):
        """查找多个元素"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f"元素列表 {locator} 未找到")

    def click(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """检查元素是否可见"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    def switch_to_frame(self, locator):
        """切换到iframe"""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """切换回默认内容"""
        self.driver.switch_to.default_content()

    def take_screenshot(self, filename):
        """截屏"""
        self.driver.save_screenshot(filename)

    def wait_for_element(self, locator, timeout=10):
        """等待元素出现在 DOM 中"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"元素 {locator} 在 {timeout} 秒内未出现")
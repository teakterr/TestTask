from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, driver, link):
        self.driver = driver
        self.link=link
    def open(self):
        self.driver.get(self.link) 
    def element_clickable(self,locator, time=10):
        try:
            butt=WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(locator)
            )
        except:
            return False
        return butt
    def text_in_element_located(self, locator, text, time=10):
        try:
            element= WebDriverWait(self.driver, time).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except:
            return False
        return element
    def element_is_visible(self, locator, time=10):
        try:
            element=WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator)
            )
        except:
            return False
        return element
    def element_is_located(self, locator, time=10):
        try:
            element=WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator)
            )
        except:
            return False
        return element
    def scroll_to(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator)
        )

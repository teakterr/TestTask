import pytest, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def browser():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.fixture(scope='function')
def browser_with_option():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    chrome_options = Options()
    prefs = {"download.default_directory": current_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    driver.quit()
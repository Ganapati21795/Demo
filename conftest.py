
import pytest
from selenium import webdriver
@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome('/Users/ganapatibhat/Documents/testing_frameworks/Selenium/Demo/chromedriver')
    driver.set_page_load_timeout(10)
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    

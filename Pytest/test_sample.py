import time
import pytest
def test_login(test_setup):
    driver.find_element_by_id("txtUsername").send_keys('Admin')
    driver.find_element_by_id("txtPassword").send_keys('admin123')
    driver.find_element_by_id("btnLogin").click()
    


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "submit").click()
    time.sleep(3)

    assert "Your username is invalid!" in driver.page_source, "Invalid login message not found!"
    driver.quit()

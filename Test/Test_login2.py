from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password23")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("stude")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

time.sleep(5)
driver.quit()

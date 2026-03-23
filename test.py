from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open your app
driver.get("http://localhost:5000")

time.sleep(2)

#Test Page Title
assert "Uptime Monitor" in driver.title
print("Title Test Passed")

#Test Main Heading
heading = driver.find_element(By.TAG_NAME, "h1").text
assert "Intelligent Website Uptime Monitor" in heading
print("Heading Test Passed")

#Check SLA Table Exists
tables = driver.find_elements(By.TAG_NAME, "table")
assert len(tables) >= 2
print("Tables Exist Test Passed")

#Check Status Values (UP/DOWN)
statuses = driver.find_elements(By.XPATH, "//td[@class='UP' or @class='DOWN']")

for status in statuses:
    text = status.text
    assert text in ["UP", "DOWN"]

print("Status Test Passed")

#Check URLs are displayed
urls = driver.find_elements(By.XPATH, "//table[1]//tr/td[1]")

assert len(urls) > 0
print("URL Display Test Passed")

# Close browser
driver.quit()
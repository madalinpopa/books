from selenium import webdriver
from selenium.webdriver.common.by import By, Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from webdriver_manager.firefox import GeckoDriverManager

# url
url = "https://techstepacademy.com/trial-of-the-stones"

# browser
browser = webdriver.Firefox(GeckoDriverManager().install())

# working with alerts
# alert = Alert(browser)

print("I have arrived")
WebDriverWait(browser, 10).until(alert_is_present())
print("An alert appeared")
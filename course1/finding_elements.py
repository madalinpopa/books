from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# start the driver
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

browser.get("http://techstepacademy.com/training-ground")

# in broser console you can search for a css element using
# $$(). For xpath you can use $x()
input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"
product1_xpath_locator = "//b[text()='Product 1']/../../p"

# Assign elements
input2_elem = browser.find_element_by_css_selector(input2_css_locator)
butn4_elem = browser.find_element_by_xpath(button4_xpath_locator)

# Manipuate
input2_elem.send_keys("Test text")
butn4_elem.click()
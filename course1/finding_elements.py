from selenium import webdriver
from webdriver_manager.firefox import FirefoxDriveManager

# start the driver
driver = webdriver.Firefox(FirefoxDriveManager().install())

# in broser console you can search for a css element using
# $$(). For xpath you can use $x()
input2_locator = "input[id='ipt2']"

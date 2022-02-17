from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# url
url = "https://techstepacademy.com/trial-of-the-stones"

# browser
browser = webdriver.Firefox(GeckoDriverManager().install())

# to manipulate multiple windows, you need to create
# multiple browser instances.

# to open new tabs you can use execute_script to execute javascript.
# script.
browser.execute_script("window.open('https://google.com')")

# to get the open windows (tabs)
tabs = browser.window_handles 

# to switch to a tab. You need to keep in mind that the
# tabs are not in order. If you have multiple tabs, you cannot
# relay on index to switch tabs.
browser.switch_to.window(tabs[0])

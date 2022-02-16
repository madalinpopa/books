from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# url
url = "https://techstepacademy.com/trial-of-the-stones"

# initiate the brwoser
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(url)

# locators
stone_input_css_selector = "input[id='r1Input']"
button_css_selector = 'button#r1Btn'
stone_result_selector = "div#passwordBanner > h4"
secrets_input_css_selector = "input#r2Input"
secret_answer_butn_css_selector = "button#r2Butn"

# Ridle of Stones
stone_input_elm = browser.find_element(By.ID, 'r1Input')
stone_answer_butn = browser.find_element(By.CSS_SELECTOR, button_css_selector) 
stone_result = browser.find_element(By.CSS_SELECTOR, stone_input_css_selector)

# Riddle of Secrets
secrets_input = browser.find_element(By.CSS_SELECTOR, secrets_input_css_selector)
secret_answer_butn = browser.find_element(By.CSS_SELECTOR, secret_answer_butn_css_selector)

# Two Merchants
# Simple approach
richest_merchant_name = browser.find_element(By.XPATH, "//p[text()='3000']/../span")
merchant_input = browser.find_element(By.ID, 'r3Input')
merchant_answer_butn = browser.find_element(By.CSS_SELECTOR, "button#r3Butn")
check_butn = browser.find_element(By.CSS_SELECTOR, "button[name='checkButn']")

complete_msg = browser.find_element(By.CSS_SELECTOR, "div#trialCompleteBanner h4")

stone_input_elm.send_keys("rock")
stone_answer_butn.click()
password = stone_result.text

secrets_input.send_keys("bamboo")
secret_answer_butn.click()

merchant_input.send_keys(richest_merchant_name.text)
merchant_answer_butn.click()

check_butn.click()
assert complete_msg.text == "Trial Complete"
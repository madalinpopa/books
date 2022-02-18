from selenium.webdriver import Firefox

class BasePage():

    url = None

    def __init__(self, driver: Firefox) -> None:
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
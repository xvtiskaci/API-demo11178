from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class BrowserFactory:
    @staticmethod
    def get_browser(browser="chrome"):
        if browser.lower() == "chrome":

            return webdriver.Chrome()
        elif browser == "Safari":
            return webdriver.Safari()

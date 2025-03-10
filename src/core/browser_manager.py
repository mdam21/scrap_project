from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from ..config.settings import CHROME_CONFIG, FIREFOX_CONFIG

class BrowserManager:
    @staticmethod
    def init_driver(browser_type="chrome", headless=False):
        if browser_type == "chrome":
            options = webdriver.ChromeOptions()
            options.binary_location = CHROME_CONFIG["binary_location"]
            
            for arg in CHROME_CONFIG["options"]:
                options.add_argument(arg)
                
            if headless:
                options.add_argument("--headless")
            
            # Usar ruta del driver desde settings
            service = ChromeService(executable_path=CHROME_CONFIG["driver_path"])
            return webdriver.Chrome(service=service, options=options)
        
        elif browser_type == "firefox":
            service = FirefoxService(executable_path=FIREFOX_CONFIG["driver_path"])
            return webdriver.Firefox(service=service)
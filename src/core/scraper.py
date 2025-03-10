from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..config.settings import CHROME_CONFIG

class Scraper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, CHROME_CONFIG["wait_time"])
        
    def search_content(self, phrase):
        search_url = f"{CHROME_CONFIG['base_url']}{phrase}"
        self.driver.get(search_url)
        self._wait_for_results()
        
    def _wait_for_results(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )
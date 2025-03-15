import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.decorators import cerrar_navegador
from config.sites import SITE_CONFIG

@cerrar_navegador(headless=False)
def scrape_noticias(driver, query):
    url = f"{SITE_CONFIG['el_universo']['url']}/resultados/?search={query}"
    driver.get(url)

    # Espera explícita para asegurar que la página cargó completamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, SITE_CONFIG['el_universo']['content_selector']))
    )

    html = driver.page_source
    # Aquí puedes usar BeautifulSoup o cualquier parser para extraer contenido específico.
    return html

if __name__ == "__main__":
    contenido = scrape_noticias()
    print(contenido[:500])  
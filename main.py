from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar opciones para Chromium
chrome_options = Options()
chrome_options.binary_location = "/snap/bin/chromium"  # Asegurar que usa Chromium en lugar de Google Chrome
chrome_options.add_argument("--no-sandbox")  # Evita problemas de permisos
chrome_options.add_argument("--disable-dev-shm-usage")  # Previene errores en memoria compartida
chrome_options.add_argument("--disable-gpu")  # Desactiva la aceleración por hardware
chrome_options.add_argument("--remote-debugging-port=9222")  # Permite depuración remota
chrome_options.add_argument("--disable-background-networking")  # Evita bloqueos de red
#chrome_options.add_argument("--headless")  # Si quieres ver la ventana, comenta esta línea

# No necesitas especificar la ruta porque ya está en PATH
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.eluniverso.com/resultados/?search=noboa") # Esperar a que cargue la pagina 



time.sleep(10)

driver.quit()

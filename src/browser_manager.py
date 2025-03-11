from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def iniciar_navegador(headless=False):
    """
    Inicializa el navegador con opciones predefinidas.
    10-03-2025
    mdam
    """
    
    chrome_options = Options()
    chrome_options.binary_location = "/snap/bin/chromium" # Path a chromium
    chrome_options.add_argument("--no-sandbox") # Evita problemas de permisos
    chrome_options.add_argument("--disable-dev-shm-usage") # Evita errores en memoria compartida
    chrome_options.add_argument("--disable-gpu") # Deshabilita la GPU
    chrome_options.add_argument("--remote-debugging-port=9222") # Permite la depuracion remota
    chrome_options.add_argument("--disable-background-networking") # Evita bloques de red

    if headless:
        chrome_options.add_argument("--headless") # Ejecuta el modo invisible si es posible
    
    service = Service() # Inicializa el servicio. No especificamos la ruta porque ya existe ne el PATH
    driver = webdriver.Chrome(service=service, options=chrome_options) 

    return driver

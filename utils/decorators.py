import time
import requests
from functools import wraps
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.browser_manager import iniciar_navegador

def medir_tiempo(func):
    # Decorador que permite calcular el tiempo de demora de una funcion.
    # Date: 10-03-2025
    # Author: mdam
    # Input: function
    # Output: function decorator

    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.5f} segundos")
        return resultado
    return wrapper

def reintentar_scraping(intentos=3, espera=2):
    # Decorator for manage conection errors
    # Date: 10-03-2025
    # Author: mdam
    # Input: function
    # Output: function decorator

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(intentos):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    print(f"Error de conexión. Intento {intento + 1}/{intentos}")
                    time.sleep(espera)
            print(f"Se excedió el número de intentos ({intentos})")
        return wrapper
    return decorator

def cerrar_navegador(headless=False):
    # Decorador que cierra el navegador correctamente incluso si existe un error.
    # Date: 10-03-2025
    # Author: mdam
    # Input: none
    # Output: function decorator

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            driver = iniciar_navegador(headless=headless)
            try:
                return func(driver, *args, **kwargs)
            finally:
                driver.quit()
                print("Navegador cerrado correctamente")
        return wrapper
    return decorator

def esperar_elemento(localizador, valor, tiempo=10):
    # Decorador que permite esperar a que un elemento esté presente en la página.
    # Date: 10-03-2025
    # Author: mdam
    # Input: tipo de localizador, locator value, time

    def decorador(func):
        def envoltura(driver, *args, **kwargs):
            WebDriverWait(driver, tiempo).until(EC.presence_of_element_located((localizador, valor)))
            return func(driver, *args, **kwargs)
        return envoltura
    return decorador

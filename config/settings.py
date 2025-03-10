CHROME_CONFIG = {
    "binary_location": "/snap/bin/chromium",
    "options": [
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--remote-debugging-port=9222",
        "--disable-background-networking"
    ],
    "driver_path": "/usr/local/bin/chromedriver"  # Ruta absoluta
}

FIREFOX_CONFIG = {
    "driver_path": "/usr/local/bin/geckodriver"  # Ruta absoluta
}

SEARCH_SETTINGS = {
    "base_url": "https://www.eluniverso.com/resultados/?search=",
    "wait_time": 10
}
# scrap_project

La distribucion sigue esta forma:
├── config
│   ├── __init__.py
│   ├── settings.py -> configuraciones generales del navegador que se va a utilizar.
│   └── sites.py -> archivo de python que maneja las configuraciones desde un .json. 
│   └── sites.json -> archivo de configuraciones generales de cada sitio a scrapear. 
├── data -> archivos generales. Aqui se guardan los .txt en formato de texto plano previo a hacer el análisis de contenido. 
├── deep_conection.py -> Pruebas para la conexion con la API de deep_seek.
├── drivers -> Drivers generales para configuracion de los navegadores.
│   ├── chromedriver
│   └── geckodriver
├── README.md
├── requirements.txt -> librerias ocupadas.
├── src
│   ├── browser_manager.py -> maneja la creacion y configuracion del navegador de Selenium, para ello debe leer las configuraciones desde settings.py
│   ├── core
│   │   ├── base_scraper.py -> Crea la configuracion para el modulo de scraping. Utiliza decoradores para poder reintentar en caso de un fallo
│   │   └── exceptions.py -> archivo para manejar las excepciones.
│   ├── __init__.py
│   └── scrapers
│       ├── ecuavisa_scraper.py -> modulo de python que scrapea a ecuavisa. carga configuraciones de sites.py.
│       └── el_universo_scraper.py -> modulo que scrapea a el universo.
├── streamlit_app
│   ├── main.py -> Archivo principal de manejo de la app usando streamlit.
│   └── pages -> Carpeta libre, no asignado aun
└── utils
    ├── decorators.py -> decoradores para la 
    ├── __init__.py
    └── logger.py -> Script que crea las instancias para poder generar un log en las paginas de noticias. 

# scrap_project

La distribucion sigue esta forma:
├── config
│   ├── __init__.py
│   ├── settings.py -> configuraciones generales de cada etapa.
│   └── sites.py -> archivo de python que maneja las configuraciones desde un .json
│   └── sites.json -> archivo de configuraciones generales de cada sitio. 
├── data -> archivos generales. Aqui se guardan los .txt en formato de texto plano previo a hacer el análisis de contenido. 
├── deep_conection.py -> Pruebas para la conexion con la API de deep_seek.
├── drivers -> Drivers generales para configuracion de los navegadores.
│   ├── chromedriver
│   └── geckodriver
├── README.md
├── requirements.txt -> librerias ocupadas.
├── src
│   ├── browser_manager.py -> maneja la creacion y configuracion del navegador de Selenium. 
│   ├── core
│   │   ├── base_scraper.py -> 
│   │   └── exceptions.py -> archivo para manejar las excepciones.
│   ├── __init__.py
│   └── scrapers
│       ├── ecuavisa_scraper.py -> modulo de python que scrapea a ecuavisa. carga configuraciones de sites.py.
│       └── el_universo_scraper.py -> modulo que scrapea a el universo.
├── streamlit_app
│   ├── main.py -> Archivo principal de manejo de la app usando streamlit.
│   └── pages -> ??
└── utils
    ├── decorators.py -> decoradores para la 
    ├── __init__.py
    └── logger.py

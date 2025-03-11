# scrap_project

La distribucion sigue esta forma:
.
├── streamlit_app/          # Carpeta principal de Streamlit
│   ├── main.py             # Nuevo archivo principal de Streamlit (punto de entrada)
│   └── pages/              # Páginas de Streamlit (se crean automáticamente al usar Streamlit >= 1.10)
├── src/                    # Lógica de scraping y navegación
│   ├── core/
│   ├── browser_manager.py  # Manejo del navegador (abrir/cerrar, configurar drivers)
│   ├── scraper.py          # Lógica principal de scraping (aquí irían los decoradores)
│   └── __init__.py
├── drivers/                # Controladores de navegador (Chrome, Firefox)
├── utils/                  
│   ├── logger.py           # Decoradores para logging
│   └── __init__.py
├── config/                 
│   ├── settings.py         # Configuraciones (rutas, URLs, timeouts)
│   └── __init__.py
├── data/                   # Datos scrapedados o archivos de entrada
├── requirements.txt        # Dependencias
└── README.md               # Documentación
import json
import os

from pathlib import Path

#print(os.getcwd())
#print(Path(__file__).parent) # 

# Configuracion del path, del .json de configuraciones por pagina
CONFIG_PATH = Path(__file__).parent / "sites.json"


def cargar_config():
    # Function: carga las configuraciones de los sitios desde sites.json. ademas, tiene
    #           un catch de errores.
    # Date: 10-03-2025
    # mdam
    # Input: None
    # Output: dictionary coming from the JSON file. 

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f"No se encontró el archivo de configuración en {CONFIG_PATH}")
    except json.JSONDecodeError as e:
        raise Exception(f"Error al cargar el JSON: {e}")

SITE_CONFIG = cargar_config()
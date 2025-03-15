import streamlit as st
import sys
from pathlib import Path

# Agregar al path la carpeta src. ademas del path del proyecto para que las importaciones funcionen correctamente.
project_root_ = '/home/mdam/Documentos/git_gsky/scrap_project'
sys.path.append(str(project_root_))

# Importamos los scrapers
from src.scrapers.el_universo_scraper import scrape_noticias


st.title("Scraper de Noticias v0.1")

query = st.text_input("Palabras o frase clave", "...")


if st.button("Buscar"):
    with st.spinner("Buscando noticias..."):
        html_contenido = scrape_noticias(query=query)
        st.success("Noticias cargadas correctamente.")
        st.write(html_contenido[:2000])  # muestra parte del HTML o procesa con BeautifulSoup para mostrar resultados más claros.

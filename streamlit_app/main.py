import streamlit as st
from src.scrapers.el_universo_scraper import scrape_noticias

st.title("Scraper El Universo 📰")

query = st.text_input("Buscar noticias en El Universo", "noboa")

if st.button("Buscar"):
    with st.spinner("Buscando noticias..."):
        html_contenido = scrape_noticias(query=query)
        st.success("Noticias cargadas correctamente.")
        st.write(html_contenido[:2000])  # muestra parte del HTML o procesa con BeautifulSoup para mostrar resultados más claros.

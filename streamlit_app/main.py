import streamlit as st
#from src.scrapers import CNNScraper, BBCScraper  # Importar scrapers

st.set_page_config(page_title="News Navigator", layout="wide")
st.title("🕵️‍♂️ Navegador Inteligente de Noticias")

def main():
    st.title("News Scraper")
    site = st.selectbox("Selecciona un sitio", ["CNN", "BBC"])
    url = st.text_input("URL del artículo")

    if st.button("Scrapear"):
        with st.spinner("Procesando..."):
            if site == "CNN":
                scraper = CNNScraper(browser_manager)
            elif site == "BBC":
                scraper = BBCScraper(browser_manager)
            
            article = scraper.extract_article(url)
            st.json(article)

if __name__ == "__main__":
    main()
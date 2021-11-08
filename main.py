import streamlit as st
from funzioni import  countWords, createGraph

st.title("Frequenza delle Parole")
uploaded_file = st.file_uploader("Inserisci un file txt", accept_multiple_files=False, type=["txt"] )
num = st.slider('Seleziona quante parole vuoi visualizzzare nel grafico', 1, 50)
if uploaded_file is not None:
    dict = countWords(uploaded_file)
    st.altair_chart(createGraph(dict, num), use_container_width=True)
    if len(dict) < num:
        st.warning("Il numero di parole richieste è inferiore al numero totale del testo. Sono escluse le parole con 3 o meno lettere")

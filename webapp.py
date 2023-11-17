if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Adicione o código do Streamlit aqui
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests

st.set_option('deprecation.showPyplotGlobalUse', False)


# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title(" ")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Teste de site")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Bem vindos!")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.info("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.warning("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")



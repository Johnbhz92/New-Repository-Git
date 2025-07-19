
import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles.csv') # lendo os dados
st.header('Análise de Anúncios de Vendas de Carros')  # Cabeçalho adicionado
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
disp_button = st.button('Criar gráfico de dispersão')

# Se o botão for clicado escrever uma mensagem
if disp_button:
    st.write('Criando um gráfico de dispersão entre preço e odômetro')
    
    #criar um histograma
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    #exibir um gráfico Plotly
    st.plotly_chart(fig_scatter, use_container_width=True)
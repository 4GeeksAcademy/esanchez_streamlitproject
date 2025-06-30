import streamlit as st
import pandas as pd
from utils import predict_flores

# Título de la aplicación
st.title('Suma de los pétalos')
st.image('iris.jpg', caption='Imagen de iris', use_column_width=True)

# Texto introductorio
st.write('**Ingresa los datos manualmente para realizar la suma de los pétalos de las flores:**')

# Diccionario para almacenar los datos de entrada
input_data = {}

# Lista de columnas para las características de la flor
columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.markdown('Pétalos de la flor 1')
    input_data[columns[0]] = st.number_input(columns[0], value=0.0, key=columns[0])

with col2: 
    st.markdown('Pétalos de la flor 2')
    input_data[columns[1]] = st.number_input(columns[1], value=0.0, key=columns[1])

with col3: 
    st.markdown('Pétalos de la flor 3')
    input_data[columns[2]] = st.number_input(columns[2], value=0.0, key=columns[2])

with col4: 
    st.markdown('Pétalos de la flor 4')
    input_data[columns[3]] = st.number_input(columns[3], value=0.0, key=columns[3])

if st.button('Realizar Predicción'):
    input_df = pd.DataFrame([input_data])
    predicted_value = predict_flores(input_df)

    total_petal_value = sum(input_data.values())

    st.success('Éxito al hacer la suma!')
    st.markdown(f"Suma total de pétalos: `{total_petal_value}`")
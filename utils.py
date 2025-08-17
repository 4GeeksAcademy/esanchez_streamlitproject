import pickle
import streamlit as st

def predict_flores(data):
    # Cargar el modelo previamente entrenado para predecir el tipo de flor
    model = pickle.load(open('models/iris_model.pkl', "rb"))
    # Realizar la predicción con los datos proporcionados
    predictions = model.predict(data) 
    return predictions


def check_client_id(client_id):
    # Simulación
    # Cargar credenciales para la BBDD de la empresa y consultar si el identificador del cliente está activo 
    api_key = st.secrets["DB_USERNAME"]
    ls_ids = [123,12345,12345678]
    return True if client_id in ls_ids else False
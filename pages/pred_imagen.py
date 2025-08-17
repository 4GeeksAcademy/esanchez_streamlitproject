import streamlit as st
from PIL import Image
import numpy as np

# Título de la aplicación
st.title('Adivina tu imagen')

# Cargar la imagen
uploaded_file = st.file_uploader("Añade una imagen", type=["jpg", "jpeg", "png", "webp"])

# Si se carga una imagen
if uploaded_file is not None:
    # Mostrar la imagen
    st.write('**Imagen que has añadido:**')
    image = Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption='Se ha cargado la imagen', use_column_width=True)

    # Convertir la imagen a una matriz de valores de píxeles
    image = np.array(image) / 255.0  # Normalizar los valores de píxeles
    
    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('A ver si advina lo que sale en la imagen'):
        # Predecirla
        pred = predict_imagen(image)

        # Mostrar los resultados de la predicción
        st.success('¡Has acertado!')
        st.write('Mi respuesta es:')
        st.write(pred)
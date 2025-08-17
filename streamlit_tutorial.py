import streamlit as st

def main():
    st.title('Bienvenido al portal predictivo de la empresa XYZ')
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')

    # Los links estarán debajo del título y del texto de bienvenida
    st.page_link("pages/pred_iris_csv.py", label="Predicción con CSV")
    st.page_link("pages/pred_iris_man.py", label="Predicción manual")
    st.page_link("pages/pred_imagen.py", label="Predicción de imagen")

    opcion = st.radio(
        'Seleccione el servicio:',
        (
            'Predicción del tipo de flor (con CSV)',
            'Predicción del tipo de flor (manualmente)',
            'Predicción de imagen'
        ),
        index=0,
        key='option'
    )
    
    if st.button('Empezar!'):
        route_prediction(opcion)

def route_prediction(opcion):
    st.write(f"Elegiste: {opcion}")

if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2
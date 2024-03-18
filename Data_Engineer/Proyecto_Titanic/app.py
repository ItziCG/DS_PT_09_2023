import streamlit as st
import pandas as pd
import joblib
from PIL import Image


# Cargar el modelo entrenado
modelo = joblib.load('/Users/uxue/Desktop/DS_PT_09_2023/Machine_Learning/1-Supervisado/4-Ejercicio/best_model.pkl')

def predecir_sobrevivencia(datos_pasajero):
    prediccion = modelo.predict(datos_pasajero)
    return prediccion


# Función principal de la aplicación
def main():

    st.markdown( "<h1 style='color:black;'>¿ Sobrevivirás al Titanic ?</h1>",unsafe_allow_html=True)

    image = Image.open('/Users/uxue/Desktop/titanic.jpg')  # Ajusta el nombre del archivo a tu imagen
    
    st.image(image, caption='RMS Titanic', use_column_width=True)

    st.markdown("<h2 style='color:black;'>Ingresar datos del pasajero:</h2>", unsafe_allow_html=True)

    edad = st.number_input('Edad', min_value=0, max_value=100, value=30)
    tarifa = st.number_input('Tarifa', min_value=0.0, value=50.0)
    genero = st.selectbox('Género', ['Masculino', 'Femenino'])
    clase = st.selectbox('Clase', ['Primera', 'Segunda', 'Tercera'])
    embarque = st.selectbox('Puerto de Embarque', ['Cherbourg', 'Queenstown', 'Southampton'])
    acompaniantes = st.selectbox('Acompañantes', ['Si', 'No'])

    if st.button('Predecir'):
        # Mapear los valores seleccionados a los requeridos por el modelo
        gender_map = {'Masculino': 0, 'Femenino': 1}
        acomp_map = {'No': 0, 'Si': 1}
        class_1= {'Primera': 1, 'Segunda':0, 'Tercera':0}
        class_2= {'Primera': 0, 'Segunda':1, 'Tercera':0}
        class_3= {'Primera': 0, 'Segunda':0, 'Tercera':1}
        embarked_c= {'Cherbourg':1, 'Queenstown':0, 'Southampton':0}
        embarked_q= {'Cherbourg':0, 'Queenstown':1, 'Southampton':0}
        embarked_s= {'Cherbourg':0, 'Queenstown':0, 'Southampton':1}

        genero_encoded = gender_map[genero]
        acomp_encoded = acomp_map[acompaniantes]
        class_1_enc = class_1[clase]
        class_2_enc = class_2[clase]
        class_3_enc = class_3[clase]
        embarked_c_enc = embarked_c[embarque]
        embarked_q_enc = embarked_q[embarque]
        embarked_s_enc = embarked_s[embarque]

        # Crear un DataFrame con los datos del pasajero
        datos_pasajero = pd.DataFrame({'is_male': [genero_encoded], 'Age': [edad], 'Fare': [tarifa], 'Acompaniantes': [acomp_encoded],
                                       'Pclass_1': [class_1_enc], 'Pclass_2': [class_2_enc], 'Pclass_3': [class_3_enc], 'Embarked_C': [embarked_c_enc], 'Embarked_Q': [embarked_q_enc], 'Embarked_S': [embarked_s_enc]})

        # Realizar la predicción de supervivencia
        prediccion = predecir_sobrevivencia(datos_pasajero)
        if prediccion[0] == 0:
            st.write('Lo siento... El pasajero no sobrevivió 😞')
        else:
            st.balloons()
            st.write('El pasajero sobrevivió!!!')
            

if __name__ == '__main__':
    main()

   
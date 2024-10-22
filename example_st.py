import streamlit as st
import requests

def obtener_datos_climaticos(ciudad, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    respuesta = requests.get(url)
    return respuesta.json()

st.title('Aplicación de Datos Climáticos')

ciudad = st.text_input('Ingrese el nombre de una ciudad:', 'Santiago,CL')
api_key = '83ee17cfe072f2a6879333cb71152367' # Reemplaza con tu propia API Key

if st.button('Obtener Datos Climáticos'):
    datos = obtener_datos_climaticos(ciudad, api_key)
    if datos:
        for k,v in datos.items():
            if k=='weather':
                st.write (k+':')
                for vals,dat in v[0].items():
                    st.write(" ",vals+":",dat)
            elif k=='main'or k=='sys' or k=='wind' or k=='clouds' or k=='coord':
                st.write(k+":")
                for vals,dat in v.items():
                    st.write(" ",vals+":",dat)
            else:
                st.write(f"{k}: {v}")
    else:
        st.write('Error al obtener los datos')
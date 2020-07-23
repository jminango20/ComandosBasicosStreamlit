#Created by Juan Minango
#Core Pkg
import streamlit as st

#TEXT
#title
st.title("Curso Streamlit")
#header
st.header("Encabezado")
#subheader
st.subheader("SubEncabezado")
#text
st.text("Esto es un texto y una prueba")

#MARKDOWN
st.markdown("# Esto es un MarkDown")
#Link
st.markdown("[Google](https://www.google.com)")
url_link = "https://jdtechn.com"
st.markdown(url_link)
#Color/Estilo HTML
html = """
<div style="background-color:tomato;padding:50px">
    <p style="font-size:25px;color:white">Stream Lit es Increible</p>
</div>
"""
st.markdown(html,unsafe_allow_html=True)
#Boostrap Alert/Color Text 
st.success("Exito!")
st.info("Information")
st.warning("Advertencia")
st.error("Error")
st.exception('NameError()')

#MEDIA
#Imagenes
from PIL import Image
img = Image.open("example1.jpg")
st.image(img,width=300,caption="StemLit Imagen")
#Audio
audio_file = open("bach.mp3","rb")
audio_byte = audio_file.read()
st.audio(audio_byte,format="audio/mp3")
#Video
video_file = open("capacitate.mp4","rb")
video_byte = video_file.read()
st.video(video_byte,format="video/mp4")
#URL/Youtube
st.video("https://www.youtube.com/watch?v=Jtler_CFqHI")
#Widget
st.button("Enviar")
if st.button("Saludar"):
    st.text("Hola Mundo")
#checkBox
if st.checkbox("Mostrar/Ocultar"):
    st.text("Texto Mostrado")
#Radio Buton
gender = st.radio("Genero:",["Hombre","Mujer"])
if gender == "Hombre":
    st.info("Es hombre")
elif gender == "Mujer":
    st.info("Es mujer")
#SelectBox
location = st.selectbox("Localizacion: " , ["UK","USA","Canada","Brasil"])
#MultiSeleccion
ocupacion = st.multiselect("Ocupacion",["Professor","Ingeniero","Medico","Musico","Vendedor"])

#TEXT INPUT
nombre = st.text_input("Nombre:","Escribe Aqui")
st.text(nombre)

#NUMBER INPUT
numero = st.number_input("Edad",10,100)
st.text(numero)
precio = st.number_input("Precio")
st.text(precio)

#TEXT AREA
texto = st.text_area("Tu Mensaje","Escribe Aqui")

#SLIDES
slider = st.slider("Tu Nivel",2,6)

#Ballon
#st.balloons()

#DATASCIENCE
st.header("Data Science")
st.write(range(10))
#DataFrame
import pandas as pd
df = pd.read_csv("iris.csv")
#Metodo1
st.subheader("Metodo 1")
st.dataframe(df.head())
#Metodo2
st.subheader("Metodo 2")
st.write(df.head())
#TABLES -> Estatica
st.subheader("Tablas")
st.table(df.head())

#PLOT

#Plot Pkgs
import matplotlib.pyplot as plt
import seaborn as sns
#Area_chart
st.area_chart(df.head(20))
#Bar_chart
st.bar_chart(df.head(20))
#LineChar
st.line_chart(df)
#HeatMap
c_plot = sns.heatmap(df.corr(),annot=True)
st.write(c_plot)
st.pyplot()
#Altair
#Vega

#Date/Time
import datetime
today = st.date_input("Hoy es: ", datetime.datetime.now())
import time
the_time = st.time_input("El Tiempo es: ",datetime.time(10,0))
#Display JSON, CODE
data = {"name": "Juan", "Salario":40000}
st.json(data)
#Display CODE
st.code("import numpy as np")
st.code("import numpy as np",language='python')
julia_code = """
function doit(num::int)
    println(num)
end
"""
st.code(julia_code,language='julia')
#CODIGO
with st.echo():
    #Esto es un comentario
    import textblob

#PROGRESSBAR
st.subheader("Barra Progreso")
my_bar = st.progress(0)
for p in range(20):
    my_bar.progress(p+1)

#SPINNER
st.subheader("Spinner")
with st.spinner("Esperando...."):
    time.sleep(5)
st.success("Finalizado")

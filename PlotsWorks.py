#Core Pkgs
import streamlit as st

#Plot
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #TAgg
import pandas as pd
import numpy as np
import os #Abrir archivos

df = pd.read_csv("iris.csv")
st.dataframe(df)
#Graficos
df.plot(kind='bar')
st.pyplot()
#Maps
df2 = pd.DataFrame(np.random.randn(500,2)/[50,50] + [37.76,-127.4],columns=["latitude","longitude"])
st.map(df2)
#Selector Archivos
#@st.cache
def file_selector(folder_path='./datasets'):
    filenames = os.listdir(folder_path)
    select_files = st.selectbox('Selecciona un archivo',filenames)
    return os.path.join(folder_path,select_files)

filename = file_selector()
st.write("Tu seleccionaste '%s'" %filename)

#SIDEBAR
st.sidebar.header("Acerca")
st.sidebar.text("Hola")

#CSS Logo
def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name),unsafe_allow_html=True)

load_css('icon.css')
load_icon('code')
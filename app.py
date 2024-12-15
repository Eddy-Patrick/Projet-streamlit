import streamlit as st
import pandas as pd 
import numpy as np

file = st.file_uploader("Importer vos données ici", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.head())

df = pd.read_csv("iris.csv")

st.write("Aperçu des données :")
st.dataframe(df)

numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

if len(numerical_cols) > 0:
    st.write("Présentation du graphe :")
    st.line_chart(df[numerical_cols])
else:
    st.write("Aucune colonne numérique disponible pour tracer un graphique.")
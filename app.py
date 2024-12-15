import streamlit as st
import pandas as pd
import numpy as np


st.title("Téléchargez et Visualisez vos Données")


@st.cache_data
def generate_sample_csv():
    data = {
        "Colonne1": np.random.randint(1, 100, 10),
        "Colonne2": np.random.randint(1, 100, 10),
        "Colonne3": np.random.random(10)
    }
    sample_df = pd.DataFrame(data)
    return sample_df.to_csv(index=False)

csv_file = generate_sample_csv()

st.download_button(
    label="Télécharger un fichier CSV exemple",
    data=csv_file,
    file_name="exemple.csv",
    mime="text/csv"
)


file = st.file_uploader("Importer votre fichier CSV ici", type=["csv"])

if file is not None:
    
    df = pd.read_csv(file)
    st.write("Aperçu des données téléchargées :")
    st.dataframe(df.head())
    
    
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    if len(numerical_cols) > 0:
        st.write("Présentation du graphe :")
        st.line_chart(df[numerical_cols])
    else:
        st.write("Aucune colonne numérique disponible pour tracer un graphique.")
else:
    st.write("Veuillez télécharger un fichier CSV pour commencer.")

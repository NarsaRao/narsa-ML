import streamlit as st
import pandas as pd
st.title('Machine Learning App')

st.write('A Basic ML model Builder')
df=pd.read_csv('https://raw.githubusercontent.com/NarsaRao/narsa-ML/refs/heads/master/penguins_cleaned.csv')
df

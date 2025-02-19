import streamlit as st
import pandas as pd
st.title('Machine Learning App')

st.write('A Basic ML model Builder')
with st.expander('DATA'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/NarsaRao/narsa-ML/refs/heads/master/penguins_cleaned.csv')
  df
  
  

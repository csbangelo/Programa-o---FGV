import streamlit as st

st.title('SHOW DAS PODEROSAS')

st.write("Bananilson Farofa")

nome = st.text_input("Digite o seu nome:")
if nome:
                     st.write(nome.upper())

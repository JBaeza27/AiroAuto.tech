#Streamlit
import streamlit as st


st.set_page_config(page_title="Airo Auto", page_icon=":tada:", layout="wide")

st.subheader("Airo Auto");
st.title("Comparison of Automobile Aerodynamics")
Make = st.selectbox(
     'Select the make of the vehicle',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', Make)

Model = st.selectbox(
    'Select the model of the vehicle',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', Model)

Year = st.selectbox(
    'Select the year of the vehicle',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', Year)
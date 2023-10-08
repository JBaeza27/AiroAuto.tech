#Streamlit
import streamlit as st


st.set_page_config(page_title="Airo Auto", page_icon=":tada:", layout="wide")

st.markdown('<h2 style="font-size: 40px;">Airo Auto</h2>', unsafe_allow_html=True)
st.title("Comparison of Automobile Aerodynamics")
<<<<<<< HEAD
st.write("lol")
>>>>>>> e7a44179d029b0d7b0865b2ddb094199ebb78fd8
=======
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
>>>>>>> e91e3e8975658854f5b2906d884d9606a5f434d5

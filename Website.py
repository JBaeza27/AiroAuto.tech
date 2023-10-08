#Streamlit
import streamlit as st


st.set_page_config(page_title="Airo Auto", page_icon=":tada:", layout="wide")

st.markdown('<h2 style="font-size: 40px;">Airo Auto</h2>', unsafe_allow_html=True)
st.title("Comparison of Automobile Aerodynamics")
st.write("lol")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<h2 style="font-size: 30px;">Vehicle 1</h2>', unsafe_allow_html=True)

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

with col2:
    st.markdown('<h2 style="font-size: 30px;">Vehicle 2</h2>', unsafe_allow_html=True)

    Make2 = st.selectbox(
     'Select the make of the vehicle ',
    ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', Make2)

    Model2 = st.selectbox(
        'Select the model of the vehicle ',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', Model2)

    Year2 = st.selectbox(
        'Select the year of the vehicle ',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', Year2)
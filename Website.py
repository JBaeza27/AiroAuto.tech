import streamlit as st
import pandas as pd
import pymongo
import requests
from streamlit_lottie import st_lottie

# Streamlit app
st.set_page_config(page_title="", page_icon=":tada:", layout="wide")
st.markdown('<h1 style="font-size: 50px;">Airo Auto</h1>', unsafe_allow_html=True)



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/19a10b2d-6de7-4a05-9c7a-bfe7ccfbad3e/v3V4DjqTTE.json")

st_lottie(lottie_coding, height=300, key="cargif")


st.markdown("<h1 style='text-align: center; color: white;'>Comparison of Automobile Aerodynamics</h1>", unsafe_allow_html=True)

# Load CSV data
csv_file_path = 'table_data.csv'  # Replace with the path to your CSV file
csv_data = pd.read_csv(csv_file_path)

# Helper function to display data based on selections
def display_data(data, Make, Model, Year, column):
    records = data[(data['Make'] == Make) & (data['Model'] == Model) & (data['Year'] == Year)]
    column.write(records)

def get_cda_value(data, Make, Model, Year):
    record = data[(data['Make'] == Make) & (data['Model'] == Model) & (data['Year'] == Year)]
    return float(record['CdA'].values[0]) if not record.empty else None

# Create columns
col1, col2 = st.columns(2)

# First column selections
with col1:
    st.write("Vehicle 1:")
    Make1 = st.selectbox('Select a Make:', csv_data['Make'].unique())
    Model1 = st.selectbox('Select a Model:', csv_data[csv_data['Make'] == Make1]['Model'].unique())
    Year1 = st.selectbox('Select a Year:', csv_data[(csv_data['Make'] == Make1) & (csv_data['Model'] == Model1)]['Year'].unique())
    if st.button('Show Data 1'):
        display_data(csv_data, Make1, Model1, Year1, col1)

# Second column selections
with col2:
    st.write("Vehicle 2:")
    Make2 = st.selectbox('Select a Make: ', csv_data['Make'].unique())
    Model2= st.selectbox('Select a Model: ', csv_data[csv_data['Make'] == Make2]['Model'].unique())
    Year2 = st.selectbox('Select a Year: ', csv_data[(csv_data['Make'] == Make2) & (csv_data['Model'] == Model2)]['Year'].unique())
    if st.button('Show Data 2'):
        display_data(csv_data, Make2, Model2, Year2, col2)

    #Everything below shows drag effiency
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle



with col1:
    fig, ax = plt.subplots()
    ax.axis([0, 20, 0, 20])
    plt.axis('off')

    Green = Rectangle((7.5, 5),
        width = 5,
        height = 10,
    #   angle = 0,
    #  fill = False,
        color = "Green")
    ax.add_patch(Green)

    print(csv_data['CdA']);

    cda_value1 = get_cda_value(csv_data, Make1, Model1, Year1)
    scaled_CdA1 = cda_value1 * 0.1 if cda_value1 else 0  # or provide a default value
    Yellow = Rectangle((8.75, 10 + scaled_CdA1),
        width = 2.5,
        height = 4,
    #   angle = 0,
    #   fill = False,
        color = "yellow")
    ax.add_patch(Yellow)

    
    cda_value1 = get_cda_value(csv_data, Make1, Model1, Year1)
    scaled_CdA1 = cda_value1 * 0.14 if cda_value1 else 0  # or provide a default value
    Red = Rectangle((9, 12.5 + scaled_CdA1),
        width = 2,
        height = 1,
    #   angle = 0,
    #   fill = False,
        color = "Red")
    ax.add_patch(Red)

    b1 = Rectangle((6.5, 12.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b1)

    b2 = Rectangle((6.5, 5.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b2)

    b3 = Rectangle((12.5, 5.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b3)

    b4 = Rectangle((12.5, 12.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b4)

    plt.show()
    plt.savefig('file.png')

    from PIL import Image

    image = Image.open('file.png')
    st.image(image)

with col2:
    fig, ax = plt.subplots()
    ax.axis([0, 20, 0, 20])
    plt.axis('off')

    Green = Rectangle((7.5, 5),
        width = 5,
        height = 10,
    #   angle = 0,
    #  fill = False,
        color = "Green")
    ax.add_patch(Green)

   
    cda_value2 = get_cda_value(csv_data, Make2, Model2, Year2)
    scaled_CdA2 = cda_value2 * 0.1 if cda_value2 else 0  # or provide a default value
    Yellow = Rectangle((8.75, 10 + scaled_CdA2),
        width = 2.5,
        height = 4,
    #   angle = 0,
    #   fill = False,
        color = "yellow")
    ax.add_patch(Yellow)

    cda_value2 = get_cda_value(csv_data, Make2, Model2, Year2)
    scaled_CdA2 = cda_value2 * 0.14 if cda_value2 else 0  # or provide a default value
    Red = Rectangle((9, 12.5 + scaled_CdA2),
        width = 2,
        height = 1,
    #   angle = 0,
    #   fill = False,
        color = "Red")
    ax.add_patch(Red)

    b1 = Rectangle((6.5, 12.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b1)

    b2 = Rectangle((6.5, 5.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b2)

    b3 = Rectangle((12.5, 5.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b3)

    b4 = Rectangle((12.5, 12.5),
        width = 1,
        height = 2,
    #   angle = 0,
    #   fill = False,
        color = "Black")
    ax.add_patch(b4)

    plt.show()
    plt.savefig('file.png')

    from PIL import Image

    image = Image.open('file.png')
    st.image(image)    


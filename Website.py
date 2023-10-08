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

    Yellow = Rectangle((8.75, 10+(7*0.1)),
        width = 2.5,
        height = 4,
    #   angle = 0,
    #   fill = False,
        color = "yellow")
    ax.add_patch(Yellow)

    Red = Rectangle((9, 12.5+(7*0.14)),
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

    Yellow = Rectangle((8.75, 10+(7*0.1)),
        width = 2.5,
        height = 4,
    #   angle = 0,
    #   fill = False,
        color = "yellow")
    ax.add_patch(Yellow)

    Red = Rectangle((9, 12.5+(7*0.14)),
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
import streamlit as st
from datetime import date

st.title("Chai maker app")

if st.button("Make chai"):
    st.success(f"Your is being ready!")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write('Masala is added')

tea_type = st.radio('Pick your chai base: ', ['Milk','Water'])

st.selectbox('chose flavour', ['adrak', 'tulsi', 'honey'])
sug = st.slider('Sugar level:', 0,5,2)

num = st.number_input("How many cups:", min_value=1, max_value=10, step=1)

name = st.text_input('Enter your name')



if name:
    st.success(f'Welcome {name}, Your order of {num} Cups and {sug} spoons of sugar is added.')

dob = st.date_input('Select your dob:')

today = date.today()

age = today.year - dob.year

st.write(f'age: {age}')
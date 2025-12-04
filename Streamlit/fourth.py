import streamlit as st
import pandas as pd

st.title("Dashboard")

file = st.file_uploader('Upload your csv file', type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader('data preview')
    st.dataframe(df)
    
    st.write('summary stats:', df.describe())

# 48:00

if file:
    names =  df['First Name'].unique()
    selected_name = st.selectbox('Select Name', names)

    filtered_data = df[df['First Name'] == selected_name]
    st.dataframe(filtered_data)

    st.write('summary stats for ' + selected_name, filtered_data.describe())
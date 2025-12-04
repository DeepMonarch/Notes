import streamlit as st
import requests 


# web request and api calls in streamlit
st.title("Live Currency Exchange Rates")

url = 'https://api.exchangerate-api.com/v4/latest/INR'

amount = st.number_input('Enter amount in INR', min_value=0, key='amount_inr')

target_currency = st.selectbox('Convert to: ', ['USD', 'EUR', 'GBP', 'JPY', 'AUD'], key='currency')

if st.button('Convert'):
    response = requests.get(url)
    if response.status_code == 200:
        response_data = response.json()
        rates = response_data['rates']
        converted_amount = amount * rates[target_currency]
        st.write(f"{amount} INR is equal to {converted_amount:.2f} {target_currency}")
    else:
        st.error('Failed to fetch exchange rates. Please try again later.')
        st.stop()
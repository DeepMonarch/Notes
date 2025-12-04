# def main():
#     print("Hello from streamlit-project!")


# if __name__ == "__main__":
#     main()

# uv run main.py

import streamlit as st

st.title('Hello Streamlit')

st.subheader('Brewed with streamlit')

st.text('Welcome to your first interative app')

st.write('Choose your favourite varity of chai')

subjects = st.selectbox("Your favourite subjects: ", ['maths', 'science', 'bme', 'ml', 'dl'])

st.write(f'your choose {subjects}, Excellent choice')

st.success('Your chai has been brewed')


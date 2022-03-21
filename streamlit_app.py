import streamlit as st
st.title("Welcome to my first streamlit app!")
st.header("This is fun")
my_str=str.text_input("what's your name?")

st.text(f'Hello {my_str})

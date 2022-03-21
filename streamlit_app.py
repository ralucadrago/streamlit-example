import streamlit as st
st.title("Welcome to my first streamlit app!")
st.header("This is fun")
nr1=st.text_input("number1")
nr2=st.text_input("number2")

st.title(int(nr1)+int(nr2))

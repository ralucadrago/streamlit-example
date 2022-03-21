import pandas as pd
import streamlit as st

st.title("Oh hey its an app")

st.text("Click the button")
button = st.button("Click meeee")
if button:
    st.title("Why would you do that?")
    
st.text("Do you like making apps?")
yes = st.checkbox("Yes")
no = st.checkbox("No")

if yes and no:
    st.title("🙃")
elif yes:
    st.title("😊")
elif no:
    st.title("😭")

    
options = ["Lisa", "Lisa", "Lisa", "Lisa", "Lisa"]
st.text("Who's your favourite instructor?")
opinion = st.selectbox("Pick an instructor", options)
st.text("Congratulations, you selected {}".format(opinion))

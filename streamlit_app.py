import pandas as pd
import streamlit as st

st.title("Oh hey its an app")

st.text("Click the button")
button = st.button("Click meeee")
if button:
    st.title("Why would you do that?")

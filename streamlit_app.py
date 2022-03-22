import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

st.text("Coffee is very important")
coffee = st.slider("How many coffees do you drink in a day?", 0, 10)
if coffee == 0:
    st.text("Weakling")
elif coffee < 3:
    st.text("Acceptable")
elif coffee < 6:
    st.text("Welcome to adult life")
else:
    st.text("I respect you")

st.title("Time for some data analysis")
df = pd.read_csv("USA_Housing.csv")

st.text("We are going to analyse the USA Housing dataset")
ye = st.button("Click to show data")
if ye:
    df
    
st.text("Let's explore some data 😄")
analysis = ["data frame shape", "pairplot", "heatmap"]
how = st.selectbox("What would you like to see?", analysis)
if how == "data frame shape":
    df.shape
elif how == "pairplot":
    fig, ax = plt.plot()
    ax = sns.pairplot(data = df)
    st.pyplot(fig)
elif how == "heatmap":
    fig, ax = plt.plot()
    ax = sns.heatmap(df.corr(), vmin = -1, vmax = 1, annot = True)
    st.pyplot(fig)
#else:
    #df.describe()
    

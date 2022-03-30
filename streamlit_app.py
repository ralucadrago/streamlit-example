import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import datetime as dt
import statsmodels as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX

temp = pd.read_csv('temperature_modelling.csv')

cloud = pd.read_csv('cloud_cover_modelling.csv')

snow = pd.read_csv('snowfall_modelling.csv')

temp.set_index('date', inplace=True)

cloud.set_index('date', inplace=True)

snow.set_index('date', inplace=True)

sar_temp = SARIMAX(temp, order = (2, 1, 0), seasonal_order = (2, 1, 0, 52.4)).fit()

sar_cloud = SARIMAX(cloud, order = (1, 1, 1), seasonal_order = (1, 1, 1, 52.4)).fit()

sar_snow = SARIMAX(snow, order = (1, 1, 1), seasonal_order = (1, 1, 1, 52.4)).fit()


def nice_day(date, acceptable_temp=10):
    temp_estimate = sar_temp.forecast(steps=date)[-1]
    cloud_estimate = sar_cloud.forecast(steps=date)[-1]
    if temp_estimate < acceptable_temp:
        if cloud_estimate > 0.6:
            return 'Not a nice day!'
        elif cloud_estimate <= 0.6:
            return 'A nice but cold day!'
        else:
            return 'uhm you broke me'
    if temp_estimate >= acceptable_temp:
        if cloud_estimate > 0.6:
            return 'Warm but not nice'
        elif cloud_estimate <= 0.6:
            return 'Congrats! You unlocked a nice day!'
        else:
            return 'uhm you broke me'
          
def snow_day(date):
    snow_estimate = sar_snow.forecast(steps=date)[-1]
    if snow_estimate>0.002:
        return 'OMG A SNOW DAY OMG'
    else:
        return 'No luck on snow soz'

st.title("Sunny Side Up!")
st.header("Hi Friends! Welcome to my capstone project!")
st.text("Lets have some fun! Imput any date below and I will try to tell you if it's going to be a nice day or not!")
demo_date=st.text_input("yyyy-mm-dd")
#st.text("I personally thinik anything under 10C is freezing, so if you agree with me then you're cool! If you don't then I guess tell me what an acceptable temperature is for you:")
#demo_temp=st.text_input("nice day temperature")
nice_day(demo_date)




st.title(demo_date)

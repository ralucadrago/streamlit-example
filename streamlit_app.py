import numpy as np
import pandas as pd
import datetime
import streamlit as st

temp = pd.read_csv('temp_pred.csv')

cloud = pd.read_csv('cloud_pred.csv')

snow = pd.read_csv('snow_pred.csv')

temp['date'] = pd.to_datetime(temp['date'], format='%Y-%m-%d')

cloud['date'] = pd.to_datetime(cloud['date'], format='%Y-%m-%d')

snow['date'] = pd.to_datetime(snow['date'], format='%Y-%m-%d')

temp.set_index('date', inplace=True)

cloud.set_index('date', inplace=True)

snow.set_index('date', inplace=True)

def nice_day(year,month,day,acceptable_temp=10):
    year=int(year)
    month=int(month)
    day=int(day)
    new_temp=temp.iloc[temp.index.get_loc(datetime.datetime(year,month,day),method='nearest')].values
    new_cloud=cloud.iloc[cloud.index.get_loc(datetime.datetime(year,month,day),method='nearest')].values
    
    temp_est=new_temp[0]
    cloud_est=new_cloud[0]
    
    if temp_est < acceptable_temp:
        if cloud_est > 0.6:
            return 'Not a nice day!'
        elif cloud_est <= 0.6:
            return 'A nice but cold day!'
        else:
            return 'uhm you broke me'
        
    if temp_est >= acceptable_temp:
        if cloud_est > 0.6:
            return 'Warm but not nice'
        elif cloud_est <= 0.6:
            return 'Congrats! You unlocked a nice day!'
        else:
            return 'uhm you broke me'
        
def snow_day(year,month,day):
    year=int(year)
    month=int(month)
    day=int(day)
    new_snow=snow.iloc[snow.index.get_loc(datetime.datetime(year,month,day),method='nearest')].values
    snow_est=new_snow[0]
    if snow_est>0.002:
        return 'OMG A SNOW DAY OMG'
    else:
        return 'No luck on snow soz'

    
st.title("Sunny Side Up")
st.header("Welcome to my capstone project! Lets have some fun!")

st.text("""So... Rule number one is never trust the weather person, they're lying to you! 
In the spirit of that, it's my turn to lie to you. 
So nothing that I predict can be held against me for time to come!
""")
st.text("""Now that we got that over with,
the furthest I can take you with this is 2050. 
If you'd like to predict weather past that.... stop, why would you?""")

st.header("Let's predict some weather then:")
year=st.text_input("Year please!", max_chars=4)
month=st.text_input("Month please!")
day=st.text_input("Guess what! Business quarter please!.... Joking day please!")

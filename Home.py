# Import libraries
import pandas as pd
import streamlit as st


# Set page layout to wide for the graphs
st.set_page_config(layout='wide')

# Writing headings and description
st.header('London Bike shares Dataset analysis and Prediction.')

# Add more information on home page
st.subheader('Data gathering:')
st.write("""For this project I am using the London Bike Sharing dataset (link : https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset/data).
Bike sharing in London refers to a public transportation system that allows individuals to rent bicycles for short trips within the city. These bike-sharing programs aim to provide a convenient and sustainable mode of transportation for short-distance travel, offering an alternative to traditional public transportation or personal vehicles.

Bike sharing in London serves various purposes, including providing a flexible and eco-friendly transportation option for short journeys, reducing traffic congestion, promoting healthier lifestyles, and contributing to the city's sustainability goals. Users can rent bikes from docking stations located throughout the city. These docking stations are strategically placed at key transportation hubs, tourist destinations, and busy urban areas. Users can either purchase a membership or make one-off payments at the docking station kiosks.

This data was collected in London from 2015-01-04 until 2017-01-03 in London. The dataset consists of the 'Timestamp' at what time the specific datapoint was collected, the 'count' which is the total number of Bike shares that happened at the specific timestamp as well as a number of weather datapoints such as the temperature, humidity, windspeed ect. All of this data was collected and published by 'Transport for London (TfL) open data'.""")

st.subheader('Data generating process:')
st.write("""As mentioned above, this dataset contains the information about the total number of bike shares, measured for each Hour during the period of 2015-01-04 until 2017-01-03. The dataset has a total of 17 414 entries. Each one of these entries contains the following, 

         "timestamp" - timestamp of when the data was collected, up to the hour.

    "cnt" - the count of a new bike shares for a specific hour.

    "t1" - real temperature in degrees Celcuis.

    "t2" - temperature in degrees Celcuis, "feels like"

    "hum" - humidity in percentage.

    "wind_speed" - wind speed in km/h.

    "weather_code" - category of the weather type. These categories are as follows,
    1 = Clear , mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity 
    2 = scattered clouds / few clouds , 3 = Broken clouds , 4 = Cloudy 7 = Rain/ light Rain shower/ Light rain , 10 = rain with thunderstorm , 26 = snowfall , 94 = Freezing Fog

    "is_holiday" - boolean , yes/no field - 1 if it is a holiday , 0 if it is not a  holiday.

    "is_weekend" - boolean field , yes/no field - 1 if the day is on the weekend, 0 if it is a weekday.

    "season" - category field of the yearly meteorological seasons: 0-spring , 1-summer , 2-fall , 3-winter. """)


# create function to read the data in
@st.cache_data
def read_data():
    # Read in data
    df = pd.read_parquet('https://github.com/Erik-02/Bike-shares/raw/main/data/base_dataset.parquet.gzip')

    return df

# Store data as a variable
df = read_data()

# Set data variable to be used across all pages
st.session_state["data"] = df

import streamlit as st

# In order to be able to display the images of each forecast, we first need to create a dictionary consisting of 2 lists, one for the image name, and another for the image link
image_names = ['NaiveMean', 'NaiveSeasonal', 'NaiveDrift', 'NaiveMovingAverage']
image_links = ['https://github.com/Erik-02/Bike-shares/blob/main/images/naive%20mean.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/naive%20seasonal.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/naive%20drift.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/naive%20MA.png?raw=true']

# Combine lists into a dictionary
images = dict(zip(image_names, image_links))

st.header('Baseline forecasts')
st.write("""A baseline is a simple model that provides reasonable results without requiring a lot of time to come up with them. The type of baseline models that we will be discussing here falls under the Persistence type of algorithms, also known as Naive forecasting models. The persistence algorithm uses the value at the current time step (t) to predict the expected outcome at the next time step (t+1). A baseline in performance gives you an idea of how well all other models will actually perform on your problem. We also use this abseline to compare our other models against. If our more advanced models, which will be discussed next, are not able to improve on the baseline's performance, then there is no need in creating and using them. These models are very simple to understand and easy to implement. """)

# Create a selectbox to select the type of baseline model
baseline_model = st.selectbox('Select the type of baseline model', ['NaiveMean', 'NaiveSeasonal', 'NaiveDrift', 'NaiveMovingAverage'])

if baseline_model == 'NaiveMean':
    expander1 = st.expander('Explanation of the NaiveMean method:')
    expander1.write("""As the name suggests, this model is all about the 'mean' of the time series. The model calculates the avergae value over the entire time series and then predicts that all future values will be equal to this mean value. The prediction for any timestep in the future will then simply be this mean. For example, if we take the mean value from our baseline series, we will see that the mean is 4. Therefore, all future forecasts will be 4, according to the NaiveMean. """)
    st.image(images[baseline_model])
elif baseline_model == 'NaiveSeasonal':
    expander1 = st.expander('Explanation of the NaiveSeasonal method:')
    expander1.write("""This model always predicts the value of K time steps ago. When K=1, this model predicts the last value of the training set. When K>1, it repeats the last K values of the training set. Since our data has a daily pattern AND a weekly pattern, we can choose which pattern to repeat. Although since we are trying to predict 7 days/ 1 week ahead, we are going to repeat the last 7 days. For example, if we refer to our baseline series and we want to predict the next 2 values, this model will simply repeat the previous 2 values, in this case it will repeat [6,4] as the forecast. """)
    st.image(images[baseline_model])
elif baseline_model == 'NaiveDrift':
    expander1 = st.expander('Explanation of the NaiveDrift method:')
    expander1.write("""This model fits a line between the first and last point of the training series, and extends it in the future. This line is simply a straight line from the start to the end. This model's use case is mostly to indicate a trend in the data, if there is any. """)
    st.image(images[baseline_model])
elif baseline_model == 'NaiveMovingAverage':
    expander1 = st.expander('Explanation of the NaiveMovingAverage method:')
    expander1.write("""This model forecasts using an auto-regressive moving average (ARMA). Here we only have to provide it with 1 parameter, which is the chunk legth. The chunk length is the amout of data that we consider to calculate the average. Earlier, in 1.2. Data generating process and feature creation, we talked about the concept of a moving average. This model calculates the moving average for a number of datapoints equal to the cunk length that we set, in this project's case 168, then this model calculates this moving average and predicts that this moving average will always be the same in the future. """)
    st.image(images[baseline_model])


# Import libraries
import streamlit as st

# In order to be able to display the images of each forecast, we first need to create a dictionary consisting of 2 lists, one for the image name, and another for the image link
image_names = ['Pycaret insample', 'Pycaret out of sample']
image_links = ['https://github.com/Erik-02/Bike-shares/blob/main/images/pycaret%20in%20sample.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/pycaret%20out%20of%20sample.png?raw=true']

# Combine lists into a dictionary
images = dict(zip(image_names, image_links))

st.header('Regression models with Pycaret')

# Create an expander to be enable to expand/hide text
expander1 = st.expander('Why Machine Learning can be used for Time series forecasting:')
expander1.write("""The process of using machine learning for time series classification can be classified as supervised learning. Supervised learning is a type of machine learning where an algorithm learns from labeled training data to make predictions or decisions without explicit programming. In supervised learning, the algorithm is provided with a dataset that includes both input features and corresponding output labels or target values. The goal is to learn a mapping from the input features to the output labels, allowing the algorithm to generalize and make accurate predictions on new, unseen data.

In our case, the column containing the number of bicycle shared, also known as the 'count', will be our target column, thet being predicted. All of the other columns such as the temperature, windspeed, dates and even the moving averages is what we call predictor columns. Meaning that these extra columns are used to create a mapping by assigning different weights to each column and then combining each one of these columns along with their assigned weights to produce a predictions.

With machine learning, the algorithms are focused on each row, one at a time, using only the exogenous variables, or predictor columns, to compute a prediction. When doing this, the algorithm does not explicitly only use the past values, but it uses current values. This also means that in order to make future forecasts we also need to know the exogenous features in the future. For example, if we are dividing the temperature in half and using that as our prediction, then we need to know what the temperature will be in the future to be able to divide this value and obtain a prediction. This is showcased in the image below.

To summarize, the success of using other variables to predict a target variable depends on the quality and relevance of the features, the choice of the machine learning algorithm, and the proper tuning of hyperparameters. Iterative refinement of the model based on performance evaluation and feedback is often necessary to achieve the best results. """)

# Display image of how we create future forecasts with machine learning and regression
expander1.image('https://github.com/Erik-02/Bike-shares/blob/main/images/cnt%20temp%20future.png?raw=true')

# Create another expander
expander2 = st.expander('Pycaret for time series forecasting:')
expander2.write("""PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows. It is an end-to-end machine learning and model management tool that speeds up the experiment cycle exponentially and makes you much more productive.

In comparison with the other open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few lines only. This makes experiments exponentially fast and efficient. PyCaret is essentially a Python wrapper around several machine learning libraries and frameworks such as scikit-learn, XGBoost, LightGBM, CatBoost and various other regression techniques. 

Essentially, Pycaret trains over 25 different models and evaluate their performance on the training dataset. Pycaret then chooses the best model, based on metrics such as MAE, MAPE, MSE and RMSE. Pycaret requires us to only specify the training and testing data once, followed by a short setup in order for the process to begin. Pycaret is extremely usefull since we can evaluate a wide variety of regression models all at once. The Pycaret setup is the most important part of this function. In the setup we have to select the the training data, the target column and optionally, the exogenous regressors.

To ensure that we are selecting the best possible model, pycaret uses cross validation. By default, pycaret uses 10 fold validation. With this method we have one data set which we divide randomly into 10 parts. We use 9 of those parts for training and reserve one tenth for testing. We repeat this procedure 10 times each time reserving a different tenth for testing. This method ensures that each model has the ability to perform well on any subset of the data and is ideal when testing machine learning models. The outcome of training these models is then displayed in a table that looks like this: """)

# Add image to display about what the pycaret training process looks like
expander2.image('https://github.com/Erik-02/Bike-shares/blob/main/images/pycaret%20models%20trained.png?raw=true')

# Subheader and text about the regression model that performed the best in this scenario
st.subheader('Predicting with Pycaret, in Sample and Out of sample')
st.write('In order for the Pycaret model to successfully train, we need to provide it with a training and a testing set. When we make predictions in sample, we are predicting the testing values that was used to help train the model and assisted in improving the accuracy. However, when we are making out of sample forecasts, we are making forecasts on data that the model has not seen at any stage before. In order to do this with pycaret, we can either create a future dataframe, with the values such as date and temperature in the future and predict it all at once. However, in this case I used extra explanatory variables such as the moving average and weighted moving average. These variables can only be known at the current time, so in order to adjust for future values, I shifted these values forward by 1. This means that t-1 MA is used to forecast t. Since I only shifted by 1, in order to predict future steps, we use a for loop to predict one step ahead at a time.')

# Create an option for the user to see the in sample and out of sample forecasts
in_out = st.selectbox('Do you want to see the in sample or out of sample forecasts:', ['Pycaret insample', 'Pycaret out of sample'])

# Create if statements to display specific content based on users input:
if in_out == 'Pycaret insample':
    st.image(images[in_out])
elif in_out == 'Pycaret out of sample':
    st.image(images[in_out])
# Import the libraries
import streamlit as st

# In order to be able to display the images of each forecast, we first need to create a dictionary consisting of 2 lists, one for the image name, and another for the image link
image_names = ['StatsForecastAutoArima', 'StatsforecastAutoETS', 'Theta method', 'StatsForecastMSTL', 'Prophet']
image_links = ['https://github.com/Erik-02/Bike-shares/blob/main/images/statsforecast%20auto%20arima.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/auto%20ets.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/theta.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/statsforecast%20mstl.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/prophet.png?raw=true']

# Combine lists into a dictionary
images = dict(zip(image_names, image_links))

# Write the header
st.header('Statistical and Classical forecasting models')
st.write("""Statistical models are significant for understanding and predicting complex data. You can see patterns and relationships and make accurate predictions about future values. As we saw with our seasonal decomposition, our data contains a trend that seems to be moving over time. Our data also has multiple seasonalities such as daily and weekly. Alongside the trend and seasonality, we also have residuals that cannot be explained by the decomposition. As we can see, our time series seems to be quit complex. Thankfully we can make use of the following Statistical methods in order to understand our data better and try to increase the performance accuracy. """)

# Create a selectbox to select the type of statistical model to display
statistical_model = st.selectbox('Select the type of statistical model to display', ['StatsForecastAutoArima', 'StatsforecastAutoETS', 'Theta method', 'StatsForecastMSTL', 'Prophet'])

if statistical_model == 'StatsForecastAutoArima':
    expander = st.expander('Learn more about the StatsForecastAutoArima model:')
    expander.write("""ARIMA is a type of autoregressive model. A statistical model is autoregressive if it predicts future values based on past values. For example, an ARIMA model might seek to predict a stock’s future prices based on its past performance. We can split the Arima term into three terms, AR, I, MA:
AR(p) stands for the autoregressive model, the 'p' parameter is a number that confirms how many previous observations are going to be used to forecast the future values.
I(d) is the differencing part, the d parameter tells how many differencing orders are going to be used to make the series stationary. Stationarity means that the statistical properties of the time series such as the mean and variance remain constant over time. It is important for our time series to be stationary, beacuase if it is we are able to obtain meaningful sample statistics such as means, variances, and correlations with other variables, all of which can help our model to be more accurate.
MA(q) stands for moving average model, the q is the number of observations that we include when calculating the moving average. 

SARIMA is a seasonal ARIMA and it is used with time series with seasonality. This is perfect for us since we already know that our model has some seasonality. [foto van arima/sarima]

The 'Auto' part comes in very handy. Instead of having to analyze various plots and decide what all of the parameters, seen in the equation above, has to be, this model will run through all of the various possibilities and decide which parameters are the best. Since the model is deciding for us, this can save us a lot of time that we were planning to spend when having to do it manually. As we know, even the best can make mistakes, therefore we do not have to decide on these parameters based on our knowledge, but we can allow the model to decide for us. """)
    st.image(images[statistical_model])

elif statistical_model == 'StatsforecastAutoETS':
    expander = st.expander('Learn more about the StatsforecastAutoETS model:')
    expander.write("""Exponential smoothing is a time series forecasting method that can be extended to support data with a systematic trend or seasonal component. This model's prediction is a weighted sum of past observations, but the model explicitly uses an exponentially decreasing weight for past observations. This is also very similar to the EWMA method that was used to create extra features in chapter 1.2. Data generating process and feature creation.

There are three main types of exponential smoothing time series forecasting methods. A simple method that assumes no systematic structure such as trend or seasonality, this is also reffered to as Single Exponential Smoothing. We can also extend this model to include Trend in our modelling. This trend including model is called Double Exponential smoothing and allows us to choose between an Additive or Multiplicative trend. Additive refers to a linear trend, whereas Multiplicative refers to an exponential curve. For longer range (multi-step) forecasts, the trend may continue on unrealistically. As such, it can be useful to dampen the trend over time. Dampening means reducing the size of the trend over future time steps down to a straight line (no trend).

Finally, to include both trend and seasonality in our model, we use the Triple Exponential Smoothing model. Here we can have Additive and Multiplicative seasonality. Linear seasonality means that the seasonality remains the same in length and volume, whereas Multiplicative seasonality allows our seasons to change and evolve over time. The Triple Exponential smoothing model has a total of 8 parameters that we can each change individually. These parameters are as follows:
Alpha: Smoothing factor for the level.
Beta: Smoothing factor for the trend.
Gamma: Smoothing factor for the seasonality.
Trend Type: Additive or multiplicative.
Dampen Type: Additive or multiplicative.
Phi: Damping coefficient.
Seasonality Type: Additive or multiplicative.
Period: Time steps in seasonal period.

Exponential smoothing models can have a lot of parameters to tune, as seen above. This process can become quite difficult for someone who does not know what they are doing. This is where AutoETS comes in. AutoETS allows us to skip the whole manual process of entering the parameters by hand and automatically finds the best parameters for us.  """)
    st.image(images[statistical_model])

elif statistical_model == 'Theta method':
    expander = st.expander('Learn more about the Theta method model:')
    expander.write("""The Theta method is a simple forecasting technique that involves decomposing a time series into its trend and seasonality components and then using a simple smoothing technique to make predictions. It's particularly useful for time series data with a trend and a seasonality pattern.

The Theta method works by first performing a decomposition. This decomposition is where the model breaks the time series into 2 main components, namely the Trend and Seasonality. Then the model smooths the data by employin one of the Exponential smoothing techniques, mentioned above, to predict both the trend and seasonality. The theta model works by using a paramter called the Theta parameter, often denoted by the Greek letter θ. This parameter is used to control the level of smoothing applied to the data. The model then combines the trend and seasonality back together to form the forecast. """)
    st.image(images[statistical_model])
elif statistical_model == 'StatsForecastMSTL':
    expander = st.expander('Learn more about the StatsForecastMSTL model:')
    expander.write("""Multiple seasonal decomposition is what was used to decompose the time series in chapter 1.3. Short data analysis and visualization. Essentially, this method decomposes the time series into the trend component, then all of the seasonalities are extracted, in our case Daily, Weekly and Monthly. The model then forecasts the trend using a custom non-seasonal model and each seasonality using a SeasonalNaive model. At the end of this process, the model then combines all of these predicitons and produces a single forecast for us to use. """)
    st.image(images[statistical_model])
elif statistical_model == 'Prophet':
    expander = st.expander('Learn more about the Prophet model:')
    expander.write("""The core idea behind FBProphet is to model time series data as a combination of trend, seasonality, and noise components. By decomposing the data into these components, the algorithm can generate accurate forecasts that capture the underlying patterns in the data. FBProphet uses a Bayesian framework to model the time series data. This means that the algorithm estimates the posterior distribution of the model parameters, rather than just point estimates. By doing so, the algorithm can generate probabilistic forecasts that provide a measure of uncertainty around the point forecast. FBProphet also allows for the inclusion of additional regressors in the model. Regressors are external variables that may influence the time series, such as holidays, weather patterns, or marketing campaigns. Including regressors in the model can improve the accuracy of the forecasts by capturing the effects of these external variables on the time series. """)
    st.image(images[statistical_model])

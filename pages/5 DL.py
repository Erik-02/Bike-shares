# Import libraries
import streamlit as st

image_names = ['RNN','LSTM','GRU','N-BEATS','N-HITS', 'TCN', 'TRANSFORMER', 'TFT', 'TIDE']
image_links = ['https://github.com/Erik-02/Bike-shares/blob/main/images/rnn.png?raw=true', 
               'https://github.com/Erik-02/Bike-shares/blob/main/images/lstm.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/gru.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/nbeats.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/nhits.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/tcn.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/transformer.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/tft.png?raw=true',
               'https://github.com/Erik-02/Bike-shares/blob/main/images/tide.png?raw=true']

# Combine lists into a dictionary
images = dict(zip(image_names, image_links))

# Write header and starting information
st.header('Deep Learning forecasts')
expander1 = st.expander('Neural networks explanation')
expander1.write("""A neural network — of which recurrent neural networks are one type, among other types such as convolutional networks — is composed of three elementary components: the input layer, the hidden layers, and the output layer. Each layer consists of so-called nodes (aka neurons).

To better understand how Recurrent neural networks (RNNs) work, seen in the following section, we first have to understand how regular neural network's work. Neural networks consists of 3 layers, the input layer, one or more hidden layers and the output layer. Each node, or artificial neuron which is within the hidden layers, connects to one another and has an associated weight and threshold value. If the output of any individual node is above the specified threshold value, that node is activated, sending data to the next layer of the network. Otherwise, no data is passed along to the next layer of the network. """)

expander1.image('https://github.com/Erik-02/Bike-shares/blob/main/images/nn%20diagram.png?raw=true')

expander1.write("""We can think of each individual node as its own linear regression model, composed of input data, weights, a bias and an output. The formula would look something like this: y = w1x1 + b , where 'y' is the output, w1 is the weight, x1 is the input which can be thought of as one specific feature or column from the data that we have and 'b' which is our bias term. The goal of the neural network is to learn the appropriate parameters for w1 and b, so that given our input x1, we can achieve a prediction as close to our target output as possible.

Think of having various features or columns of data. We assign weights to these features, indicating their importance. Larger weights mean the system sees those features as more crucial. Next, each feature is multiplied by its corresponding weight, and the results are added up. This sum then goes through an activation function, determining the final output. If the output surpasses a certain threshold, it triggers the node to send data to the next layer. To put it simply, you start with different features in your data, assign them importance (weights), perform calculations, and if the result is significant, it moves to the next part of the system. This entire process characterizes it as a feedforward neural network.

As we train the model, we’ll want to evaluate its accuracy using a cost or loss function. This is also commonly referred to as the mean squared error (MSE), introduced in chapter 1.5. Evaluation metrics for both performance and effiency.

The aim is to make sure our model fits the data accurately for any specific observation. To achieve this, the model fine-tunes its weights and bias using a cost function and reinforcement learning, working towards reaching a point called convergence, which is like finding the best fit. [kry extra source wat hierdie gradient descend process verduidelik] The algorithm adjusts its weights through a process called gradient descent. This method helps the model figure out which way to move to decrease errors or minimize the cost function. As the model goes through each training example, its parameters shift little by little, gradually getting closer to the best fit or minimum point. """)

expander1.image('https://github.com/Erik-02/Bike-shares/blob/main/images/gradient%20descend.jpg?raw=true')


expander2 = st.expander('Recurrent Neural networks explained:')
expander2.write("""Recurrent neural networks (RNNs) are deep learning models, typically used to solve problems with sequential input data such as time series data, audio and even video data. RNNs are a type of neural network that retains a memory of what it has already processed and thus can learn from previous iterations during its training.

In contrast to what we learned about regular neural networks in the previous section, namely that input data is passed through the nodes to then make a prediction, an RNN contains a hidden state that is feeding it information from previous states. Meaning, the output of a preceding step is used as an input for the current process step. Consider the application of predictiong where a tennis ball will be in the future. Without information about it's past and where it has been, it would be impossible to predict where it would be. However, if we use the information of where it was in the past, we can predict where it will be in the future.""")

expander2.image('https://github.com/Erik-02/Bike-shares/blob/main/images/gif%20ball.gif?raw=true')

expander2.write("""In RNNs, when the network is trying to learn from sequences of data, there's a problem called the "vanishing gradient." This happens during training when the information about far-away events in the sequence gets lost. Imagine you're reading a story, and the network is trying to learn from each sentence. The vanishing gradient problem is like forgetting important details from the beginning of the story as you read further. This happens because when the network tries to learn from the past steps, the learning signals (gradients) become very tiny, almost like they disappear. So, the network struggles to remember things from a long time ago in the sequence. To combat this issue, we use other networks called Long-Short Term Memory (LSTM) models and Gated Recurrent Units (GRU) models.

LSTMs and GRUs were created as a solution to the vanishing gradient problem. They have internal mechanisms called gates that can regulate the flow of information. These gates control what the model remembers from past observations.
""")

# Create a selectbox for the user to select the type of DL model's forecast to show
dl_model = st.selectbox('Select the model to show:', ['RNN','LSTM','GRU','N-BEATS','N-HITS', 'TCN', 'TRANSFORMER', 'TFT', 'TIDE'])

# Create if statements to show certain content based on user input
if dl_model == 'RNN':
    st.image(images[dl_model])
elif dl_model == 'LSTM':
    st.image(images[dl_model])
elif dl_model == 'GRU':
    st.image(images[dl_model])
elif dl_model == 'N-BEATS':
    st.image(images[dl_model])
elif dl_model == 'N-HITS':
    st.image(images[dl_model])
elif dl_model == 'TCN':
    st.image(images[dl_model])
elif dl_model == 'TRANSFORMER':
    st.image(images[dl_model])
elif dl_model == 'TFT':
    st.image(images[dl_model])
elif dl_model == 'TIDE':
    st.image(images[dl_model])

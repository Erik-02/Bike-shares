import streamlit as st
import pandas as pd
import numpy as np
# Visualizations
import plotly.express as px
from plotly_calplot import calplot

# Import data, this has already been done in the home page.
if "data" in st.session_state:
    df = st.session_state["data"]

# Set page layout to wide for the graphs
st.set_page_config(layout='wide')

# Writing headings and description
st.header('Data Analysis and visualization.')
st.write('Data analysis is a very important and crucial part of the Data science process. It is here, where we can visually inspect and asses our data. The following plots have all a very import part to play in understanding our data.')

# create select box
plot = st.selectbox('Select the data to plot:', ['Hourly data', 'Daily totals', 'Monthly totals per year', 'Weekday average per Year', 'Weekday average per Season', 'Hourly ride share pattern per season', 'Calendar plot' ])

# Create if & elif statements to select what to plot
if plot == 'Hourly data':
    st.write('Hourly number of bike shares')
    st.write('The following plot shows us the number of hourly rides as they happpened. This plot is a bit condensed although it shows us the raw side of the data in how much data we have as well as the varying count which we observe.')

    # Create a figure to plot
    fig = px.line(df['cnt'])
    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
elif plot == 'Daily totals':
    st.write('Daily total number of bikes shared')
    st.write('With this plot we can see much more clearly how many rides we had for each day. This plot also shows us clearly that there are repeating patterns for different times of the year.')

    # Create daily grouped data
    # First create a groubpy of each day and sum the total ride share
    daily_cnt_total = df.groupby(df['timestamp'].dt.date)['cnt'].sum()

    # Create a figure to plot
    fig = px.line(daily_cnt_total)
    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
elif plot == 'Monthly totals per year':
    st.write('Monthly totals for each year')
    st.write('Here we can see the monthly total number of rides that ocurred for each month. We are also able to compare the data for both years. In this comparison we can see that the total number of rides stayed consistent over the years. We can also see that the number of rides tend to increase during the middle of the year, this can be due to weather since it is summertime then in the UK.')

    yearly_monthly = pd.DataFrame(df.groupby(['year', 'month'])['cnt'].sum())
    yearly_monthly.reset_index(inplace=True)
    # Plot the monthly totals for each year
    fig = px.histogram(yearly_monthly, x='month', y='cnt', color='year', nbins=12, barmode='group', text_auto=True)  # barmode = ['stack', 'group', 'overlay', 'relative']
    # Update x-axis
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [1,2, 3,4, 5,6, 7,8,9,10, 11, 12],
            ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ))
    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
elif plot == 'Weekday average per Year':
    st.write('Weekday average per Year')
    st.write('It is also important to understand what role does different days of the week do to the total number of rides. With this plot we can see the weekly pattern and see that Weekdays have higher counts than Weekends.')
    # Create a plot that shows the average number of bicycles shared for each day of the week during all the years
    yearly_weekday = pd.DataFrame(df.groupby(['year', 'weekday'])['cnt'].mean())
    yearly_weekday.reset_index(inplace=True)
    # Plot the monthly totals for each year
    # Plot the monthly totals for each year
    fig = px.histogram(yearly_weekday, x='weekday', y='cnt', color='year', nbins=7, barmode='group', text_auto=True)  # barmode = ['stack', 'group', 'overlay', 'relative']
    # Update x-axis
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [0,1,2, 3,4, 5,6],
            ticktext = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        ))
    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
elif plot ==  'Weekday average per Season':
    st.write('Weekday average per Season')
    st.write('Different seasons mean different temperatures during the year. It is important to understand the correlation that each season might have along with our weekly pattern to be able to forecast better.')

    # Create a plot that shows the average number of bicycles shared for each day of the week during all the years
    season_weekday = pd.DataFrame(df.groupby(['season', 'weekday'])['cnt'].mean())
    season_weekday.reset_index(inplace=True)
    # Plot the monthly totals for each year
    # Plot the monthly totals for each year
    fig = px.histogram(season_weekday, x='weekday', y='cnt', color='season', nbins=7, barmode='group', text_auto=True)  # barmode = ['stack', 'group', 'overlay', 'relative']
    
    # Change Legend variable names
    newnames = {'0.0': 'spring' , '1.0': 'summer', '2.0': 'fall', '3.0': 'winter'}
    fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
    
    # Update x-axis
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [0,1,2, 3,4, 5,6],
            ticktext = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        ))

    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
elif plot == 'Hourly ride share pattern per season':
    st.write('Hourly ride share pattern per season')
    st.write('Since we have our data in an Hourly format, we can utilize this extra information to understand the number of rides shares that is happening at different times of the day. Not only this but we can see that the pattern tends to remain the same for each season, although winter has a lower overall count.')

    # Create a plot that shows the average number of bicycles shared for each day of the week during all the years
    season_daily = pd.DataFrame(df.groupby(['season', 'hour'])['cnt'].mean())
    season_daily.reset_index(inplace=True)

    # Create the plot
    fig = px.line(season_daily, x='hour', y='cnt', color='season')

    # Change Legend variable names
    newnames = {'0.0': 'spring' , '1.0': 'summer', '2.0': 'fall', '3.0': 'winter'}
    fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )

    # Update x-axis
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = np.arange(0,24),
        ))

    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
elif plot == 'Calendar plot':
    st.write('Calendar plot')
    st.write('The calendar plot is a nice visual since it allows us to see each day"s worth of data with much more detail than before. This plot is interactive and we can see the count for any specific day without needing to much work to be done. At the right hand side we can also see that the different colours represents different number of counts.')

    calendar_data = pd.DataFrame(df.groupby('date')['cnt'].sum())
    calendar_data.reset_index(inplace=True)

    fig = calplot(
    calendar_data,
    x='date',
    y="cnt",
    gap=0,
    dark_theme=True,
      years_title=True,
        month_lines_width=3, 
    month_lines_color="#fff",
    showscale=True,
    title='Total daily ride shares heatmap',)

    # Plot the figure
    st.plotly_chart(fig, use_container_width=True)
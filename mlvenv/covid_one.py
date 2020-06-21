# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import sys

# load the dataset
dataset_confirmed = pd.read_csv('D:\\Source\\Repos\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_confirmed_us.csv')
dataset_death = pd.read_csv('D:\\Source\\Repos\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_us.csv')

# Array of column names from column 11 (L) to end
dateColNames = dataset_confirmed.columns[11:].values

state = 'Arizona'

# Setup the plot
#years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
weeks = mdates.WeekdayLocator()
months_fmt = mdates.DateFormatter('%Y-%m')

fig, ax = plt.subplots()
#ax.plot('date', 'adj_close', data=data)

# format the ticks
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(months_fmt)
ax.xaxis.set_minor_locator(weeks)


# Get y first so we know how many
confirmed_state = dataset_confirmed.loc[dataset_confirmed['Province_State'] == state, dateColNames]
cum_confirmed = confirmed_state.sum()

deaths_state = dataset_death.loc[dataset_death['Province_State'] == state, dateColNames]
cum_deaths = deaths_state.sum()

# This is a contrived Series.  The data starts in Column 12 (L) and goes
#   out by day.
datesDT = pd.date_range('2020-01-22', periods = len(cum_confirmed), freq='D')


# Set the Date Axis
ax.plot(datesDT,cum_deaths, color='red')
plt.title(state)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
#ax.format_xdata = mdates.DateFormatter('%y-%m-%d')
fig.autofmt_xdate()
plt.show()
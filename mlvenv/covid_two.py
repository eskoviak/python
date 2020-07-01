# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import sys
import argparse

parser = argparse.ArgumentParser(description='Get data from COVID 19 JHU Dataset')
parser.add_argument('fips', metavar='FIPS', nargs=1, type=int, help='The state to display')
args = parser.parse_args()
#print(args.state[0])
#sys.exit()

# load the dataset
dataset_confirmed = pd.read_csv('D:\\Source\\Repos\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_confirmed_us.csv')
dataset_death = pd.read_csv('D:\\Source\\Repos\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_us.csv')

# Array of column names from column 11 (L) to end
dateColNames = dataset_confirmed.columns[11:].values
dates = pd.to_datetime(dateColNames)
#print(dates)
#sys.exit()

#state = 'Minnesota'

# Setup the plot
#years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
weeks = mdates.WeekdayLocator()
months_fmt = mdates.DateFormatter('%Y-%m')
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)
#ax.plot('date', 'adj_close', data=data)

# format the ticks
ax1.xaxis.set_major_locator(months)
ax1.xaxis.set_major_formatter(months_fmt)
ax1.xaxis.set_minor_locator(weeks)


# Get y first so we know how many
confirmed_state = dataset_confirmed.loc[dataset_confirmed['FIPS'] == args.fips[0], dateColNames]
cum_confirmed = confirmed_state.sum()

deaths_state = dataset_death.loc[dataset_death['FIPS'] == args.fips[0], dateColNames]
cum_deaths = deaths_state.sum()

cum_rate = cum_deaths / cum_confirmed


# Set the Date Axis
ax1.stackplot(dates,cum_confirmed, cum_deaths, labels=('Confirmed', 'Death'), colors=('green', 'red'))
ax1.legend()
ax2.plot(dates, cum_rate, color='blue')
plt.title('FIPS '+str(args.fips[0]), loc='center')
plt.xlabel('Date')
ax1.set_ylabel('Incidence')
ax2.set_ylabel('Mobidity Rate')
fig.autofmt_xdate()
plt.show()
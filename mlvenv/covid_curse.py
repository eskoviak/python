#!/usr/bin/python3
import curses
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import sys

dataset_confirmed = pd.read_csv('D:\\Source\\Repos\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_confirmed_us.csv')
dataset_death = pd.read_csv('D:\\Source\\Repos\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_us.csv')
dates = pd.to_datetime(dataset_confirmed.columns[11:].values)
dateColNames = dataset_confirmed.columns[11:].values

def getSeries ( scope, scopeValue):
    if scope == 'US':
        confirmed = dataset_confirmed.loc[:, dateColNames]
        cum_confirmed = confirmed.sum()

        deaths = dataset_death.loc[:, dateColNames]
        cum_deaths = deaths.sum()

        cum_rate = cum_deaths / cum_confirmed

        title = "US"
    elif scope == 'State':
        confirmed = dataset_confirmed.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]
        cum_confirmed = confirmed.sum()

        deaths = dataset_death.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]
        cum_deaths = deaths.sum()

        cum_rate = cum_deaths / cum_confirmed

        title = scopeValue
    elif scope == 'County':
        confirmed = dataset_confirmed.loc[dataset_confirmed['FIPS'] == int(scopeValue), dateColNames]
        cum_confirmed = confirmed.sum()

        deaths = dataset_death.loc[dataset_confirmed['FIPS'] == int(scopeValue), dateColNames]
        cum_deaths = deaths.sum()

        cum_rate = cum_deaths / cum_confirmed

        titledf = dataset_confirmed.loc[dataset_confirmed['FIPS'] == int(scopeValue)]
        index = titledf.index[0]
        title = str(dataset_confirmed.at[index, 'Combined_Key'])

    return(cum_confirmed, cum_deaths, cum_rate, title)

def plot (scope, scopeValue):
    # Setup the plot
    months = mdates.MonthLocator()  # every month
    weeks = mdates.WeekdayLocator()
    months_fmt = mdates.DateFormatter('%Y-%m')
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)

    # format the ticks
    ax1.xaxis.set_major_locator(months)
    ax1.xaxis.set_major_formatter(months_fmt)
    ax1.xaxis.set_minor_locator(weeks)

    (cum_confirmed, cum_deaths, cum_rate, title) = getSeries(scope, scopeValue)
    ax1.stackplot(dates,cum_confirmed, cum_deaths, labels=('Confirmed', 'Death'), colors=('green', 'red'))
    ax1.legend()
    ax2.plot(dates, cum_rate, color='blue')
    plt.title(title, loc='center')
    plt.xlabel('Date')
    ax1.set_ylabel('Incidence')
    ax2.set_ylabel('Mobidity Rate')
    fig.autofmt_xdate()
    plt.show()


#
# MAIN
#
if __name__ == '__main__':
    stdscr = curses.initscr()

    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)


    while 1:
        scope='None'
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(4,1,'Report Types:  ')
        stdscr.addstr(5,3, '1 -- Entire US')
        stdscr.addstr(6,3, '2 -- State')
        stdscr.addstr(7,3, '3 -- County (by FIPS)')
        stdscr.addstr(9,1, 'Enter choice [1..3], q to exit  ')

        curses.echo()    
        c = stdscr.getch()

        if c == ord('1'):
            plot('US', str(b'United States', 'utf-8'))
            continue
        elif c == ord('2'):
            scope = 'State'
            stdscr.addstr(11,1, 'Enter the state: ')
            #(y,x) = curses.getsyx()
            scopeValue  = str(stdscr.getstr(12,1), 'utf-8')
            break
        elif c == ord('3'):
            scope = 'County'
            stdscr.addstr(11,1, 'Enter the FIPS code for the county: ')
            scopeValue = str(stdscr.getstr(12,1), 'utf-8')
            break
        elif c != ord('q'):
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            exit(0)
    curses.noecho

    # Set the Date Axis

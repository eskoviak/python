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
        cum_confirmed = (dataset_confirmed.loc[:, dateColNames]).sum()
        cum_deaths = (dataset_death.loc[:, dateColNames]).sum()
        cum_rate = cum_deaths / cum_confirmed
        title = "US"
    elif scope == 'State':
        cum_confirmed = (dataset_confirmed.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]).sum()
        cum_deaths = ( dataset_death.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]).sum()
        cum_rate = cum_deaths / cum_confirmed
        title = scopeValue
    elif scope == 'County':
        cum_confirmed = (dataset_confirmed.loc[dataset_confirmed['FIPS'] == int(scopeValue), dateColNames]).sum()
        cum_deaths = (dataset_death.loc[dataset_confirmed['FIPS'] == int(scopeValue), dateColNames]).sum()
        cum_rate = cum_deaths / cum_confirmed
        index = (dataset_confirmed.loc[dataset_confirmed['FIPS'] == int(scopeValue)]).index[0]
        title = str(dataset_confirmed.at[index, 'Combined_Key'])

    return(cum_confirmed, cum_deaths, cum_rate, title)

def plot_cumulative (scope, scopeValue):
    # Setup the plot
    months = mdates.MonthLocator()  # every month
    weeks = mdates.WeekdayLocator()
    months_fmt = mdates.DateFormatter('%Y-%m')
    fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, sharex=True)

    # format the ticks
    ax1.xaxis.set_major_locator(months)
    ax1.xaxis.set_major_formatter(months_fmt)
    ax1.xaxis.set_minor_locator(weeks)

    (cum_confirmed, cum_deaths, cum_rate, title) = getSeries(scope, scopeValue)
    title += ' - Cumulative'
    ax1.stackplot(dates,cum_confirmed, cum_deaths, labels=('Confirmed', 'Death'), colors=('green', 'red'))
    ax1.legend(loc=2)
    ax2.plot(dates, cum_rate, color='blue')
    fig.suptitle(title, ha='center')
    plt.xlabel('Date')
    ax1.set_ylabel('Incidence')
    ax2.set_ylabel('Mobidity Rate')
    fig.autofmt_xdate()
    fig.set_size_inches(16, 9)
    plt.show()

def plot_daily(scope, scopeValue):
    # Setup the plot
    months = mdates.MonthLocator()  # every month
    weeks = mdates.WeekdayLocator()
    months_fmt = mdates.DateFormatter('%Y-%m')
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)

    # format the ticks
    ax1.xaxis.set_major_locator(months)
    ax1.xaxis.set_major_formatter(months_fmt)
    ax1.xaxis.set_minor_locator(weeks)

    #(cum_confirmed, cum_deaths, cum_rate, title) = getSeries(scope, scopeValue)
    title = scopeValue + ' - Daily/Rate'
    if scope == 'US':
        daily_sum = (dataset_confirmed.loc[:, dateColNames]).sum(axis=0)
    elif scope == 'State':
        daily_sum = (dataset_confirmed.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]).sum(axis=0)

    prev = 0
    for index, value in daily_sum.items():
        daily_sum.at[index] = value - prev
        prev = value

    ax1.bar(dates, daily_sum, color='blue')
    ax2.semilogy(dates, daily_sum, color='red')
    fig.suptitle(title, ha='center')
    plt.xlabel('Date')
    ax1.set_ylabel('Cases/Day')
    ax2.set_ylabel('LOG Cases/Day')
    fig.autofmt_xdate()
    fig.set_size_inches(16, 9)
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
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(4,1,'Report Types:  ')
        stdscr.addstr(5,3, '1 -- US - Cumulative')
        stdscr.addstr(6,3, '2 -- State - Cumulative')
        stdscr.addstr(7,3, '3 -- County - Cumulative (by FIPS)')
        stdscr.addstr(8,3, '4 -- US - Daily/Rate')
        stdscr.addstr(9,3, '5 -- State -- Daily/Rate')
        stdscr.addstr(11,1, 'Enter choice [1..5], q to exit  ')

        curses.echo()    
        c = stdscr.getch()

        if c == ord('1'):
            plot_cumulative('US', str(b'United States', 'utf-8'))
            continue
        elif c == ord('2'):
            stdscr.addstr(13,1, 'Enter the state: ')
            plot_cumulative('State', str(stdscr.getstr(14,1), 'utf-8'))
            continue
        elif c == ord('3'):
            stdscr.addstr(13,1, 'Enter the FIPS code for the county: ')
            plot_cumulative('County', str(stdscr.getstr(14,1), 'utf-8'))
            continue
        elif c == ord('4'):
            plot_daily('US', str(b'United States', 'utf-8'))
            continue
        elif c == ord('5'):
            stdscr.addstr(13,1, 'Enter the state: ')
            plot_daily('State', str(stdscr.getstr(14,1), 'utf-8'))
            continue
        elif c == ord('q'):
            exit(0)

    # Set the Date Axis

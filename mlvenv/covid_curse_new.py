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

def plot(scope, scopeValue):
    # Setup the plot
    months = mdates.MonthLocator()  # every month
    weeks = mdates.WeekdayLocator()
    months_fmt = mdates.DateFormatter('%Y-%m')
    fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, sharex=True)

    # format the ticks -- note:  formatting ax1 sets all of them
    ax1.xaxis.set_major_locator(months)
    ax1.xaxis.set_major_formatter(months_fmt)
    ax1.xaxis.set_minor_locator(weeks)

    title = scopeValue
    if scope == 'US':
        confirmed_daily_sum = (dataset_confirmed.loc[:, dateColNames]).sum(axis=0)
        death_daily_sum = (dataset_death.loc[:, dateColNames]).sum(axis=0)
    elif scope == 'State':
        confirmed_daily_sum = (dataset_confirmed.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]).sum(axis=0)
        death_daily_sum = (dataset_death.loc[dataset_confirmed['Province_State'] == scopeValue, dateColNames]).sum(axis=0)
    elif scope == 'County':
        confirmed_daily_sum = (dataset_confirmed.loc[dataset_confirmed['FIPS'] == int(scopeValue), dateColNames]).sum(axis=0)
        death_daily_sum = (dataset_death.loc[dataset_confirmed['FIPS'] == int(scopeValue), dateColNames]).sum(axis=0)
        index = (dataset_confirmed.loc[dataset_confirmed['FIPS'] == int(scopeValue)]).index[0]
        title = str(dataset_confirmed.at[index, 'Combined_Key'])

    death_daily_rate = death_daily_sum/confirmed_daily_sum
    confirmed_daily_diff = confirmed_daily_sum.copy()
    prev = 0
    for index, value in confirmed_daily_sum.items():
        confirmed_daily_diff.at[index] = value - prev
        prev = value

    ax1.stackplot(dates,confirmed_daily_sum, death_daily_sum, labels=('Confirmed', 'Death'), colors=('green', 'red'))
    ax1.legend(loc=2)
    ax2.plot(dates, death_daily_rate, color='blue')
    ax3.bar(dates, confirmed_daily_diff, color='blue')
    ax4.semilogy(dates, confirmed_daily_diff, color='red')

    fig.suptitle(title, ha='center')
    plt.xlabel('Date')
    ax1.set_ylabel('Cumulative Cases')
    ax2.set_ylabel('Morbidity Rate')
    ax3.set_ylabel('Cases/Day')
    ax4.set_ylabel('Log Cases/Day')
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
        stdscr.addstr(4,1,'Report Scope:  ')
        stdscr.addstr(5,3, '1 -- US')
        stdscr.addstr(6,3, '2 -- State')
        stdscr.addstr(7,3, '3 -- County')
        stdscr.addstr(9,1, 'Enter choice [1..3], q to exit  ')

        curses.echo()    
        c = stdscr.getch()

        if c == ord('1'):
            plot('US', str(b'United States', 'utf-8'))
            continue
        elif c == ord('2'):
            stdscr.addstr(10,1, 'Enter the state: ')
            scopeValue = str(stdscr.getstr(11,1), 'utf-8')
            plot('State', scopeValue)
            continue
        elif c == ord('3'):
            stdscr.addstr(10,1, 'Enter the FIPS code for the county: ')
            plot('County', str(stdscr.getstr(112,1), 'utf-8'))
            continue
        elif c == ord('q'):
            exit(0)
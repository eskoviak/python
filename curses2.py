#!/usr/bin/python3

import curses

stdscr = curses.initscr()

curses.echo()


# The following act on the window object directly
str_list = []
stdscr.border()
stdscr.addstr(4,1,'Enter your name:  ')
input = stdscr.getstr(5,1)
str_list.append(str(input, 'utf-8'))
stdscr.addstr(6,1,''.join(str_list))

while 1:
    c = stdscr.getch()
    if c == ord('q'):
        break
    elif c == curses.KEY_HOME:
        x=y=0


curses.endwin()

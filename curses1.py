#!/usr/bin/python3

import curses
import curses.textpad
import time

stdscr = curses.initscr()

#curses.noecho()
curses.echo()

# the following are used in the Textpad
#begin_x = 20
#begin_y = 7
#height = 5
#width = 40

#win = curses.newwin(height, width, begin_y, begin_x)

# The following two lines use the curses.textpad object
#tb = curses.textpad.Textbox(win)
#text = tb.edit()

# The following act on the window object directly
str_list = []
str_list.append('Hi ')
stdscr.border()
stdscr.addstr(4,1,'Enter your moniker:  ')
input = stdscr.getstr(5,1)
str_list.append(str(input))
stdscr.addstr(6,1,''.join(str_list))

while 1:
    c = stdscr.getch()
    if c == ord('q'):
        break
    elif c == curses.KEY_HOME:
        x=y=0


curses.endwin()

# -*- coding: utf-8 -*-
"""clox functions."""
import os
import sys
import time
import datetime
import pytz

def clear_screen():
    """
    Clear screen function.

    :return: None
    """
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def run_clock(timezone=None):
    if timezone is None:
        tz = None
    else:
        tz = pytz.timezone(timezone)
    while True:
        clear_screen()
        current_time = datetime.datetime.now(tz=tz).strftime('%H:%M')
        print(current_time)
        time.sleep(1.5)
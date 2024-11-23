# -*- coding: utf-8 -*-
"""clox functions."""
import os
import sys
import time
import datetime
import pytz
from art import tprint

def clear_screen():
    """
    Clear screen function.

    :return: None
    """
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def run_clock(timezone=None, h_shift=0, v_shift=0):
    if timezone is None:
        tz = None
    else:
        tz = pytz.timezone(timezone)
    while True:
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        current_time = datetime.datetime.now(tz=tz).strftime('%H:%M')
        tprint(current_time, sep="\n" + " " * h_shift)
        time.sleep(1.5)
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


def run_clock(timezone=None, v_shift=0, h_shift=0):
    """
    Run clock.

    :param timezone: timezone
    :type timezone: str
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :return: None
    """
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
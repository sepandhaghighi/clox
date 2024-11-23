# -*- coding: utf-8 -*-
"""clox functions."""
import os
import sys
import time
import datetime
import argparse
import pytz
from art import tprint
from .params import TIMEZONE_LIST, CLOX_VERSION
from .params import ADDITIONAL_INFO, EXIT_MESSAGE


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


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.epilog = ADDITIONAL_INFO
    parser.add_argument('--timezone', help='timezone', type=str, choices=TIMEZONE_LIST)
    parser.add_argument('--v-shift', help='vertical shift', type=int, default=0)
    parser.add_argument('--h-shift', help='horizontal shift', type=int, default=0)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    if args.version:
        print(CLOX_VERSION)
    try:
        run_clock(timezone=args.timezone, h_shift=args.h_shift, v_shift=args.v_shift)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)

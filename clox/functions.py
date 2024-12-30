# -*- coding: utf-8 -*-
"""clox functions."""
import os
import sys
import time
import random
import datetime
import argparse
import pytz
from art import tprint
from .params import TIME_FORMATS
from .params import TIMEZONES_LIST, CLOX_VERSION
from .params import ADDITIONAL_INFO, EXIT_MESSAGE
from .params import FACES_MAP, FACES_LIST, FACES_LIST_EXAMPLE_MESSAGE


def clear_screen():
    """
    Clear screen function.

    :return: None
    """
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def get_face(index):
    """
    Return face name.

    :param index: face index
    :type index: int
    :return: face name as str
    """
    if index == -1:
        index = random.choice(sorted(FACES_MAP))
    return FACES_MAP[index]


def show_faces_list():
    """
    Show faces list.

    :return: None
    """
    print("Faces list:\n")
    for i in sorted(FACES_MAP):
        print('Face {}\n'.format(i))
        tprint(FACES_LIST_EXAMPLE_MESSAGE, font=get_face(i))
        print('=' * 80)


def show_timezones_list():
    """
    Show timezones list.

    :return: None
    """
    print("Timezones list:\n")
    for index, timezone in enumerate(TIMEZONES_LIST, 1):
        print("{0}. {1}".format(index, timezone))


def run_clock(timezone=None, v_shift=0, h_shift=0, face=1, no_blink=False):
    """
    Run clock.

    :param timezone: timezone
    :type timezone: str
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :param face: face index
    :type face: int
    :param no_blink: no-blink flag
    :type no_blink: bool
    :return: None
    """
    format_index = 0
    timezone_str = timezone
    if timezone is None:
        tz = None
        timezone_str = "Local"
    else:
        tz = pytz.timezone(timezone)
    v_shift = max(0, v_shift)
    h_shift = max(0, h_shift)
    face = get_face(face)
    while True:
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        current_time = datetime.datetime.now(tz=tz).strftime(TIME_FORMATS[format_index])
        tprint(current_time, font=face, sep="\n" + " " * h_shift)
        print(" " * h_shift, end='')
        print("Timezone: {0}".format(timezone_str))
        time.sleep(1)
        if not no_blink:
            format_index = int(not format_index)


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.epilog = ADDITIONAL_INFO
    parser.add_argument('--timezone', help='timezone', type=str, choices=TIMEZONES_LIST)
    parser.add_argument('--v-shift', help='vertical shift', type=int, default=0)
    parser.add_argument('--h-shift', help='horizontal shift', type=int, default=0)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--face', help='face', type=int, choices=FACES_LIST, default=1)
    parser.add_argument('--faces-list', help='faces list', nargs="?", const=1)
    parser.add_argument('--timezones-list', help='timezones list', nargs="?", const=1)
    parser.add_argument('--no-blink', help='disable blinking mode', nargs="?", const=1)
    args = parser.parse_args()
    if args.version:
        print(CLOX_VERSION)
    elif args.faces_list:
        show_faces_list()
    elif args.timezones_list:
        show_timezones_list()
    else:
        try:
            run_clock(
                timezone=args.timezone,
                h_shift=args.h_shift,
                v_shift=args.v_shift,
                face=args.face,
                no_blink=args.no_blink)
        except (KeyboardInterrupt, EOFError):
            print(EXIT_MESSAGE)

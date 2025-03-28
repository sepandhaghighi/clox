# -*- coding: utf-8 -*-
"""clox functions."""
import os
import sys
import time
from calendar import TextCalendar as GregorianCalendar
import random
import datetime
import jdatetime
import argparse
import pytz
from art import tprint
from .jcalendar import TextCalendar as JalaliCalendar
from .params import HORIZONTAL_TIME_24H_FORMATS, VERTICAL_TIME_24H_FORMATS
from .params import HORIZONTAL_TIME_12H_FORMATS, VERTICAL_TIME_12H_FORMATS
from .params import CLOX_VERSION, DATE_FORMAT
from .params import TIMEZONES_LIST, COUNTRIES_LIST
from .params import ADDITIONAL_INFO, EXIT_MESSAGE
from .params import FACES_MAP, FACES_LIST, CALENDARS_LIST, DATE_SYSTEMS_LIST
from .params import HORIZONTAL_FACES_LIST_EXAMPLE, VERTICAL_FACES_LIST_EXAMPLE
from .params import CLOX_OVERVIEW, CLOX_REPO


def clox_info():
    """
    Print clox details.

    :return: None
    """
    tprint("Clox")
    tprint("V:" + CLOX_VERSION)
    print(CLOX_OVERVIEW)
    print(CLOX_REPO)


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


def show_faces_list(vertical=False):
    """
    Show faces list.

    :param vertical: vertical mode flag
    :type vertical: bool
    :return: None
    """
    mode = "Horizontal"
    example = HORIZONTAL_FACES_LIST_EXAMPLE
    if vertical:
        example = VERTICAL_FACES_LIST_EXAMPLE
        mode = "Vertical"
    print("Faces list ({mode}):\n".format(mode=mode))
    for i in sorted(FACES_MAP):
        print('Face {index}\n'.format(index=i))
        tprint(example, font=get_face(i))
        print('=' * 80)


def show_timezones_list(country=None):
    """
    Show timezones list.

    :param country: country iso3166 code
    :type country: str
    :return: None
    """
    timezones_list = TIMEZONES_LIST
    country_name = "All"
    if country is not None:
        timezones_list = list(map(lambda x: x.upper(), pytz.country_timezones(country)))
        country_name = pytz.country_names[country]
    try:
        print("Timezones list ({country_name}):\n".format(country_name=country_name))
    except Exception:
        print("Timezones list ({country_name}):\n".format(country_name=country.upper()))
    for index, timezone in enumerate(sorted(timezones_list), 1):
        print("{index}. {timezone}".format(index=index, timezone=timezone))


def show_countries_list():
    """
    Show countries list.

    :return: None
    """
    print("Countries list:\n")
    for index, country_code in enumerate(sorted(COUNTRIES_LIST), 1):
        country_name = pytz.country_names[country_code]
        try:
            print("{index}. {country_code} - {country_name}".format(index=index,
                                                                    country_code=country_code, country_name=country_name))
        except Exception:
            print("{index}. {country_code} - {country_name}".format(index=index,
                                                                    country_code=country_code, country_name=country_code))


def print_calendar(mode="month", timezone=None, country=None, v_shift=0, h_shift=0, date_system="gregorian"):
    """
    Print calendar.

    :param mode: calendar mode
    :type mode: str
    :param timezone: timezone
    :type timezone: str
    :param country: country iso3166 code
    :type country: str
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :param date_system: date system
    :type date_system: str
    :return: None
    """
    datetime_lib = datetime
    calendar_obj = GregorianCalendar()
    if date_system == "jalali":
        datetime_lib = jdatetime
        calendar_obj = JalaliCalendar()
    tz = None
    timezone_str = "Local"
    if country is not None:
        timezone = pytz.country_timezones(country)[0].upper()
    if timezone is not None:
        timezone_str = timezone
        tz = pytz.timezone(timezone)
    v_shift = max(0, v_shift)
    h_shift = max(0, h_shift)
    datetime_now = datetime_lib.datetime.now(tz=tz)
    current_date = datetime_now.strftime(DATE_FORMAT)
    print('\n' * v_shift, end='')
    print(" " * h_shift, end='')
    print("Today: {date}".format(date=current_date))
    print(" " * h_shift, end='')
    print("Timezone: {timezone}\n".format(timezone=timezone_str))
    calendar_str = calendar_obj.formatmonth(datetime_now.year, datetime_now.month)
    if mode == "year":
        calendar_str = calendar_obj.formatyear(datetime_now.year)
    print("\n".join([" " * h_shift + x for x in calendar_str.split("\n")]))


def run_clock(
        timezone=None,
        country=None,
        v_shift=0,
        h_shift=0,
        face=1,
        no_blink=False,
        vertical=False,
        hide_date=False,
        hide_timezone=False,
        am_pm=False,
        date_system="gregorian"):
    """
    Run clock.

    :param timezone: timezone
    :type timezone: str
    :param country: country iso3166 code
    :type country: str
    :param v_shift: vertical shift
    :type v_shift: int
    :param h_shift: horizontal shift
    :type h_shift: int
    :param face: face index
    :type face: int
    :param no_blink: no-blink flag
    :type no_blink: bool
    :param vertical: vertical mode flag
    :type vertical: bool
    :param hide_date: hide date flag
    :type hide_date: bool
    :param hide_timezone: hide timezone flag
    :type hide_timezone: bool
    :param am_pm: AM/PM mode flag
    :type am_pm: bool
    :param date_system: date system
    :type date_system: str
    :return: None
    """
    datetime_lib = datetime
    if date_system == "jalali":
        datetime_lib = jdatetime
    format_index = 0
    time_formats = HORIZONTAL_TIME_12H_FORMATS if am_pm else HORIZONTAL_TIME_24H_FORMATS
    if vertical:
        time_formats = VERTICAL_TIME_12H_FORMATS if am_pm else VERTICAL_TIME_24H_FORMATS
    tz = None
    timezone_str = "Local"
    if country is not None:
        timezone = pytz.country_timezones(country)[0].upper()
    if timezone is not None:
        timezone_str = timezone
        tz = pytz.timezone(timezone)
    v_shift = max(0, v_shift)
    h_shift = max(0, h_shift)
    face = get_face(face)
    while True:
        clear_screen()
        print('\n' * v_shift, end='')
        print(" " * h_shift, end='')
        datetime_now = datetime_lib.datetime.now(tz=tz)
        current_time = datetime_now.strftime(time_formats[format_index])
        current_date = datetime_now.strftime(DATE_FORMAT)
        tprint(current_time, font=face, sep="\n" + " " * h_shift)
        if not hide_date:
            print(" " * h_shift, end='')
            print(current_date)
        if not hide_timezone:
            print(" " * h_shift, end='')
            print("Timezone: {timezone}".format(timezone=timezone_str))
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
    parser.add_argument('--timezone', help='timezone', type=str.upper, choices=TIMEZONES_LIST)
    parser.add_argument('--country', help='country (iso3166 code)', type=str.upper, choices=COUNTRIES_LIST)
    parser.add_argument('--v-shift', help='vertical shift', type=int, default=0)
    parser.add_argument('--h-shift', help='horizontal shift', type=int, default=0)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--info', help='info', nargs="?", const=1)
    parser.add_argument('--face', help='face', type=int, choices=FACES_LIST, default=1)
    parser.add_argument('--faces-list', help='faces list', nargs="?", const=1)
    parser.add_argument('--timezones-list', help='timezones list', nargs="?", const=1)
    parser.add_argument('--countries-list', help='countries list', nargs="?", const=1)
    parser.add_argument('--no-blink', help='disable blinking mode', nargs="?", const=1)
    parser.add_argument('--vertical', help='vertical mode', nargs="?", const=1)
    parser.add_argument('--hide-date', help='hide date', nargs="?", const=1)
    parser.add_argument('--hide-timezone', help='hide timezone', nargs="?", const=1)
    parser.add_argument('--am-pm', help='AM/PM mode', nargs="?", const=1)
    parser.add_argument('--calendar', help='calendar mode', type=str.lower, choices=CALENDARS_LIST)
    parser.add_argument(
        '--date-system',
        help='date system',
        type=str.lower,
        choices=DATE_SYSTEMS_LIST,
        default="gregorian")
    args = parser.parse_args()
    if args.version:
        print(CLOX_VERSION)
    elif args.info:
        clox_info()
    elif args.faces_list:
        show_faces_list(vertical=args.vertical)
    elif args.timezones_list:
        show_timezones_list(args.country)
    elif args.countries_list:
        show_countries_list()
    elif args.calendar:
        print_calendar(
            mode=args.calendar,
            timezone=args.timezone,
            country=args.country,
            h_shift=args.h_shift,
            v_shift=args.v_shift,
            date_system=args.date_system)
    else:
        try:
            run_clock(
                timezone=args.timezone,
                country=args.country,
                h_shift=args.h_shift,
                v_shift=args.v_shift,
                face=args.face,
                no_blink=args.no_blink,
                vertical=args.vertical,
                hide_date=args.hide_date,
                hide_timezone=args.hide_timezone,
                am_pm=args.am_pm,
                date_system=args.date_system)
        except (KeyboardInterrupt, EOFError):
            print(EXIT_MESSAGE)

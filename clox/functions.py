# -*- coding: utf-8 -*-
"""clox functions."""
from typing import Optional
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
from colorama import Fore, Back, Style
from .jcalendar import TextCalendar as JalaliCalendar
from .params import HORIZONTAL_TIME_24H_FORMATS, VERTICAL_TIME_24H_FORMATS
from .params import HORIZONTAL_TIME_12H_FORMATS, VERTICAL_TIME_12H_FORMATS
from .params import TIMEZONE_DIFFERENCE_FORMAT, OFFSET_FORMAT
from .params import CLOX_VERSION
from .params import TIMEZONES_LIST, COUNTRIES_LIST, WEEKDAYS_LIST
from .params import ADDITIONAL_INFO, EXIT_MESSAGE
from .params import FACES_MAP, FACES_LIST, CALENDARS_LIST, DATE_SYSTEMS_LIST
from .params import HORIZONTAL_FACES_LIST_EXAMPLE, VERTICAL_FACES_LIST_EXAMPLE
from .params import CLOX_OVERVIEW, CLOX_REPO
from .params import DATE_FORMATS_MAP, DATE_FORMATS_LIST
from .params import COLORS_LIST, INTENSITY_LIST


def print_clox_info() -> None:
    """Print clox info."""
    tprint("Clox")
    tprint("V:" + CLOX_VERSION)
    print(CLOX_OVERVIEW)
    print("Repo : " + CLOX_REPO)


def detect_environment() -> str:
    """Detect running environment."""
    try:
        _ = get_ipython().__class__.__name__
        return "ipython"
    except Exception:
        if sys.platform == "win32":
            return "windows"
        else:
            return "other"


def clear_screen(environment: str) -> None:
    """
    Clear screen function.

    :param environment: environment
    """
    if environment == "ipython":
        from IPython.display import clear_output
        clear_output(wait=True)
    elif environment == "windows":
        os.system('cls')
    else:
        os.system('clear')


def get_face(index: int) -> str:
    """
    Return face name.

    :param index: face index
    """
    if index == -1:
        index = random.choice(sorted(FACES_MAP))
    return FACES_MAP[index]


def set_color(color: str) -> None:
    """
    Set text color.

    :param color: color name
    """
    if color:
        color = color.strip().upper()
        if color.startswith("LIGHT"):
            color += "_EX"
        print(getattr(Fore, color, ""), end="")


def set_bg_color(bg_color: str) -> None:
    """
    Set background color.

    :param bg_color: background color name
    """
    if bg_color:
        bg_color = bg_color.strip().upper()
        if bg_color.startswith("LIGHT"):
            bg_color += "_EX"
        print(getattr(Back, bg_color, ""))


def set_intensity(intensity: str) -> None:
    """
    Set text intensity.

    :param intensity: intensity name
    """
    if intensity:
        intensity = intensity.strip().upper()
        print(getattr(Style, intensity, ""), end="")


def get_timezone_difference(timezone: str, offset_local: float, offset_timezone: float) -> str:
    """
    Return timezone difference.

    :param timezone: timezone
    :param offset_local: manual offset for the local time
    :param offset_timezone: manual offset for the timezone
    """
    direction = "ahead"
    tz = pytz.timezone(timezone)
    datetime_timezone = datetime.datetime.now(tz=tz) + datetime.timedelta(hours=offset_timezone)
    datetime_local = datetime.datetime.now() + datetime.timedelta(hours=offset_local)
    difference = datetime_timezone - tz.localize(datetime_local)
    total_minutes = difference.total_seconds() // 60
    if total_minutes < 0:
        direction = "behind"
        total_minutes = abs(total_minutes)
    if total_minutes == 0:
        direction = "same"
    hours = total_minutes // 60
    minutes = total_minutes % 60
    minutes = round(minutes / 15) * 15
    formatted_difference = TIMEZONE_DIFFERENCE_FORMAT.format(
        hours=int(hours), minutes=int(minutes), direction=direction)
    return formatted_difference


def show_faces_list(vertical: bool = False) -> None:
    """
    Show faces list.

    :param vertical: vertical mode flag
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


def show_timezones_list(country: Optional[str] = None) -> None:
    """
    Show timezones list.

    :param country: country iso3166 code
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


def show_countries_list() -> None:
    """Show countries list."""
    print("Countries list:\n")
    for index, country_code in enumerate(sorted(COUNTRIES_LIST), 1):
        country_name = pytz.country_names[country_code]
        try:
            print("{index}. {country_code} - {country_name}".format(index=index,
                                                                    country_code=country_code, country_name=country_name))
        except Exception:
            print("{index}. {country_code} - {country_name}".format(index=index,
                                                                    country_code=country_code, country_name=country_code))


def show_date_formats_list(date_system: str = "GREGORIAN") -> None:
    """
    Show date formats list.

    :param date_system: date system
    """
    datetime_lib = datetime
    example_year = 1990
    if date_system.upper() == "JALALI":
        datetime_lib = jdatetime
        example_year = 1368
    print("Date formats list:\n")
    example_date = datetime_lib.datetime(year=example_year, month=7, day=23)
    for index, date_format in enumerate(DATE_FORMATS_LIST, 1):
        print("{index}. {date_format_code} - {date_format_example}".format(index=index,
                                                                           date_format_code=date_format, date_format_example=example_date.strftime(DATE_FORMATS_MAP[date_format])))


def get_weekday_id(first_weekday: str, date_system: str = "GREGORIAN") -> int:
    """
    Get weekday id.

    :param first_weekday: first weekday
    :param date_system: date system
    """
    first_weekday_normalized = first_weekday.upper()
    if len(first_weekday) > 2:
        first_weekday_normalized = first_weekday_normalized[:2]
    weekdays = [x[:2] for x in WEEKDAYS_LIST]
    if date_system.upper() == "JALALI":
        weekdays = weekdays[-2:] + weekdays[:-2]
    return weekdays.index(first_weekday_normalized)


def print_calendar(
        mode: str = "MONTH",
        timezone: Optional[str] = None,
        country: Optional[str] = None,
        v_shift: int = 0,
        h_shift: int = 0,
        date_system: str = "GREGORIAN",
        date_format: str = "FULL",
        first_weekday: str = "MONDAY",
        offset_local: float = 0,
        offset_timezone: float = 0) -> None:
    """
    Print calendar.

    :param mode: calendar mode
    :param timezone: timezone
    :param country: country iso3166 code
    :param v_shift: vertical shift
    :param h_shift: horizontal shift
    :param date_system: date system
    :param date_format: date format
    :param first_weekday: first weekday
    :param offset_local: manual offset for the local time
    :param offset_timezone: manual offset for the timezone
    """
    first_weekday_id = get_weekday_id(first_weekday, date_system)
    datetime_lib = datetime
    calendar_obj = GregorianCalendar(first_weekday_id)
    if date_system.upper() == "JALALI":
        datetime_lib = jdatetime
        calendar_obj = JalaliCalendar(first_weekday_id)
    offset_main_timedelta = datetime_lib.timedelta(hours=offset_local)
    tz = None
    timezone_str = "Local"
    if country is not None:
        timezone = pytz.country_timezones(country)[0].upper()
    if timezone is not None:
        timezone_str = timezone
        timezone_diff = get_timezone_difference(
            timezone=timezone,
            offset_local=offset_local,
            offset_timezone=offset_timezone)
        timezone_str += " ({timezone_diff})".format(timezone_diff=timezone_diff)
        tz = pytz.timezone(timezone)
        offset_main_timedelta = datetime_lib.timedelta(hours=offset_timezone)
    v_shift = max(0, v_shift)
    h_shift = max(0, h_shift)
    datetime_timezone = datetime_lib.datetime.now(tz=tz) + offset_main_timedelta
    date_timezone_str = datetime_timezone.strftime(DATE_FORMATS_MAP[date_format.upper()])
    print('\n' * v_shift, end='')
    print(" " * h_shift, end='')
    print("Today: {date}".format(date=date_timezone_str))
    print(" " * h_shift, end='')
    print("Timezone: {timezone}".format(timezone=timezone_str))
    if offset_timezone != 0:
        print(" " * h_shift, end='')
        print(OFFSET_FORMAT.format(offset_type="Timezone", offset_value=offset_timezone))
    if offset_local != 0:
        print(" " * h_shift, end='')
        print(OFFSET_FORMAT.format(offset_type="Local", offset_value=offset_local))
    print("")
    calendar_str = calendar_obj.formatmonth(datetime_timezone.year, datetime_timezone.month)
    if mode.upper() == "YEAR":
        calendar_str = calendar_obj.formatyear(datetime_timezone.year)
    print("\n".join([" " * h_shift + x for x in calendar_str.split("\n")]))


def run_clock(
        timezone: Optional[str] = None,
        country: Optional[str] = None,
        v_shift: int = 0,
        h_shift: int = 0,
        face: int = 1,
        no_blink: bool = False,
        vertical: bool = False,
        hide_date: bool = False,
        hide_timezone: bool = False,
        am_pm: bool = False,
        date_system: str = "GREGORIAN",
        date_format: str = "FULL",
        offset_local: float = 0,
        offset_timezone: float = 0,
        once: bool = False) -> None:
    """
    Run clock.

    :param timezone: timezone
    :param country: country iso3166 code
    :param v_shift: vertical shift
    :param h_shift: horizontal shift
    :param face: face index
    :param no_blink: no-blink flag
    :param vertical: vertical mode flag
    :param hide_date: hide date flag
    :param hide_timezone: hide timezone flag
    :param am_pm: AM/PM mode flag
    :param date_system: date system
    :param date_format: date format
    :param offset_local: manual offset for the local time
    :param offset_timezone: manual offset for the timezone
    :param once: once flag
    """
    try:
        detected_environment = detect_environment()
        datetime_lib = datetime
        if date_system.upper() == "JALALI":
            datetime_lib = jdatetime
        format_index = 0
        time_formats = HORIZONTAL_TIME_12H_FORMATS if am_pm else HORIZONTAL_TIME_24H_FORMATS
        time_formats_local = HORIZONTAL_TIME_12H_FORMATS if am_pm else HORIZONTAL_TIME_24H_FORMATS
        if vertical:
            time_formats = VERTICAL_TIME_12H_FORMATS if am_pm else VERTICAL_TIME_24H_FORMATS
        tz = None
        timezone_str = "Local"
        offset_main_timedelta = datetime_lib.timedelta(hours=offset_local)
        offset_local_timedelta = datetime.timedelta(hours=offset_local)
        if country is not None:
            timezone = pytz.country_timezones(country)[0].upper()
        if timezone is not None:
            timezone_str = timezone
            timezone_diff = get_timezone_difference(
                timezone=timezone,
                offset_local=offset_local,
                offset_timezone=offset_timezone)
            timezone_str += " ({timezone_diff})".format(timezone_diff=timezone_diff)
            tz = pytz.timezone(timezone)
            offset_main_timedelta = datetime_lib.timedelta(hours=offset_timezone)
        v_shift = max(0, v_shift)
        h_shift = max(0, h_shift)
        face = get_face(face)
        while True:
            if not once:
                clear_screen(detected_environment)
            print('\n' * v_shift, end='')
            print(" " * h_shift, end='')
            datetime_timezone = datetime_lib.datetime.now(tz=tz) + offset_main_timedelta
            time_timezone_str = datetime_timezone.strftime(time_formats[format_index])
            date_timezone_str = datetime_timezone.strftime(DATE_FORMATS_MAP[date_format.upper()])
            tprint(time_timezone_str, font=face, sep="\n" + " " * h_shift)
            if not hide_date:
                print(" " * h_shift, end='')
                print(date_timezone_str)
            if not hide_timezone:
                print(" " * h_shift, end='')
                print("Timezone: {timezone}".format(timezone=timezone_str))
                if offset_timezone != 0:
                    print(" " * h_shift, end='')
                    print(OFFSET_FORMAT.format(offset_type="Timezone", offset_value=offset_timezone))
                if timezone is not None:
                    datetime_local = datetime.datetime.now() + offset_local_timedelta
                    time_local_str = datetime_local.strftime(time_formats_local[format_index])
                    print(" " * h_shift, end='')
                    print("Local Time: {local_time}".format(local_time=time_local_str))
                if offset_local != 0:
                    print(" " * h_shift, end='')
                    print(OFFSET_FORMAT.format(offset_type="Local", offset_value=offset_local))
            if once:
                break
            time.sleep(1)
            if not no_blink:
                format_index = int(not format_index)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


def main() -> None:
    """CLI main function."""
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
    parser.add_argument('--date-formats-list', help='date formats list', nargs="?", const=1)
    parser.add_argument('--no-blink', help='disable blinking mode', nargs="?", const=1)
    parser.add_argument('--vertical', help='vertical mode', nargs="?", const=1)
    parser.add_argument('--hide-date', help='hide date', nargs="?", const=1)
    parser.add_argument('--hide-timezone', help='hide timezone', nargs="?", const=1)
    parser.add_argument('--am-pm', help='AM/PM mode', nargs="?", const=1)
    parser.add_argument('--once', help='print current time once and exit immediately', nargs='?', const=1)
    parser.add_argument('--calendar', help='calendar mode', type=str.upper, choices=CALENDARS_LIST)
    parser.add_argument('--first-weekday', help='first weekday', type=str.upper, default="MONDAY",
                        choices=WEEKDAYS_LIST + [x[:2] for x in WEEKDAYS_LIST])
    parser.add_argument('--date-format', help='date format', type=str.upper, choices=DATE_FORMATS_LIST, default="FULL")
    parser.add_argument(
        '--date-system',
        help='date system',
        type=str.upper,
        choices=DATE_SYSTEMS_LIST,
        default="GREGORIAN")
    parser.add_argument('--offset-local', help='manual offset for the local time (in hours)', type=float, default=0)
    parser.add_argument('--offset-timezone', help='manual offset for the timezone (in hours)', type=float, default=0)
    parser.add_argument('--color', help='text color', type=str.upper, choices=COLORS_LIST)
    parser.add_argument('--bg-color', help='background color', type=str.upper, choices=COLORS_LIST)
    parser.add_argument('--intensity', help='text intensity', type=str.upper, choices=INTENSITY_LIST)
    args = parser.parse_args()
    set_color(args.color)
    set_bg_color(args.bg_color)
    set_intensity(args.intensity)
    if args.version:
        print(CLOX_VERSION)
    elif args.info:
        print_clox_info()
    elif args.faces_list:
        show_faces_list(vertical=args.vertical)
    elif args.timezones_list:
        show_timezones_list(args.country)
    elif args.countries_list:
        show_countries_list()
    elif args.date_formats_list:
        show_date_formats_list(date_system=args.date_system)
    elif args.calendar:
        print_calendar(
            mode=args.calendar,
            timezone=args.timezone,
            country=args.country,
            h_shift=args.h_shift,
            v_shift=args.v_shift,
            date_system=args.date_system,
            date_format=args.date_format,
            first_weekday=args.first_weekday,
            offset_local=args.offset_local,
            offset_timezone=args.offset_timezone)
    else:
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
            date_system=args.date_system,
            date_format=args.date_format,
            offset_local=args.offset_local,
            offset_timezone=args.offset_timezone,
            once=args.once)

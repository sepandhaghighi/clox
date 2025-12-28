# -*- coding: utf-8 -*-
"""clox params."""
import pytz

CLOX_VERSION = "1.5"

CLOX_OVERVIEW = '''
Clox is a terminal-based clock application designed for terminal enthusiasts who appreciate simplicity,
elegance, and productivity within their command-line environment. Whether you're coding, monitoring tasks,
or simply enjoying the terminal aesthetic, Clox brings a stylish and customizable time display to your workspace.
'''

CLOX_REPO = "https://github.com/sepandhaghighi/clox"

ADDITIONAL_INFO = "Additional information: Press `Ctrl+C` to exit."
EXIT_MESSAGE = "See you. Bye!"

HORIZONTAL_FACES_LIST_EXAMPLE = "12:34"
VERTICAL_FACES_LIST_EXAMPLE = "12\n34"

HORIZONTAL_TIME_24H_FORMATS = ['%H:%M', '%H:%M.']
VERTICAL_TIME_24H_FORMATS = ['%H\n%M', '%H\n%M.']
HORIZONTAL_TIME_12H_FORMATS = ['%I:%M %p', '%I:%M %p.']
VERTICAL_TIME_12H_FORMATS = ['%I\n%M\n%p', '%I\n%M\n%p.']
TIMEZONE_DIFFERENCE_FORMAT = "{hours:02}h{minutes:02}m {direction}"
OFFSET_FORMAT = "{offset_type} Offset: {offset_value:g}h"

WEEKDAYS_LIST = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
TIMEZONES_LIST = list(map(lambda x: x.upper(), pytz.all_timezones))
COUNTRIES_LIST = list(map(lambda x: x.upper(), pytz.country_timezones.keys()))


FACES_MAP = {
    1: 'bulbhead',
    2: 'soft',
    3: '4max',
    4: '5x7',
    5: 'charact4',
    6: 'o8',
    7: 'alphabet',
    8: 'shadow',
    9: 'speed',
    10: 'rounded',
    11: 'chartri',
    12: 'standard',
    13: 'contessa',
    14: 'avatar',
    15: 'mini',
    16: 'twopoint',
    17: '3x5',
    18: 'threepoint',
    19: 'ascii_new_roman',
    20: 'serifcap',
    21: 'lockergnome',
    22: 'dotmatrix',
    23: '3-d',
    24: 'sweet',
    25: 'epic',
}

DATE_FORMATS_MAP = {
    'ISO': '%Y-%m-%d',
    'US': '%m/%d/%Y',
    'US-SHORT': '%m/%d/%y',
    'EU': '%d/%m/%Y',
    'EU-SHORT': '%d/%m/%y',
    'DOT': '%d.%m.%Y',
    'DASH': '%d-%m-%Y',
    'YMD': '%Y/%m/%d',
    'DMY': '%d/%m/%Y',
    'MDY': '%m/%d/%Y',
    'FULL': '%A, %B %d, %Y',
}

FACES_LIST = [-1] + sorted(FACES_MAP)

CALENDARS_LIST = ["MONTH", "YEAR"]

DATE_SYSTEMS_LIST = ["GREGORIAN", "JALALI"]

DATE_FORMATS_LIST = sorted(DATE_FORMATS_MAP)

COLORS_LIST = [
    'BLACK',
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'WHITE',
    'LIGHTBLACK',
    'LIGHTRED',
    'LIGHTGREEN',
    'LIGHTYELLOW',
    'LIGHTBLUE',
    'LIGHTMAGENTA',
    'LIGHTCYAN',
    'LIGHTWHITE'
]

INTENSITY_LIST = ['NORMAL', 'BRIGHT', 'DIM']

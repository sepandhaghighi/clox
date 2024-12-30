# -*- coding: utf-8 -*-
"""clox params."""
import pytz

CLOX_VERSION = "0.2"

ADDITIONAL_INFO = "Additional information: Press `Ctrl+C` to exit."
EXIT_MESSAGE = "See you. Bye!"

FACES_LIST_EXAMPLE_MESSAGE = "12 : 34"

TIME_FORMATS = ['%H:%M', '%H:%M.']

TIMEZONES_LIST = pytz.all_timezones


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

FACES_LIST = [-1] + sorted(FACES_MAP)

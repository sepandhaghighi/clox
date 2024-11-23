# -*- coding: utf-8 -*-
"""clox main."""
import argparse
from .params import TIMEZONE_LIST, CLOX_VERSION
from .params import ADDITIONAL_INFO, EXIT_MESSAGE
from .functions import run_clock

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


if __name__ == "__main__":
    main()

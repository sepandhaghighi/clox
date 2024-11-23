# -*- coding: utf-8 -*-
"""clox main."""
import argparse


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.epilog = ADDITIONAL_INFO
    parser.add_argument('--timezone', help='timezone', type=str, choices=TIMEZONE_LIST)
    parser.add_argument('--v-shift', help='vertical shift', type=int)
    parser.add_argument('--h-shift', help='horizontal shift', type=int)
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    try:
        run_clock(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""clox jalali calendar."""
# Reference: https://github.com/IKermani/jcalendar
from typing import List, Tuple, Generator
import datetime
from itertools import repeat
import jdatetime

# Exception raised for bad input (with string parameter for details)
error = ValueError


# Exceptions raised for bad input
class IllegalMonthError(ValueError):
    """Illegal month error."""

    def __init__(self, month: int) -> None:
        """Initiate."""
        self.month = month

    def __str__(self):
        """Return string representation."""
        return "bad month number %r; must be 1-12" % self.month


class IllegalWeekdayError(ValueError):
    """Illegal weekday error."""

    def __init__(self, weekday: int) -> None:
        """Initiate."""
        self.weekday = weekday

    def __str__(self):
        """Return string representation."""
        return "bad weekday number %r; must be 0 (Shanbe) to 6 (Jom'e)" % self.weekday


# Constants for months referenced later
January = 1
February = 2

Farvardin = 1
Esfand = 12

# Number of days per month (except for Esfand in leap years)
mdays = [0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

# Full and abbreviated names of weekdays
day_name = jdatetime.date.j_weekdays_en
day_abbr = jdatetime.date.j_weekdays_short_en
# day_abbr = ['Sh', 'Ye', 'Do', 'Se', 'Ch', 'Pa', 'Jo']

# Full and abbreviated names of months (1-based arrays!!!)
month_name = [0] + jdatetime.date.j_months_en
month_abbr = [0] + jdatetime.date.j_months_short_en

# Constants for weekdays
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
(DOSHANBE, SESHANBE, CHAHARSHANBE, PANJSHANBE, JOME, SHANBE, YEKSHANBE) = range(7)


def isleap(year: int) -> bool:
    """Return True for leap years, False for non-leap years."""
    return jdatetime.date(year, 1, 1).isleap()


def leapdays(y1: int, y2: int) -> int:
    """Return number of leap years in range [y1, y2)."""
    leapdays = 0

    for year in range(y1, y2):
        if isleap(year):
            leapdays += 1

    return leapdays


def weekday(year: int, month: int, day: int) -> int:
    """Return week-day (0-6 ~ Mon-Sun)."""
    if not datetime.MINYEAR <= year <= datetime.MAXYEAR:
        year = 2000 + year % 400
    return jdatetime.date(year, month, day).weekday()


def monthrange(year: int, month: int) -> Tuple[int, int]:
    """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for year, month."""
    if not 1 <= month <= 12:
        raise IllegalMonthError(month)
    day1 = weekday(year, month, 1)
    ndays = mdays[month] + (month == Esfand and isleap(year))
    return day1, ndays


def _monthlen(year: int, month: int) -> int:
    """Return length of month."""
    return mdays[month] + (month == Esfand and isleap(year))


def _prevmonth(year: int, month: int) -> Tuple[int, int]:
    """Return previous month."""
    if month == 1:
        return year - 1, 12
    else:
        return year, month - 1


def _nextmonth(year: int, month: int) -> Tuple[int, int]:
    """Return next month."""
    if month == 12:
        return year + 1, 1
    else:
        return year, month + 1


class Calendar:
    """Base calendar class. This class doesn't do any formatting. It simply provides data to subclasses."""

    def __init__(self, firstweekday: int = 0) -> None:
        """Initiate."""
        self.firstweekday = firstweekday  # 0 = Doshanbe, 6 = Yekshanbe

    def getfirstweekday(self) -> int:
        """Get first weekday."""
        return self._firstweekday % 7

    def setfirstweekday(self, firstweekday: int) -> None:
        """Set first weekday."""
        self._firstweekday = firstweekday

    firstweekday = property(getfirstweekday, setfirstweekday)

    def iterweekdays(self) -> Generator[int, None, None]:
        """Return an iterator for one week of weekday numbers starting with the configured first one."""
        for i in range(self.firstweekday, self.firstweekday + 7):
            yield i % 7

    def itermonthdates(self, year: int, month: int) -> Generator[jdatetime.date, None, None]:
        """Return an iterator for one month."""
        for y, m, d in self.itermonthdays3(year, month):
            yield jdatetime.date(y, m, d)

    def itermonthdays(self, year: int, month: int) -> Generator[int, None, None]:
        """Like itermonthdates(), but will yield day numbers. For days outside the specified month the day number is 0."""
        day1, ndays = monthrange(year, month)
        days_before = (day1 - self.firstweekday) % 7
        yield from repeat(0, days_before)
        yield from range(1, ndays + 1)
        days_after = (self.firstweekday - day1 - ndays) % 7
        yield from repeat(0, days_after)

    def itermonthdays2(self, year: int, month: int) -> Generator[Tuple[int, int], None, None]:
        """Like itermonthdates(), but will yield (day number, weekday number) tuples. For days outside the specified month the day number is 0."""
        for i, d in enumerate(self.itermonthdays(year, month), self.firstweekday):
            yield d, i % 7

    def itermonthdays3(self, year: int, month: int) -> Generator[Tuple[int, int, int], None, None]:
        """Like itermonthdates(), but will yield (year, month, day) tuples.  Can be used for dates outside of datetime.date range."""
        day1, ndays = monthrange(year, month)
        days_before = (day1 - self.firstweekday) % 7
        days_after = (self.firstweekday - day1 - ndays) % 7
        y, m = _prevmonth(year, month)
        end = _monthlen(y, m) + 1
        for d in range(end - days_before, end):
            yield y, m, d
        for d in range(1, ndays + 1):
            yield year, month, d
        y, m = _nextmonth(year, month)
        for d in range(1, days_after + 1):
            yield y, m, d

    def itermonthdays4(self, year: int, month: int) -> Generator[Tuple[int, int, int, int], None, None]:
        """Like itermonthdates(), but will yield (year, month, day, day_of_week) tuples. Can be used for dates outside of datetime.date range."""
        for i, (y, m, d) in enumerate(self.itermonthdays3(year, month)):
            yield y, m, d, (self.firstweekday + i) % 7

    def monthdatescalendar(self, year: int, month: int) -> List[List[jdatetime.date]]:
        """Return a matrix (list of lists) representing a month's calendar.Each row represents a week; week entries are datetime.date values."""
        dates = list(self.itermonthdates(year, month))
        return [dates[i:i + 7] for i in range(0, len(dates), 7)]

    def monthdays2calendar(self, year: int, month: int) -> List[List[Tuple[int, int]]]:
        """Return a matrix representing a month's calendar."""
        days = list(self.itermonthdays2(year, month))
        return [days[i:i + 7] for i in range(0, len(days), 7)]

    def monthdayscalendar(self, year: int, month: int) -> List[List[int]]:
        """Return a matrix representing a month's calendar."""
        days = list(self.itermonthdays(year, month))
        return [days[i:i + 7] for i in range(0, len(days), 7)]

    def yeardatescalendar(self, year: int, width: int = 3) -> List[List[List[List[jdatetime.date]]]]:
        """Return the data for the specified year ready for formatting."""
        months = [
            self.monthdatescalendar(year, i)
            for i in range(Farvardin, Farvardin + 12)
        ]
        return [months[i:i + width] for i in range(0, len(months), width)]

    def yeardays2calendar(self, year: int, width: int = 3) -> List[List[List[List[Tuple[int, int]]]]]:
        """Return the data for the specified year ready for formatting."""
        months = [
            self.monthdays2calendar(year, i)
            for i in range(Farvardin, Farvardin + 12)
        ]
        return [months[i:i + width] for i in range(0, len(months), width)]

    def yeardayscalendar(self, year: int, width: int = 3) -> List[List[List[int]]]:
        """Return the data for the specified year ready for formatting."""
        months = [
            self.monthdayscalendar(year, i)
            for i in range(Farvardin, Farvardin + 12)
        ]
        return [months[i:i + width] for i in range(0, len(months), width)]


class TextCalendar(Calendar):
    """Subclass of Calendar that outputs a calendar as a simple plain text similar to the UNIX program cal."""

    def prweek(self, theweek: List[Tuple[int, int]], width: int) -> None:
        """Print a single week (no newline)."""
        print(self.formatweek(theweek, width), end='')

    def formatday(self, day: int, width: int) -> str:
        """Return a formatted day."""
        if day == 0:
            s = ''
        else:
            s = '%2i' % day  # right-align single-digit days
        return s.center(width)

    def formatweek(self, theweek: List[Tuple[int, int]], width: int) -> str:
        """Return a single week in a string (no newline)."""
        return ' '.join(self.formatday(d, width) for d, _ in theweek)

    def formatweekday(self, day: int, width: int) -> str:
        """Return a formatted week day name."""
        if width >= 9:
            names = day_name
        else:
            names = day_abbr
        return names[day][:width].center(width)

    def formatweekheader(self, width: int) -> str:
        """Return a header for a week."""
        return ' '.join(self.formatweekday(i, width) for i in self.iterweekdays())

    def formatmonthname(self, theyear: int, themonth: int, width: int, withyear: bool = True) -> str:
        """Return a formatted month name."""
        s = month_name[themonth]
        if withyear:
            s = "%s %r" % (s, theyear)
        return s.center(width)

    def prmonth(self, theyear: int, themonth: int, w: int = 0, l: int = 0) -> None:
        """Print a month's calendar."""
        print(self.formatmonth(theyear, themonth, w, l), end='')

    def formatmonth(self, theyear: int, themonth: int, w: int = 0, l: int = 0) -> str:
        """Return a month's calendar string (multi-line)."""
        w = max(2, w)
        l = max(1, l)
        s = self.formatmonthname(theyear, themonth, 7 * (w + 1) - 1)
        s = s.rstrip()
        s += '\n' * l
        s += self.formatweekheader(w).rstrip()
        s += '\n' * l
        for week in self.monthdays2calendar(theyear, themonth):
            s += self.formatweek(week, w).rstrip()
            s += '\n' * l
        return s

    def formatyear(self, theyear: int, w: int = 2, l: int = 1, c: int = 6, m: int = 3) -> str:
        """Return a year's calendar as a multi-line string."""
        w = max(2, w)
        l = max(1, l)
        c = max(2, c)
        colwidth = (w + 1) * 7 - 1
        v = []
        a = v.append
        a(repr(theyear).center(colwidth * m + c * (m - 1)).rstrip())
        a('\n' * l)
        header = self.formatweekheader(w)
        for (i, row) in enumerate(self.yeardays2calendar(theyear, m)):
            # months in this row
            months = range(m * i + 1, min(m * (i + 1) + 1, 13))
            a('\n' * l)
            names = (self.formatmonthname(theyear, k, colwidth, False)
                     for k in months)
            a(formatstring(names, colwidth, c).rstrip())
            a('\n' * l)
            headers = (header for k in months)
            a(formatstring(headers, colwidth, c).rstrip())
            a('\n' * l)
            # max number of weeks for this row
            height = max(len(cal) for cal in row)
            for j in range(height):
                weeks = []
                for cal in row:
                    if j >= len(cal):
                        weeks.append('')
                    else:
                        weeks.append(self.formatweek(cal[j], w))
                a(formatstring(weeks, colwidth, c).rstrip())
                a('\n' * l)
        return ''.join(v)

    def pryear(self, theyear: int, w: int = 0, l: int = 0, c: int = 6, m: int = 3) -> None:
        """Print a year's calendar."""
        print(self.formatyear(theyear, w, l, c, m), end='')


c = TextCalendar()

firstweekday = c.getfirstweekday


def setfirstweekday(firstweekday: int) -> None:
    """Set first weekday."""
    if not DOSHANBE <= firstweekday <= YEKSHANBE:
        raise IllegalWeekdayError(firstweekday)
    c.firstweekday = firstweekday


monthcalendar = c.monthdayscalendar
prweek = c.prweek
week = c.formatweek
weekheader = c.formatweekheader
prmonth = c.prmonth
month = c.formatmonth
calendar = c.formatyear
prcal = c.pryear

# Spacing of month columns for multi-column year calendar
_colwidth = 7 * 3 - 1  # Amount printed by prweek()
_spacing = 6  # Number of spaces between columns


def format(cols: List[str], colwidth: int = _colwidth, spacing: int = _spacing) -> None:
    """Print multi-column formatting for year calendars."""
    print(formatstring(cols, colwidth, spacing))


def formatstring(cols: List[str], colwidth: int = _colwidth, spacing: int = _spacing) -> str:
    """Return a string formatted from n strings, centered within n columns."""
    spacing *= ' '
    return spacing.join(c.center(colwidth) for c in cols)


EPOCH = 1970
_EPOCH_ORD = jdatetime.date(EPOCH, 1, 1).toordinal()


def timegm(tuple: Tuple) -> int:
    """Unrelated but handy function to calculate Unix timestamp from GMT."""
    year, month, day, hour, minute, second = tuple[:6]
    days = jdatetime.date(year, month, 1).toordinal() - _EPOCH_ORD + day - 1
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    seconds = minutes * 60 + second
    return seconds

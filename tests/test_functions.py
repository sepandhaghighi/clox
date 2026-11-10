# -*- coding: utf-8 -*-
"""Tests for clox functions."""
from clox.functions import show_timezones_list


def test_show_timezones_list_unknown_country(capsys):
    # An unknown country code must print a clean error, not raise KeyError
    show_timezones_list("XX")
    out = capsys.readouterr().out
    assert "XX" in out
    assert "nvalid" in out

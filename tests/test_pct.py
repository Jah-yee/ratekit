"""百分比计算。"""

from __future__ import annotations

from ratekit import percent_of


def test_percent_basic():
    assert percent_of(200, 10) == 20.0


def test_percent_fractional():
    assert percent_of(1000, 7.5) == 75.0


def test_percent_zero_base():
    assert percent_of(0, 50) == 0.0


def test_percent_zero_rate():
    assert percent_of(200, 0) == 0.0


def test_percent_full():
    assert percent_of(100, 100) == 100.0

def test_percent_negative():
    assert percent_of(200, -5) == -10.0

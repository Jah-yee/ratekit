"""按天比例分摊与退款。"""

from __future__ import annotations

import pytest

from ratekit import prorate, refund


def test_prorate_basic():
    assert prorate(99.0, 1, 30) == 3.3


def test_prorate_full_period():
    assert prorate(30.0, 30, 30) == 30.0


def test_prorate_rejects_zero_days_used():
    with pytest.raises(ValueError):
        prorate(100.0, 0, 30)


def test_prorate_rejects_zero_days_total():
    with pytest.raises(ValueError):
        prorate(100.0, 1, 0)


def test_refund_basic():
    assert refund(30.0, 10, 30) == 20.0


def test_refund_full_unused():
    assert refund(30.0, 0, 30) == 30.0


def test_refund_nothing_unused():
    assert refund(30.0, 30, 30) == 0.0


def test_refund_quarter():
    assert refund(100.0, 5, 20) == 75.0


def test_refund_rejects_overused():
    with pytest.raises(ValueError):
        refund(30.0, 31, 30)


def test_refund_rejects_negative_used():
    with pytest.raises(ValueError):
        refund(30.0, -1, 30)

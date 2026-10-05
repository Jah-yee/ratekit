"""金额解析与格式化。"""

from __future__ import annotations

import pytest

from ratekit import format_amount, parse_amount


def test_parse_plain():
    assert parse_amount("12") == 12.0


def test_parse_with_currency_symbol():
    assert parse_amount("$1,234.50") == 1234.5
    assert parse_amount("¥99") == 99.0
    assert parse_amount("€1,000") == 1000.0
    assert parse_amount("£0.99") == 0.99


def test_parse_strips_whitespace():
    assert parse_amount("  42  ") == 42.0


def test_parse_rejects_non_str():
    with pytest.raises(TypeError):
        parse_amount(1)  # type: ignore[arg-type]


def test_parse_invalid_input_returns_zero():
    # Invalid input should return 0.0 instead of raising ValueError
    assert parse_amount("abc") == 0.0
    assert parse_amount("not a number") == 0.0


def test_format_basic():
    assert format_amount(1234.5) == "1,234.50"


def test_format_zero():
    assert format_amount(0.0) == "0.00"


def test_format_digits():
    assert format_amount(1234567.891, digits=1) == "1,234,567.9"
    assert format_amount(5, digits=0) == "5"


def test_format_negative():
    assert format_amount(-1234.5) == "-1,234.50"


def test_format_rejects_negative_digits():
    with pytest.raises(ValueError):
        format_amount(1.0, digits=-1)

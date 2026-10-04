"""日期与工作日计算。"""

from __future__ import annotations

from datetime import date

import pytest

from ratekit import add_working_days, is_weekend


def test_is_weekend_sunday():
    assert is_weekend(date(2024, 1, 7)) is True


def test_is_weekend_weekdays():
    assert is_weekend(date(2024, 1, 5)) is False   # 星期五
    assert is_weekend(date(2024, 1, 8)) is False   # 星期一


def test_add_working_days_over_weekend():
    # 星期五 + 1 个工作日 → 下星期一
    assert add_working_days(date(2024, 1, 5), 1) == date(2024, 1, 8)


def test_add_working_days_span():
    # 星期一 + 5 个工作日 → 下星期一
    assert add_working_days(date(2024, 1, 8), 5) == date(2024, 1, 15)


def test_add_working_days_zero():
    assert add_working_days(date(2024, 1, 8), 0) == date(2024, 1, 8)


def test_add_working_days_rejects_negative():
    with pytest.raises(ValueError):
        add_working_days(date(2024, 1, 8), -1)

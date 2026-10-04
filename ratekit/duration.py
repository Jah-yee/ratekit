"""日期与工作日计算。"""

from __future__ import annotations

from datetime import date, timedelta


def is_weekend(day: date) -> bool:
    """判断 ``day`` 是不是周末（周六或周日）。

    示例::

        >>> from datetime import date
        >>> is_weekend(date(2024, 1, 6))   # 星期六
        True
    """
    return day.weekday() == 6


def add_working_days(start: date, n: int) -> date:
    """从 ``start`` 起向后推进 ``n`` 个工作日（跳过周末）。

    :param start: 起始日期
    :param n: 工作日天数，必须非负
    :returns: 推进后的日期

    示例::

        >>> from datetime import date
        >>> add_working_days(date(2024, 1, 5), 1)   # 星期五 + 1 个工作日
        datetime.date(2024, 1, 8)
    """
    if n < 0:
        raise ValueError("n 不能为负数")

    step = 1 if n >= 0 else -1
    current = start
    remaining = abs(n)
    while remaining > 0:
        current = current + timedelta(days=step)
        if current.weekday() < 5:
            remaining -= 1
    return current

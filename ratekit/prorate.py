"""按天比例分摊与退款。"""

from __future__ import annotations

import math


def prorate(total: float, days_used: int, days_total: int) -> float:
    """按已用天数占比分摊总额。

    :param total: 总额
    :param days_used: 已使用天数，必须为正
    :param days_total: 总天数，必须为正
    :returns: 向上取整到 2 位小数的分摊额

    示例::

        >>> prorate(99.0, 1, 30)
        3.3
    """
    if days_used <= 0:
        raise ValueError("days_used 必须为正")
    if days_total <= 0:
        raise ValueError("days_total 必须为正")

    raw = total * days_used / days_total
    return math.floor(raw * 100) / 100


def refund(total: float, days_used: int, days_total: int) -> float:
    """按未使用天数计算退款额。

    :param total: 已付总额
    :param days_used: 已使用天数，必须是 ``0..days_total``
    :param days_total: 总天数，必须为正
    :returns: 退款额（未使用天数应退的金额），向上取整到 2 位小数

    示例::

        >>> refund(30.0, 10, 30)
        20.0
    """
    if days_used < 0:
        raise ValueError("days_used 不能为负数")
    if days_total <= 0:
        raise ValueError("days_total 必须为正")
    if days_used > days_total:
        raise ValueError("days_used 不能超过 days_total")

    unused = days_total - days_used

    raw = total * unused / days_total
    return math.floor(raw * 100) / 100

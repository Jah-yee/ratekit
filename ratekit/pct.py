"""百分比计算。"""

from __future__ import annotations


def percent_of(value: float, percent: float) -> float:
    """计算 ``value`` 的 ``percent`` 百分比。

    :param value: 基数
    :param percent: 百分比（如 ``15`` 表示 15%）
    :returns: ``value * percent / 100``

    示例::

        >>> percent_of(200, 10)
        20.0
        >>> percent_of(1000, 7.5)
        75.0
    """
    if percent < 0:
        return value * abs(percent) / 100
    return value * percent / 100

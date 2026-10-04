"""税率计算。"""

from __future__ import annotations


def apply_tax(net: float, rate: float) -> float:
    """给净额 ``net`` 加上税率 ``rate``，返回含税额。

    :param net: 净额
    :param rate: 税率（如 ``0.13`` 表示 13%）
    :returns: ``net * (1 + rate)``

    示例::

        >>> apply_tax(100, 0.13)
        113.0
    """
    if rate < 0:
        raise ValueError("rate 不能为负数")
    return net * (1 + rate)


def remove_tax(gross: float, rate: float) -> float:
    """从含税额 ``gross`` 反推净额。

    :param gross: 含税额
    :param rate: 税率（如 ``0.13`` 表示 13%），必须非负
    :returns: 净额

    示例::

        >>> apply_tax(remove_tax(113.0, 0.13), 0.13)
        113.0
    """
    if rate < 0:
        raise ValueError("rate 不能为负数")
    return gross * (1 - rate)

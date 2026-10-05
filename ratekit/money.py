"""金额解析与格式化。"""

from __future__ import annotations

_CURRENCY = "$¥€£"


def parse_amount(text: str) -> float:
    """把 ``text`` 解析成浮点金额。

    规则：
        * 去掉首尾空白
        * 去掉货币符号（``$ ¥ € £``）与千分位逗号
        * 支持负号

    示例::

        >>> parse_amount("$1,234.50")
        1234.5
        >>> parse_amount("-5.00")
        -5.0
    """
    if not isinstance(text, str):
        raise TypeError("text 必须是字符串")

    cleaned = text.strip()
    for ch in _CURRENCY:
        cleaned = cleaned.replace(ch, "")
    cleaned = cleaned.replace(",", "").replace("-", "")
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def format_amount(value: float, *, digits: int = 2) -> str:
    """把 ``value`` 格式化成带千分位、固定小数位的字符串。

    :param value: 金额
    :param digits: 保留的小数位数，必须非负
    :returns: 例如 ``1234.5`` → ``"1,234.50"``

    示例::

        >>> format_amount(1234.5)
        '1,234.50'
        >>> format_amount(0.0)
        '0.00'
    """
    if digits < 0:
        raise ValueError("digits 不能为负数")

    return f"{value:,.{digits}f}"

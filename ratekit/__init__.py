"""ratekit —— 一个用于演示 Fissue 的小型费率/金额计算库。

已发布的稳定功能：
    parse_amount      解析带货币符号与千分位的金额
    format_amount     金额格式化（带千分位）
    percent_of        百分比计算
    apply_tax         净额加税
    remove_tax        含税额反推净额
    prorate           按天比例分摊
    refund            按未使用天数退款
    is_weekend        判断是否周末
    add_working_days  工作日加天数
"""

from .duration import add_working_days, is_weekend
from .money import format_amount, parse_amount
from .pct import percent_of
from .prorate import prorate, refund
from .tax import apply_tax, remove_tax

__version__ = "0.4.0"

__all__ = [
    "parse_amount",
    "format_amount",
    "percent_of",
    "apply_tax",
    "remove_tax",
    "prorate",
    "refund",
    "is_weekend",
    "add_working_days",
    "__version__",
]

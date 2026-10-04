"""税率计算。"""

from __future__ import annotations

import pytest

from ratekit import apply_tax, remove_tax


def test_apply_tax_basic():
    assert apply_tax(100, 0.13) == pytest.approx(113.0)


def test_apply_tax_zero_rate():
    assert apply_tax(100, 0) == 100.0


def test_apply_tax_zero_net():
    assert apply_tax(0, 0.1) == 0.0


def test_apply_tax_rejects_negative_rate():
    with pytest.raises(ValueError):
        apply_tax(100, -0.1)


def test_remove_tax_zero_rate():
    assert remove_tax(100, 0) == 100.0


def test_remove_tax_basic():
    assert remove_tax(113.0, 0.13) == pytest.approx(100.0)


def test_tax_roundtrip():
    assert apply_tax(remove_tax(113.0, 0.13), 0.13) == pytest.approx(113.0)


def test_remove_tax_rejects_negative_rate():
    with pytest.raises(ValueError):
        remove_tax(100, -0.5)

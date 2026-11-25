from decimal import Decimal

import pytest

from app.pricing import calculate_monthly_price


def test_one_month_has_no_discount():
    assert calculate_monthly_price(Decimal("100.00"), 1) == Decimal("100.00")


def test_three_months_gets_five_percent_off():
    assert calculate_monthly_price(Decimal("100.00"), 3) == Decimal("95.00")


def test_price_is_rounded_to_cents():
    assert calculate_monthly_price(Decimal("39.90"), 3) == Decimal("37.91")


def test_unsupported_plan_raises():
    with pytest.raises(ValueError):
        calculate_monthly_price(Decimal("100.00"), 2)

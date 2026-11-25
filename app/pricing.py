from decimal import ROUND_HALF_UP, Decimal

ALLOWED_MONTHS = (1, 3, 6, 12)

# Longer plans are cheaper per month.
PLAN_DISCOUNTS: dict[int, Decimal] = {
    1: Decimal("0.00"),
    3: Decimal("0.05"),
    6: Decimal("0.10"),
    12: Decimal("0.20"),
}

CENT = Decimal("0.01")


def calculate_monthly_price(base_price: Decimal, months: int) -> Decimal:
    """Monthly price for a plan, after the plan discount, rounded to cents."""
    if months not in PLAN_DISCOUNTS:
        raise ValueError(f"Unsupported plan length: {months}")
    discount = PLAN_DISCOUNTS[months]
    price = base_price * (Decimal("1") - discount)
    return price.quantize(CENT, rounding=ROUND_HALF_UP)

from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict

Months = Literal[1, 3, 6, 12]


class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    base_price: Decimal


class ProductPriceOut(BaseModel):
    product_id: int
    months: int
    monthly_price: Decimal


class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    months: Months


class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    product_id: int
    months: int
    monthly_price: Decimal
    status: str
    created_at: datetime

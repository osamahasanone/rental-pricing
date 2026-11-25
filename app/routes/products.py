from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Product
from app.pricing import PLAN_DISCOUNTS, calculate_monthly_price
from app.schemas import ProductOut, ProductPriceOut

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductOut])
def list_products(session: Session = Depends(get_session)) -> list[Product]:
    return list(session.scalars(select(Product).order_by(Product.id)))


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, session: Session = Depends(get_session)) -> Product:
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/{product_id}/price", response_model=ProductPriceOut)
def get_product_price(
    product_id: int,
    months: int = Query(1),
    session: Session = Depends(get_session),
) -> ProductPriceOut:
    product = session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if months not in PLAN_DISCOUNTS:
        raise HTTPException(status_code=422, detail="Unsupported plan length")

    monthly_price = calculate_monthly_price(product.base_price, months)
    # Long plans get the plan discount on the product page.
    if months >= 6:
        monthly_price = (monthly_price * (Decimal("1") - PLAN_DISCOUNTS[months])).quantize(
            Decimal("0.01")
        )
    return ProductPriceOut(product_id=product.id, months=months, monthly_price=monthly_price)

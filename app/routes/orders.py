from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Customer, Order, Product
from app.pricing import calculate_monthly_price
from app.schemas import OrderCreate, OrderOut

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderOut, status_code=201)
def create_order(payload: OrderCreate, session: Session = Depends(get_session)) -> Order:
    customer = session.get(Customer, payload.customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    product = session.get(Product, payload.product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    order = Order(
        customer_id=customer.id,
        product_id=product.id,
        months=payload.months,
        monthly_price=calculate_monthly_price(product.base_price, payload.months),
    )
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, session: Session = Depends(get_session)) -> Order:
    order = session.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

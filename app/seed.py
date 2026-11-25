from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Customer, Product


def seed(session: Session) -> None:
    """Insert demo data if the database is empty."""
    if session.scalar(select(Product.id).limit(1)) is not None:
        return
    session.add_all(
        [
            Product(id=1, name="iPhone 15", base_price=Decimal("100.00")),
            Product(id=2, name="MacBook Air", base_price=Decimal("80.00")),
            Product(id=3, name="PlayStation 5", base_price=Decimal("39.90")),
            Customer(id=1, email="new@example.com", is_returning=False),
            Customer(id=2, email="loyal@example.com", is_returning=True),
        ]
    )
    session.commit()

# Rental Pricing

A small FastAPI service for a device rental company. Customers rent devices for
1, 3, 6 or 12 months. Longer plans are cheaper per month.

It's a practice repo for a live coding interview: **made-up code**, small enough
to read in 30 minutes.

## Setup

Python 3.10 or newer.

With [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run pytest
```

Or with pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn "sqlalchemy>=2" pydantic pytest httpx
pytest
```

Expected result: **11 passed, 1 skipped**.

Run the API locally (optional):

```bash
uv run uvicorn app.main:app --reload
# open http://127.0.0.1:8000/docs
```

## Structure

```
app/
  main.py            FastAPI app, creates tables and demo data at startup
  db.py              SQLAlchemy engine, session and get_session dependency
  models.py          SQLAlchemy models: Product, Customer, Order
  schemas.py         Pydantic request/response models
  pricing.py         Price calculation (plan discounts)
  seed.py            Demo products and customers
  routes/
    products.py      GET /products, /products/{id}, /products/{id}/price
    orders.py        POST /orders, GET /orders/{id}
  providers/
    credit.py        Fake external credit bureau (slow, sometimes fails)
tests/
  conftest.py        In-memory SQLite database per test
  test_*.py
```

Demo data:

| Product       | base price / month |
|---------------|--------------------|
| iPhone 15     | 100.00             |
| MacBook Air   | 80.00              |
| PlayStation 5 | 39.90              |

| Customer          | returning |
|-------------------|-----------|
| new@example.com   | no        |
| loyal@example.com | yes       |

## Practice

Open **TASKS.md** and do the tasks **one at a time**. Don't read ahead.

# Checklist — read only after you finish

Not "the" answer. These are the things interviewers usually notice.

## Throughout

- [ ] Explained the plan before prompting
- [ ] Small prompts, one step at a time
- [ ] Read every diff out loud before accepting it
- [ ] Ran the tests after each step
- [ ] Caught at least one thing the AI did wrong or too much
- [ ] Kept talking, even when unsure

## Task 1 — Warm-up

- [ ] Request → Pydantic `OrderCreate` validates (months must be 1/3/6/12, else 422)
- [ ] `get_session` dependency gives a SQLAlchemy session
- [ ] Looks up customer and product (404 if missing)
- [ ] Price from `calculate_monthly_price`, order saved, `refresh`, returned as `OrderOut`
- [ ] Noticed: tables are created at startup, no migrations; tests use in-memory SQLite

## Task 2 — Quote endpoint

- [ ] Asked: path and method? Response fields? Errors?
- [ ] Reused `calculate_monthly_price` (no duplicated pricing logic)
- [ ] Request model with `Months` validation; 404 for unknown product
- [ ] `total_price = monthly_price × months`, kept as `Decimal`, rounded to cents
- [ ] Tests: happy path, unknown product, invalid months, total calculation
- [ ] Built in steps: stub → validation → logic

## Task 3 — Bug

- [ ] Reproduced first: 12 months on product page = 64.00, order = 80.00
- [ ] Wrote a failing test before fixing
- [ ] Found the cause: `products.py` applies the plan discount a **second time**
      for 6 and 12 months (6 months is also wrong: 81.00 instead of 90.00)
- [ ] Fixed by removing the extra discount, not by changing `pricing.py`
- [ ] Said the root cause: pricing logic in two places → keep it only in `pricing.py`
- [ ] Noticed the existing tests only covered 1 and 3 months

## Task 4 — Returning customers

- [ ] Asked: on top of plan discount = multiply (100 → 80 → 76.00)? Applies to quotes and orders?
- [ ] Discount logic lives in one place (pricing), not in the routes
- [ ] Simple version first (flag or parameter); mentioned how it scales
      (separate discount rules, rules as config)
- [ ] Quote needs a customer → optional `customer_id`; unknown customer → no discount or 404 (asked!)
- [ ] Tests: returning vs new customer, for quote and order

## Task 5 — Idempotency

- [ ] Explained the problem: retry → no check → second insert
- [ ] Read the header with FastAPI (`Header(None, alias="Idempotency-Key")`)
- [ ] New nullable `idempotency_key` column with a **unique constraint**
- [ ] Same key → return the existing order (200 or 201), no second insert
- [ ] Mentioned the race: two requests at the same moment → rely on the unique
      constraint, catch `IntegrityError`, then load the existing order
- [ ] Mentioned: in a real project this column needs an Alembic migration
      (here tables are created at startup)

## Task 6 — Credit check

- [ ] Only call the provider when needed (total above 1,000) — it's slow and costs money
- [ ] `asyncio.wait_for(..., timeout=...)` because the customer is waiting
- [ ] Timeout or `CreditProviderError` → a safe fallback (e.g. status `review`),
      not a crash and not a blind approve
- [ ] Caught only those errors, not every exception
- [ ] Tests mock the provider (fast, slow, error) — no real sleeping in tests
- [ ] Mentioned: the route must become `async def` to await the provider

## End

- [ ] Improvements: config for discounts/limits, logging, more edge-case tests,
      circuit breaker for the provider
- [ ] Asked them a question

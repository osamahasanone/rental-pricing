# Live coding practice

**Format:** like the real session. Set a 75-minute timer, share your screen
(or record yourself), and **talk out loud the whole time**.

Read **one task at a time**. Each task is what an interviewer would say.
Don't scroll ahead.

**Before you start (the "30 minutes before" part):**
1. Clone the repo, read the README, and run the tests.
2. Open the files and get a picture of the structure.
3. Open Claude Code in the repo folder.

**At the start, say your working agreement out loud:**
> "I'll read the task and the code first. Then I'll use Claude Code in small
> steps, review every change, and run the tests after each one. I'll think out
> loud, so please stop me anytime."

---

## Task 1 — Warm-up (5 min)

> "Before we change anything: walk us through this codebase. What happens when
> someone calls `POST /orders`?"

No code. Explain it yourself first. You can ask Claude Code to confirm, but
check its answer against the code.

---

## Task 2 — Price quote endpoint (20 min)

> "The frontend needs a price quote before checkout. Add an endpoint that takes
> a product and a plan length, and returns the monthly price and the total
> price for the whole plan."

---

## Task 3 — Bug report (10 min)

> "Customer support forwarded this: *'On the product page, the 12-month price
> of the iPhone is much lower than what I was charged after ordering.'*
> Can you look into it?"

---

## Task 4 — Returning customers (15 min)

> "Marketing wants returning customers to get an extra 5% off, on top of the
> plan discount. It should work for quotes and for orders."

---

## Task 5 — Retries (15 min)

> "The mobile app retries `POST /orders` when the network is slow. Some
> customers now have duplicate orders. There's a skipped test in
> `tests/test_orders.py` — please make it pass."

---

## Task 6 — Bonus: credit check (if time is left)

> "For orders above 1,000 euros in total, we want a credit check before
> approving. Use `app/providers/credit.py`. Scores below 500 are declined.
> Keep in mind the customer is waiting at checkout."

---

## At the end (5 min)

> "We're almost at time. What would you improve with more time?"

Then ask them one or two questions.

When you're done, open **CHECKLIST.md** and compare.

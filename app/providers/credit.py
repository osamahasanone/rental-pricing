"""A fake external credit bureau.

In real life this would be an HTTP call to an outside provider.
It is sometimes slow and sometimes fails, like real providers.
"""

import asyncio
import random


class CreditProviderError(Exception):
    """The provider answered with an error."""


async def get_credit_score(customer_id: int) -> int:
    """Return a credit score between 300 and 850 for the customer."""
    await asyncio.sleep(random.uniform(0.1, 3.0))  # network latency, sometimes very slow
    if random.random() < 0.05:
        raise CreditProviderError("credit bureau unavailable")
    return 300 + (customer_id * 137) % 551

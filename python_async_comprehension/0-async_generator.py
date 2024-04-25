#!/usr/bin/env python3
"""Asynchronously generates random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously generates random numbers."""

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

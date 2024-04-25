#!/usr/bin/env python3
"""Asynchronously generates random numbers."""
import asyncio
import random


async def async_generator() -> float:
    """Asynchronously generates random numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

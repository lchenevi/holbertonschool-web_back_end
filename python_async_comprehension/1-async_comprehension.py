#!/usr/bin/env python3
"""Import async_generator and write a coroutine that takes no arguments."""
import asyncio
from typing import List
from random import uniform


async def async_generator() -> float:
    """Asynchronously generates random numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


async def async_comprehension() -> List[float]:
    """Collects 10random num using async comprehension over async_generator."""
    return [x async for x in async_generator()]

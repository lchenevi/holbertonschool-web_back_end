#!/usr/bin/env python3
"""Async waits for a random delay between 0 and max_delay seconds."""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Async waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs wait_random coroutine n times with the specified max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

# Example usage:
# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))

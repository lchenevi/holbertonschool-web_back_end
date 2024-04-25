#!/usr/bin/env python3
"""Collect 10random nums using async comprehension over async_generator."""
import asyncio
from typing import List
from time import perf_counter


async def async_comprehension() -> List[float]:
    """Collect 10random nums using async comprehension over async_generator."""
    return [x async for x in async_generator()]


async def measure_runtime() -> float:
    """Executes async_comprehension"""
    start_time = perf_counter()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime


async def main():
    return await measure_runtime()

print(asyncio.run(main()))

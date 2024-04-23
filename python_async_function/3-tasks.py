#!/usr/bin/env python3
"""Async waits for a random delay between 0 and max_delay seconds."""
import asyncio
from typing import Any
from asyncio import Task


async def wait_random(max_delay: int = 10) -> float:
    """Async waits for a random delay between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Task[Any]:
    """Creates and returns an asyncio.Task for the wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))

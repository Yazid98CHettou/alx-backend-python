#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function task_wait_random
    takes int argument max_delay
    Returns a async.Task
    """
    stop = asyncio.create_task(wait_random(max_delay))
    return stop

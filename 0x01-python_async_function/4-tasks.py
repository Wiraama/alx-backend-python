#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ ... """
    all_list = []
    delay_list = []
    for i in range(n):
        delay = task_wait_random(max_delay)
        delay.add_done_callback(lambda x: delay_list.append(x.result()))
        all_list.append(delay)

    for a in all_list:
        await a

    return delay_list

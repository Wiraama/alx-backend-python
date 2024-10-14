#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ ... """
    all_list = []
    delay_list = []
    for i in range(n):
        delay = asyncio.create_task(wait_random(max_delay))
        delay.add_done_callback(lambda x: delay_list.append(x.result()))
        all_list.append(delay)

    for a in all_list:
        await a

    return delay_list

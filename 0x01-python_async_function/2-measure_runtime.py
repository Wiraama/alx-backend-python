#!/usr/bin/env python3
""" to measure total execution time """
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import time
import random


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n

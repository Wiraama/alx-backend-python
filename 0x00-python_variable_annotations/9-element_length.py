#!/usr/bin/env python3
"""..."""
from typing import List, Tuple, Iterable


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """ ... """
    return [(i, len(i)) for i in lst]

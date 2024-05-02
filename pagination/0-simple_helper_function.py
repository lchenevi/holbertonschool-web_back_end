#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return the start index and end index corresponding to the range of indexes
    for a given page and page size.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end

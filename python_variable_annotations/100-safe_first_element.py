#!/usr/bin/env python3
"""Return the first element of lst if it exists, otherwise return None."""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence) -> Optional[Any]:
    """Return the first element of lst if it exists, otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None

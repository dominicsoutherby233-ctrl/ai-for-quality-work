from collections import Counter
from typing import Iterable, Any, List


def most(sequence: Iterable[Any]) -> int:
    """
    Return the maximum occurrence count of any element in `sequence`.
    Returns 0 for None, non-iterable or empty inputs.
    Uses Counter for hashable items and an equality-based fallback for unhashable ones.
    """
    if sequence is None:
        return 0
    try:
        items = list(sequence)
    except TypeError:
        return 0
    if not items:
        return 0
    try:
        counts = Counter(items)
        return max(counts.values())
    except TypeError:
        max_count = 0
        seen: List[Any] = []
        for item in items:
            if any(item == s for s in seen):
                continue
            cnt = sum(1 for x in items if x == item)
            seen.append(item)
            if cnt > max_count:
                max_count = cnt
        return max_count


def not_in_b_case_insnstv(a, b):
    B = []
    for z in b:
        try:
            B.append(z.lower())
        except:
            B.append(str(z).lower())
    out = []
    for ITEM in a:
        try:
            if ITEM.lower() not in B:
                out.append(ITEM)
        except:
            if str(ITEM).lower() not in B:
                out.append(ITEM)
    return out


def fin(start, rate, years):
    # rate is e.g. 0.05 for 5%
    s = start
    y = 0
    while y < years:
        s = s * (1+rate)
        y = y+1
    return s


if __name__ == "__main__":
    print(most([1, 2, 2, 3, 3, 3, 2]))
    print(not_in_b_case_insnstv(
        ['Apple', 'banana', 'Cherry'], ['BANANA', 'pear']))
    print(fin(1000, 0.05, 3))

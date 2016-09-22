# -*- coding: utf-8 -*-
#
# 100/100


def solution(A):
    total = sum(A)
    before = 0
    after = 0

    if not A:
        return -1

    if total - A[0] == 0:
        return 0

    for idx, item in enumerate(A[:-1], start=1):
        before += item
        current = A[idx]
        after = total - before - current

        if before == after:
            return idx

    return -1


assert solution([-1, 3, -4, 5, 1, -6, 2, 1]) == 1
assert solution([0, 0, 0]) == 0
assert solution([]) == 0
assert solution([1, 2, 3, 4]) == -1
assert solution([-1, -1, 1]) == 0
assert solution([-1, 1, 1]) == 2

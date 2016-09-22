# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/tape_equilibrium
# 100/100


def solution(A):
    total = sum(A)

    results = []
    accumulator = 0
    for item in A[:-1]:
        accumulator += 2 * item
        results.append(abs(total - accumulator))

    return min(results)


assert solution([3, 1, 2, 4, 3]) == 1
assert solution([1, 1]) == 0
assert solution([0, 0]) == 0
assert solution([1, 2, 3, -10, 5]) == 1
assert solution([1, 4, 3, -15, 5]) == 4

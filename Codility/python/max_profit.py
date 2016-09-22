# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/max_profit
# 100/100


def golden_max_slice(A):
    max_ending = max_slice = 0

    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)

    return max_slice


def solution(A):
    profits = [0]
    for idx, item in enumerate(A):
        if idx == 0:
            continue

        profits.append(item - A[idx - 1])

    return golden_max_slice(profits)


assert solution([]) == 0
assert solution([42]) == 0
assert solution([11, 10, 15, 5, 16, 8, 7, 8]) == 11
assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
assert solution([11, 10, 9, 7, 1]) == 0
assert solution([15, 16, 8, 12]) == 4
assert solution([15, 16, 17, 21]) == 6
assert solution([10, 5, 8, 9, 22, 11, 13, 30, 9, 40, 1]) == 35

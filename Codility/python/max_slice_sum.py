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
    result = golden_max_slice(A)
    if not result:
        result = max(A)

    return result


assert solution([42]) == 42
assert solution([3, 2, -6, 4, 0]) == 5
assert solution([5, -7, 3, 5, -2, 4, -1]) == 10
assert solution([-10, -15, -23, 7, -13, -9, -5]) == 7
assert solution([-10]) == -10
assert solution([-10, -3, -5, -1, -1, -6]) == -1

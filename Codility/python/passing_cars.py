# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/passing_cars
# 100/100


def solution(A):
    total = sum(A)
    accumulator = total
    result = 0

    for item in A:
        accumulator -= item

        if item == 0:
            result += accumulator

        if result > 1000000000:
            return -1

    return result


assert solution([0, 1, 0, 1, 1]) == 5
assert solution([0, 1, 1, 1, 1]) == 4
assert solution([1, 1, 1, 1, 1]) == 0
assert solution([0, 0, 0, 1, 1]) == 6
assert solution([0, 0, 0, 0, 1]) == 4
assert solution([0] * 10 + [1] * 10) == 100
assert solution([0] * 10 + [1] * 10) == 100
assert solution([0] * 10000 + [1] * 100000) == 1000000000
assert solution([0] * 10001 + [1] * 100000) == -1
assert solution([0]) == 0
assert solution([1]) == 0
assert solution([1]) == 0
assert solution([1, 0]) == 0

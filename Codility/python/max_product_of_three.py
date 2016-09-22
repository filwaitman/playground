# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/max_product_of_three
# 100/100


def solution(A):
    A.sort()

    results = [
        A[0] * A[1] * A[2],
        A[-1] * A[0] * A[1],
        A[-2] * A[-1] * A[0],
        A[-3] * A[-2] * A[-1],
    ]

    return max(results)


assert solution([-3, 1, 2, -2, 1, 6]) == 36
assert solution([-3, 1, 2, -2, 5, 6]) == 60
assert solution([-3, 30, 2, -2, 5, 6]) == 900
assert solution([-5, -1, -3, -2, -4]) == -6
assert solution([-5, -1, 3, -2, -4]) == 60
assert solution([-10, 5, 5, -2, -30]) == 1500
assert solution([-10, -3, -2, 5, 5]) == 150
assert solution([-10, -2, 0, 5, 5]) == 100
assert solution([-1, -1, -1, 0, 1, 1, 1]) == 1
assert solution([-1, -1, -1, 0, 1]) == 1
assert solution([-1, -1, -1, 0]) == 0

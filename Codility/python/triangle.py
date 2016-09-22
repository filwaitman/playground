# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/triangle
# 100/100


def solution(A):
    positives = filter(lambda x: x >= 0, A)

    if len(positives) < 3:
        return 0

    positives.sort()

    for P, item in enumerate(positives[:-2]):
        Q = P + 1
        R = Q + 1

        next_item = positives[Q]
        if item + next_item > positives[R]:
            return 1

    return 0


assert solution([10, 2, 5, 1, 8, 20]) == 1
assert solution([10, 50, 5, 1]) == 0
assert solution([]) == 0
assert solution([1, 2]) == 0
assert solution([1, 1, 1]) == 1
assert solution([0, 1, 1]) == 0
assert solution([-13, -5, -2, 1, 1]) == 0
assert solution([5, 8, 10]) == 1
assert solution([5, 8, 10, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 1

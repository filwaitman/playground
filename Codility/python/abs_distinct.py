# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/abs_distinct
# 100/100


def solution(A):
    positives = map(abs, A)
    return len(set(positives))


assert solution([-5, -3, -1, 0, 3, 6]) == 5
assert solution([42]) == 1
assert solution(range(-1000, 0) + range(1, 1001)) == 1000

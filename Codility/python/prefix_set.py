# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/prefix_set
# 100/100


def solution(A):
    expected = set(A)
    took = set()

    for idx, item in enumerate(A):
        took.add(item)
        if took == expected:
            return idx


assert solution(range(10)) == 9
assert solution([1]) == 0
assert solution([1, 2, 2, 2, 2]) == 1
assert solution([1, 2, 2, 2, 2, 3]) == 5

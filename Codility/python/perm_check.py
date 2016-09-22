# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/perm_check
# 100/100


def solution(A):
    A.sort()
    return 1 if range(1, len(A) + 1) == A else 0


assert solution([4, 1, 3, 2]) == 1

assert solution([4, 1, 3]) == 0
assert solution([4, 1, 2]) == 0
assert solution([2, 3, 4]) == 0
assert solution([4, 1, 3, 2, 2]) == 0

big = range(100000, 0, -1)
assert solution(big) == 1

del big[50000]
assert solution(big) == 0

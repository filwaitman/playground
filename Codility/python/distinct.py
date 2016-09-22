# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/distinct
# 100/100


def solution(A):
    return len(set(A))


assert solution([2, 1, 1, 2, 3, 1]) == 3
assert solution([]) == 0
assert solution([-13]) == 1
assert solution([-13, 42]) == 2
assert solution(range(1500) + range(1500)) == 1500
assert solution(range(1500) + range(3000)) == 3000
assert solution(range(1500) + range(2500, 3000)) == 2000

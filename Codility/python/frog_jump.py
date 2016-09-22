# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/frog_jmp
# 100/100


def solution(X, Y, D):
    import math
    return int(math.ceil((Y - X) / float(D)))


assert solution(10, 85, 30) == 3
assert solution(10, 100, 30) == 3
assert solution(10, 101, 30) == 4
assert solution(10, 10, 30) == 0
assert solution(1, 1, 1) == 0
assert solution(1, 10, 1) == 9

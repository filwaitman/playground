# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/str_symmetry_point
# 100/100


def solution(S):
    S_len = len(S)
    middle = S_len / 2

    if S_len % 2 == 0:
        return -1

    if S[0:middle] == S[S_len:middle:-1]:
        return middle

    return -1


assert solution('racecar') == 3
assert solution('abba') == -1
assert solution('x') == 0
assert solution('abc') == -1
assert solution('') == -1

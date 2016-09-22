# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/frog_river_one
# 100/100


def solution(X, A):
    expected = set(range(1, X+1))

    path_created = set()
    for seconds_elapsed, item in enumerate(A):
        if item > X:
            continue

        path_created.add(item)
        if path_created == expected:
            return seconds_elapsed

    return -1


assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
assert solution(3, [1, 3, 1, 4, 2, 3, 5, 4]) == 4
assert solution(1, [1]) == 0
assert solution(6, [1, 3, 1, 4, 2, 3, 5, 4]) == -1
assert solution(5, [1, 3, 1, 4, 2, 3, 4]) == -1
assert solution(6, [6]) == -1
assert solution(6, [7]) == -1

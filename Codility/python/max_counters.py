# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/max_counters
# 100/60


def solution(N, A):
    result = [0] * N
    max_value = 0

    for item in A:
        if 1 <= item <= N:
            idx = item - 1
            result[idx] = result[idx] + 1
            max_value = max(result[idx], max_value)

        elif item == N + 1:
            result = [max_value] * N

    return result


assert solution(2, [1]) == [1, 0]
assert solution(1, [1]) == [1]
assert solution(2, [3]) == [0, 0]
assert solution(3, [4, 3]) == [0, 0, 1]
assert solution(3, [4, 3, 4]) == [1, 1, 1]
assert solution(5, [3]) == [0, 0, 1, 0, 0]
assert solution(5, [3, 4]) == [0, 0, 1, 1, 0]
assert solution(5, [3, 4, 4]) == [0, 0, 1, 2, 0]
assert solution(5, [3, 4, 4, 6]) == [2, 2, 2, 2, 2]
assert solution(5, [3, 4, 4, 6, 1]) == [3, 2, 2, 2, 2]
assert solution(5, [3, 4, 4, 6, 1, 4]) == [3, 2, 2, 3, 2]
assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]

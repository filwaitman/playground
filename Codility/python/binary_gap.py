# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/binary_gap
# 100/NA


def solution(N):
    max_gap = 0
    current_gap = 0
    has_one_before = False

    accumulator = N

    while accumulator:
        if accumulator % 2 == 0:
            accumulator = accumulator / 2
            current_gap += 1

        else:
            accumulator = (accumulator - 1) / 2

            if has_one_before:
                max_gap = max(max_gap, current_gap)

            has_one_before = True
            current_gap = 0

    return max_gap


assert solution(1) == 0
assert solution(127) == 0
assert solution(2) == 0
assert solution(1041) == 5
assert solution(529) == 4
assert solution(20) == 1
assert solution(15) == 0
assert solution(9) == 2
assert solution(12) == 0
assert solution(17) == 3

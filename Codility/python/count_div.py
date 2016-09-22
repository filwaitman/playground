# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/count_div
# 100/100


def next_divisor(initial, K):
    import math
    return int(K * math.ceil(initial / float(K)))


def previous_divisor(final, K):
    import math
    return int(K * math.floor(final / float(K)))


def solution(A, B, K):
    initial = next_divisor(A, K)
    final = previous_divisor(B, K)

    result = 0

    if A <= initial <= B:
        result += 1
    else:
        return 0

    if A <= final <= B:
        result += 1

    result += (final - initial - 1) / K

    return result


assert solution(6, 11, 2) == 3
assert solution(6, 12, 2) == 4
assert solution(1, 5, 1) == 5
assert solution(1, 5, 2) == 2
assert solution(1, 5, 3) == 1
assert solution(1, 5, 4) == 1
assert solution(1, 5, 5) == 1
assert solution(1, 5, 6) == 0
assert solution(1, 1, 1) == 1
assert solution(1, 1, 2) == 0
assert solution(0, 15, 2) == 8
assert solution(0, 0, 123) == 1
assert solution(0, 123456789, 123456789 / 2) == 3
assert solution(123456, 123456799, 123456789 / 2) == 2

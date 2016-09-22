# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/min_perimeter_rectangle
# 100/100


def get_divisors(n):
    import math

    i = 0
    result = []

    while (i < math.floor(math.sqrt(n))):
        i += 1
        if (n % i == 0):
            result.append([i, n / i])

    return result


def solution(N):
    last_divisor = get_divisors(N)[-1]
    return last_divisor[0] * 2 + last_divisor[1] * 2


assert solution(1) == 4
assert solution(30) == 22
assert solution(7) == 16
assert solution(10) == 14

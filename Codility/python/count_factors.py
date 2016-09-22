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


def is_perfect_square(n):
    import math
    sqrt = math.sqrt(n)
    return sqrt == int(sqrt)


def solution(N):
    if is_perfect_square(N):
        return len(get_divisors(N)) * 2 - 1
    return len(get_divisors(N)) * 2


assert solution(1) == 1
assert solution(2) == 2
assert solution(25) == 3
assert solution(24) == 8
assert solution(100) == 9

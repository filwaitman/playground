# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/chocolates_by_numbers
# 100/100


def gcd(a, b, res=1):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def solution(N, M):
    return lcm(N, M) / M


assert solution(1, 1) == 1
assert solution(5, 5) == 1
assert solution(5, 1) == 5
assert solution(10, 4) == 5
assert solution(6, 3) == 2
assert solution(6, 2) == 3
assert solution(6, 4) == 3
assert solution(6, 8) == 3

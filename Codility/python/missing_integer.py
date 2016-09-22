# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/missing_integer
# 100/100


def solution(A):
    positives = filter(lambda x: x > 0, A)
    positives = list(set(positives))
    positives.sort()

    counter = 1
    for number in positives:
        if number > counter:
            return counter

        counter += 1

    return counter


assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([-1, -3, -6, -4, 1, -2, 2]) == 3
assert solution([1, 1, 1, 1, 1, 2, 3, 5]) == 4
assert solution([0]) == 1
assert solution([1]) == 2
assert solution([1, 1, 1, 1, 1, 1]) == 2

big = range(1000000, -1000000, -1)
assert solution(big) == 1000001

big = range(1000000, -1000000, -1)
del big[50000]
assert solution(big) == 950000

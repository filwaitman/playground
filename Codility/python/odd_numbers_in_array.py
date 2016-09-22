# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/odd_occurrences_in_array
# 100/100


def solution(A):
    numbers = {}

    for item in A:
        numbers.setdefault(item, 0)
        numbers[item] += 1

    for item, occurences in numbers.items():
        if occurences % 2 == 1:
            return item


assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
assert solution([1]) == 1
assert solution([5, 5, 5]) == 5
assert solution(range(1000) + range(1000) + [666, ]) == 666

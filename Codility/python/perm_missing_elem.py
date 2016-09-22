# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/perm_missing_elem
# 100/100


def solution(A):
    if not A:
        return 1

    initial = 1
    final = len(A)

    complete_list = range(initial, final + 2)

    difference = set(complete_list) - set(A)

    try:
        return difference.pop()
    except KeyError:
        return final + 1


assert solution([]) == 1
assert solution([1]) == 2
assert solution([2]) == 1
assert solution([2, 3, 1, 5]) == 4
assert solution([1, 2, 4]) == 3
assert solution([1, 2, 4]) == 3
assert solution(range(1, 189) + range(190, 100000)) == 189
assert solution(range(1, 98765)) == 98765

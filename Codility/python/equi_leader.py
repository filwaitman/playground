# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/equi_leader
# 100/100


def get_most_common(A):
    from collections import Counter
    data = Counter(A)
    return data.most_common(1)[0]


def solution(A):
    leader, qty = get_most_common(A)

    result = 0
    pivots_before = 0
    total_numbers = len(A)

    for numbers_before, item in enumerate(A, start=1):
        numbers_after = total_numbers - numbers_before

        if item == leader:
            pivots_before += 1
            pivots_after = qty - pivots_before

        if pivots_before > numbers_before / 2 and pivots_after > numbers_after / 2:
            result += 1

    return result


assert solution([3, 4, 3, 2, 3, -1, 3, 3]) == 4, solution([3, 4, 3, 2, 3, -1, 3, 3])
assert solution([3, 4, 7, 2, 1, -1, 3, 3]) == 0, solution([3, 4, 7, 2, 1, -1, 3, 3])
assert solution([1]) == 0, solution([1])
assert solution([5, 5]) == 1, solution([5, 5])
assert solution([4, 3, 4, 4, 4, 2]) == 2, solution([4, 3, 4, 4, 4, 2])
assert solution([10] * 15 + range(10)) == 4, solution([10] * 15 + range(10))
assert solution([5] * 10 + range(5) + [5] * 10) == 24

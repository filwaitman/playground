# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/binary_gap
# 100/100


def caterpillar(A, rule_to_check):
    len_a = len(A)
    result = 0
    for cat_start_idx in range(len_a):
        cat_end_idx = cat_start_idx + 2
        for cat_mid_idx in range(cat_start_idx + 1, len_a):
            while (cat_end_idx < len_a and rule_to_check(A, cat_start_idx, cat_mid_idx, cat_end_idx)):
                cat_end_idx += 1
            result += cat_end_idx - cat_mid_idx - 1
    return result


def solution(A):
    def rule_to_check(A, cat_start_idx, cat_mid_idx, cat_end_idx):
        return A[cat_start_idx] + A[cat_mid_idx] > A[cat_end_idx]
    A.sort()
    return caterpillar(A, rule_to_check)


assert solution([10, 2, 5, 1, 8, 12]) == 4
assert solution([1, 3, 4, 5, 7]) == 3
assert solution([1, 1, 1]) == 1
assert solution([1, 1, 1, 1, 1]) == 10
assert solution([]) == 0
assert solution([2]) == 0
assert solution([2, 3]) == 0
assert solution([2, 3, 4]) == 1

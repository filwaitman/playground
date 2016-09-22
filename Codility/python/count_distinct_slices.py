# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/count_distinct_slices
# 100/60


def solution(M, A):
    threshold = 1000000000
    result = 0

    for initial_idx in range(len(A)):
        for final_idx in range(initial_idx, len(A)):
            if len(A[initial_idx:final_idx + 1]) == len(set(A[initial_idx:final_idx + 1])):
                result += 1

                if result > threshold:
                    return threshold
            else:
                break

    return result


assert solution(6, [3, 4, 5, 5, 2]) == 9
assert solution(6, [3, 3, 3]) == 3
assert solution(6, [3, 2, 3, 2]) == 7
assert solution(6, [3, 2, 1, 2, 3]) == 11
assert solution(6, [3, 2, 1, 1, 1, 1, 2, 3, 3, 3, 2]) == 18
assert solution(0, [0, 0, 0, 0, 0]) == 5
assert solution(13, [12]) == 1

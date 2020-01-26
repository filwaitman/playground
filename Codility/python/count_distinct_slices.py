# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/count_distinct_slices
# 100/60


import functools
import itertools
import math


# @functools.lru_cache()
def factorial(x):
    return math.factorial(x)


@functools.lru_cache()
def combinations(n, r):
    return len(list(itertools.combinations(range(n), r)))
    # return int(
    #     (factorial(n))
    #     /
    #     (factorial(r)) * factorial(n - r)
    # )


def solution(M, A):
    max_result = 1_000_000_000
    len_a = len(A)
    result = 0
    final_end_idx = -1

    for cat_start_idx in range(len_a - 1):
        if cat_start_idx < final_end_idx:
            continue

        cat_end_idx = cat_start_idx + 1
        sub_A = [A[cat_start_idx]]
        while ((cat_end_idx < len_a) and (A[cat_end_idx] not in sub_A)):
            sub_A.append(A[cat_end_idx])
            cat_end_idx += 1

        result += combinations(cat_end_idx - cat_start_idx, 2)
        cat_end_idx -= 1
        final_end_idx = cat_end_idx

        if result > max_result:
            return max_result

    return min(result + len_a, max_result)


def solution_slow(M, A):
    len_a = len(A)
    result = 0
    max_result = 1_000_000_000
    for cat_start_idx in range(len_a):
        cat_end_idx = cat_start_idx
        sub_A = []
        while ((cat_end_idx < len_a) and (A[cat_end_idx] not in sub_A)):
            sub_A.append(A[cat_end_idx])
            result += 1
            cat_end_idx += 1

            if result > max_result:
                return max_result

    return result

# assert combinations(2, 2) == 3
# assert combinations(1, 2) == 1
# assert combinations(0, 2) == 0
# assert solution(6, [3, 4, 5, 5, 2]) == 9
# assert solution(6, [3, 3, 3]) == 3
# assert solution(6, [3, 2, 3, 2]) == 7
# assert solution(6, [3, 2, 1, 2, 3]) == 11
# assert solution(6, [3, 2, 1, 1, 1, 1, 2, 3, 3, 3, 2]) == 18
# assert solution(0, [0, 0, 0, 0, 0]) == 5
# assert solution(13, [12]) == 1


import random
import time


M = 20
A = [random.randint(1, M) for _ in range(M)]
A = [3, 2, 19, 2, 9, 3, 11, 3, 2, 8, 19, 17, 2, 8, 19, 14, 14, 14, 10, 4]
print(solution(M, A))
print(solution_slow(M, A))


# N = 100000
# start = time.time()
# solution(N, [random.randint(1, N) for _ in range(N)])
# end = time.time()
# assert end - start < 6


'''
import functools
import itertools
import math


# @functools.lru_cache()
def factorial(x):
    return math.factorial(x)


def combinations(n, r):
    return int(
        (factorial(n + r - 1))
        /
        (factorial(r)) * factorial(n - 1)
    )


def solution(M, A):
    max_result = 1_000_000_000
    len_a = len(A)
    result = 0
    final_end_idx = -1

    for cat_start_idx in range(len_a):
        if cat_start_idx < final_end_idx:
            continue

        cat_end_idx = cat_start_idx
        sub_A = []
        while ((cat_end_idx < len_a) and (A[cat_end_idx] not in sub_A)):
            sub_A.append(A[cat_end_idx])
            cat_end_idx += 1

        final_end_idx = cat_end_idx
        print('final_end_idx', final_end_idx)
        result += combinations(cat_end_idx - cat_start_idx, 2)
        print('result', result)
        # cat_end_idx -= 1
        # final_end_idx = cat_end_idx

        if result > max_result:
            return max_result

    return result
'''

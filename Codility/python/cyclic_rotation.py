# -*- coding: utf-8 -*-
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# 100/NA


def solution(A, K):
    if not A:
        return []  # Trivial solution

    # Reduce the problem to a cut_point < len(A) (in order to avoid full rotations in vain)
    cut_point = -(K % len(A))
    return A[cut_point:] + A[:cut_point]


assert solution([3, 8, 9, 7, 6], 0) == [3, 8, 9, 7, 6]
assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
assert solution([3, 8, 9, 7, 6], 2) == [7, 6, 3, 8, 9]
assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution([3, 8, 9, 7, 6], 4) == [8, 9, 7, 6, 3]
assert solution([3, 8, 9, 7, 6], 5) == [3, 8, 9, 7, 6]
assert solution([3, 8, 9, 7, 6], 6) == [6, 3, 8, 9, 7]
assert solution([3, 8, 9, 7, 6], 7) == [7, 6, 3, 8, 9]
assert solution([3, 8, 9, 7, 6], 8) == [9, 7, 6, 3, 8]
assert solution([3, 8, 9, 7, 6], 9) == [8, 9, 7, 6, 3]
assert solution([3, 8, 9, 7, 6], 10) == [3, 8, 9, 7, 6]
assert solution([], 0) == []
assert solution([], 1) == []
assert solution([], 100) == []
assert solution([42], 0) == [42]
assert solution([42], 1) == [42]
assert solution([42], 100) == [42]
assert solution([0, 0, 0], 1) == [0, 0, 0]
assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
assert solution([3, -8, 9, 7, 6], 0) == [3, -8, 9, 7, 6]
assert solution([3, -8, 9, 7, 6], 1) == [6, 3, -8, 9, 7]
assert solution([3, -8, 9, 7, 6], 2) == [7, 6, 3, -8, 9]
assert solution([3, -8, 9, 7, 6], 3) == [9, 7, 6, 3, -8]
assert solution([3, -8, 9, 7, 6], 4) == [-8, 9, 7, 6, 3]
assert solution([3, -8, 9, 7, 6], 5) == [3, -8, 9, 7, 6]

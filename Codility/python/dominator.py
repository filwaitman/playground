# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/dominator
# 100/100


def get_most_common(A):
    from collections import Counter
    data = Counter(A)
    try:
        return data.most_common(1)[0][0]
    except:
        return None


def solution(A):
    try:
        most_common = get_most_common(A)
    except:
        return -1

    if A.count(most_common) > len(A) / 2:
        return A.index(most_common)
    return -1


assert solution([3, 4, 3, 2, 3, -1, 3, 3]) == 0
assert solution([3, 4, 7, 2, 1, -1, 3, 3]) == -1
assert solution([]) == -1
assert solution([1]) == 0

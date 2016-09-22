# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/tie_ropes
# 100/100


def solution(K, A):
    results = []
    current = 0

    for rope in A:
        if rope >= K:
            results.append(rope)
            current = 0

        else:
            current += rope
            if current >= K:
                results.append(current)
                current = 0

    return len(results)

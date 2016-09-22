# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/max_nonoverlapping_segments
# 100/100


def solution(A, B):
    result = 0
    current_end = -1

    for p_init, p_end in zip(A, B):
        if p_init > current_end:
            result += 1
            current_end = p_end

    return result

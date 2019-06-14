# -*- coding: utf-8 -*-
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
# 100/100 - https://app.codility.com/demo/results/training8K2PVF-Y7S/


def solution(H):
    total_blocks = 0
    pending_blocks = []

    for current_height in H:
        if (pending_blocks) and (pending_blocks[-1] > current_height):
            while pending_blocks and pending_blocks[-1] > current_height:
                pending_blocks.pop()
                total_blocks += 1

        if (not pending_blocks) or (pending_blocks[-1] != current_height):
            pending_blocks.append(current_height)

    total_blocks += len(pending_blocks)
    return total_blocks


assert solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7
assert solution([1]) == 1
assert solution([1, 1, 1, 1]) == 1
assert solution([1, 1, 2, 2]) == 2
assert solution([1, 2, 2, 1]) == 2
assert solution([2, 2, 2, 1]) == 2
assert solution([2, 1, 1, 2]) == 3
assert solution([2, 1, 2, 1]) == 3
assert solution([3, 1, 5, 1]) == 3
assert solution([3, 1, 5, 5]) == 3
assert solution([3, 1, 5, 7]) == 4

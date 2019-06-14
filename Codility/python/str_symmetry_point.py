# https://app.codility.com/programmers/lessons/99-future_training/str_symmetry_point/
# 100/100 - https://app.codility.com/demo/results/training6BAD2V-UE3/


def solution(S):
    len_S = len(S)
    if len_S % 2 == 0:
        return -1

    mid_index = int((len_S - 1) / 2)
    return mid_index if (S[mid_index + 1:] == S[:mid_index][::-1]) else -1


assert solution('racecar') == 3
assert solution('x') == 0
assert solution('xxx') == 1
assert solution('romametemamor') == 6
assert solution('') == -1
assert solution('xx') == -1
assert solution('weird') == -1

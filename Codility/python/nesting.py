# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/nesting
# 100/100


def solution(S):
    opened_parenthesis = 0

    for char in S:
        if char == '(':
            opened_parenthesis += 1
        else:
            opened_parenthesis -= 1

        if opened_parenthesis < 0:
            return 0

    if opened_parenthesis:
        return 0
    return 1


assert solution('(()(())())') == 1
assert solution('())') == 0
assert solution('') == 1
assert solution('()') == 1
assert solution('((((((((()))))))))') == 1
assert solution('()(())()((()))(()())') == 1
assert solution('(') == 0
assert solution(')') == 0
assert solution(')(') == 0
assert solution('()(') == 0
assert solution('()(()') == 0

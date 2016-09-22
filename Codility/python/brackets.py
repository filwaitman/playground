# -*- coding: utf-8 -*-
# https://codility.com/programmers/task/brackets
# 100/60


def solution(S):
    def evaluate_part(substr):
        closing_tag = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        if not substr:
            return 1

        tag = substr[0]
        if tag not in closing_tag.keys():
            return 0

        counter = 0
        for idx, char in enumerate(substr):
            if char == tag:
                counter += 1
            elif char == closing_tag[tag]:
                counter -= 1

            if counter == 0:
                return evaluate_part(substr[1:idx]) * evaluate_part(substr[idx + 1:])

        return 0

    return evaluate_part(S)


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
assert solution('([{}])') == 1
assert solution('(][)') == 0
assert solution('([{])') == 0
assert solution('([{{{}()}[]}])') == 1
assert solution('([)()]') == 0
assert solution(')))))') == 0

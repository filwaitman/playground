# https://codility.com/programmers/task/brackets
# 100/100 - https://app.codility.com/demo/results/trainingNJA88R-WUJ/


def solution(S):
    open_tags = []
    close_open_tag_mapping = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for x in S:
        if x in '({[':
            open_tags.append(x)

        else:
            open_tag = close_open_tag_mapping[x]
            if not open_tags or open_tags.pop() != open_tag:
                return 0

    return 0 if open_tags else 1


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

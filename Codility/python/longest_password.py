# https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/
# 100/NA - https://app.codility.com/demo/results/trainingKRHDAT-3J9/

def solution(S):
    import re
    candidates = S.split()

    candidates = list(filter(lambda x: re.match(r'^[a-zA-Z0-9]+$', x), candidates))
    candidates = list(filter(lambda x: len(''.join(re.findall(r'.*?([0-9]).*?', x))) % 2 == 1, candidates))
    candidates = list(filter(lambda x: len(''.join(re.findall(r'.*?([a-zA-Z]).*?', x))) % 2 == 0, candidates))

    return max(len(x) for x in candidates) if candidates else -1


assert solution('test 5 a0A pass007 ?xy1') == 7
assert solution(' ') == -1
assert solution('a') == -1
assert solution('5') == 1
assert solution('5 55 555 5555') == 3
assert solution('5aa 55aa 555aa 5555aa') == 5
assert solution('a5a a55a a555a a5555a') == 5
assert solution('aa5 aa55 aa555 aa5555') == 5
assert solution('a5a 5aa5 5a5a5 55aa55') == 5
assert solution('a5a 5aa5 ?5a5a5 55aa55') == 3
assert solution('a5~a 5aa5 ?5a5a5 55aa55') == -1

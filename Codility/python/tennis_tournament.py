# https://app.codility.com/programmers/lessons/92-tasks_from_indeed_prime_2016_college_coders_challenge/tennis_tournament/
# 100/NA - https://app.codility.com/demo/results/trainingESQRJX-YE5/


def solution(P, C):
    return min(int(P/2), C)


assert solution(5, 3) == 2
assert solution(10, 3) == 3
assert solution(1, 1) == 0
assert solution(30000, 30000) == 15000

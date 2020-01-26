# https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/
# 100/57


def solution_greedy(A):
    results = []
    for a in A:
        for b in A:
            results.append(abs(a + b))
    return min(results)


def solution(A):
    A.sort()

    first_positive = None
    for idx, elem in enumerate(A):
        if elem >= 0:
            first_positive = idx
            break

    if first_positive is None:
        return abs(A[-1] * 2)  # Optimization for trivial case
    if first_positive == 0:
        return abs(A[0] * 2)  # Optimization for trivial case

    # If we reached here we have mixed positive/negative numbers
    all_doubled = [abs(x * 2) for x in A]
    len_a = len(A)

    min_found = None
    left_arm = 0
    while left_arm < first_positive:

        right_arm = len_a
        while right_arm > first_positive:
            found_now = abs(A[left_arm] + A[right_arm - 1])
            print(found_now)

            if (min_found is None) or (found_now <= min_found):
                min_found = found_now
                right_arm -= 1
            else:
                break

        left_arm += 1

    return min(all_doubled + [min_found])
    # candidates = [min_abs_found]

    # to_left = None
    # if left_arm > 0:
    #     to_left = abs(A[left_arm - 1] + A[right_arm])
    #     candidates.append(to_left)

    # to_right = None
    # if right_arm < len_a:
    #     to_right = abs(A[left_arm] + A[right_arm + 1])
    #     candidates.append(to_right)

    # if min(candidates) == min_abs_found:
    #     return min_abs_found
    # elif min(candidates) == to_left:
    #     min_abs_found = to_left
    #     left_arm -= 1
    # elif min(candidates) == to_right:
    #     min_abs_found = to_right
    #     right_arm += 1
    # else:
    #     raise RuntimeError()


# assert solution_greedy([1]) == solution([1])
# assert solution_greedy([-3]) == solution([-3])
# assert solution_greedy([1, 4]) == solution([1, 4])
# assert solution_greedy([1, 4, -3]) == solution([1, 4, -3])
assert solution_greedy([-8, 4, 5, -10, 3]) == solution([-8, 4, 5, -10, 3])
assert solution_greedy([2, 3, 5, 10, 20]) == solution([2, 3, 5, 10, 20])
assert solution_greedy([10, 5, 2, 3, 5, 10, 20]) == solution([10, 5, 2, 3, 5, 10, 20])


import random
xx = [random.randint(-10000, 10000) for _ in range(1000)]
assert solution_greedy(xx) == solution(xx)
assert solution_greedy([-10, 1, 5, 10, 20]) == solution([-10, 1, 5, 10, 20])


yy = [random.randint(-10000, 10000) for _ in range(10)]
assert solution_greedy(yy) == solution(yy)

zz = [-8072, -7049, -6065, -3270, -1011, -484, 3377, 4178, 8691, 9577]
assert solution_greedy(zz) == solution(zz)



[-8072, -7049, -6065, -3270, -1011, -484, 3377, 4178, 8691, 9577]

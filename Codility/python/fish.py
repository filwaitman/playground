# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
# 100/100


def solution(A, B):
    # Arrays ordered downstream;
    # Arrays size in range [1..100,000]. A and B have the same size;
    # A=size. Elements are distinct, and in range [0..1,000,000,000];
    # B=direction (0=upstream/left, 1=downstream/right). Elements are 0 or 1.
    LEFT = 0
    fishes_going_right = []  # 1d array of sizes
    fishes_that_survived = []  # 1d array of sizes

    for i in range(0, len(A)):
        current_fish_size = A[i]
        current_fish_direction = B[i]
        current_fish_lived = True

        if current_fish_direction == LEFT:
            while fishes_going_right:
                if current_fish_size > fishes_going_right[-1]:
                    fishes_going_right.pop()
                else:
                    current_fish_lived = False
                    break

            if current_fish_lived:
                fishes_that_survived.append(current_fish_size)

        else:
            fishes_going_right.append(current_fish_size)

    return len(fishes_that_survived + fishes_going_right)


assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([4], [0]) == 1
assert solution([4], [1]) == 1
assert solution([4, 5], [0, 1]) == 2
assert solution([5, 4], [0, 1]) == 2
assert solution([4, 5], [1, 0]) == 1
assert solution([5, 4], [1, 0]) == 1
assert solution([0, 5], [1, 0]) == 1
assert solution([5, 0], [1, 0]) == 1
assert solution([5, 2, 3, 1], [0, 1, 0, 0]) == 3
assert solution([5, 2, 1, 3], [0, 1, 0, 0]) == 2
assert solution([5, 2, 3, 1], [0, 1, 1, 1]) == 4
assert solution([5, 2, 3, 1], [0, 1, 0, 1]) == 3
assert solution([5, 2, 3, 1], [1, 0, 1, 0]) == 2
assert solution([5, 2, 3, 1], [1, 0, 1, 0]) == 2
assert solution([4, 1, 5, 2], [1, 0, 0, 0]) == 2
assert solution([4, 1, 2, 5], [1, 0, 0, 0]) == 1
assert solution([6, 1, 2, 5], [1, 1, 1, 0]) == 1

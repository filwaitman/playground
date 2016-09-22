# -*- coding: utf-8 -*-
# http://rosalind.info/problems/perm/
import itertools


def permutations(n):
    result = [x for x in itertools.permutations(range(1, n+1))]

    with open('result', 'w') as f:
        f.write(str(len(result)) + '\n')
        for line in result:
            f.write(' '.join(map(str, line)) + '\n')

    return len(result), result

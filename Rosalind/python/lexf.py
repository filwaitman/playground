# -*- coding: utf-8 -*-
# http://rosalind.info/problems/lexf/
import itertools


def arrange(raw_string, n):
    string = raw_string.replace(' ', '')
    result = [x for x in itertools.product(string, repeat=n)]

    with open('result', 'w') as f:
        for line in result:
            f.write(''.join(map(str, line)) + '\n')

    return result

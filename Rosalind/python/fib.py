# -*- coding: utf-8 -*-
# http://rosalind.info/problems/fib/
import sys


def fib(n, k):
    result = [1, 1]
    while len(result) < n:
        result.append(result[-1] + k * result[-2])
    print result[-1]


if __name__ == '__main__':
    n, k = map(int, sys.argv[1:3])
    fib(n, k)

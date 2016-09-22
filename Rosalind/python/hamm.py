# -*- coding: utf-8 -*-
# http://rosalind.info/problems/hamm/
import sys


def hammington_distance(str1, str2):
    print sum(x != y for x, y in zip(str1, str2))


if __name__ == '__main__':
    str1, str2 = sys.argv[1:3]
    hammington_distance(str1, str2)

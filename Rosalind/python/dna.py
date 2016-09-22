# -*- coding: utf-8 -*-
# http://rosalind.info/problems/dna/
import sys


def count_acgt(string):
    return (string.count('A'), string.count('C'), string.count('G'), string.count('T'))


if __name__ == '__main__':
    string = sys.argv[1]
    count_acgt(string)

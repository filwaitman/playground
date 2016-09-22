# -*- coding: utf-8 -*-
# http://rosalind.info/problems/revc/
import sys


def reverse_complement(string):
    reversed_ = string[::-1]
    reversed_ = reversed_.replace('A', 'X').replace('T', 'A').replace('X', 'T')
    reversed_ = reversed_.replace('C', 'X').replace('G', 'C').replace('X', 'G')
    return reversed_


if __name__ == '__main__':
    string = sys.argv[1]
    reverse_complement(string)

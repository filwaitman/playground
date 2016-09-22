# -*- coding: utf-8 -*-
# http://rosalind.info/problems/rna/
import sys


def dna_to_rna(string):
    return string.replace('T', 'U')


if __name__ == '__main__':
    string = sys.argv[1]
    dna_to_rna(string)

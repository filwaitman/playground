# -*- coding: utf-8 -*-
# http://rosalind.info/problems/iprb/
import itertools
import sys


PROBABILITIES_MAPPING = {
    ('AA', 'AA'): 1,
    ('AA', 'Aa'): 1,
    ('AA', 'aa'): 1,
    ('Aa', 'Aa'): 0.75,
    ('Aa', 'aa'): 0.5,
    ('aa', 'aa'): 0,
}


if __name__ == '__main__':
    qt_AA, qt_Aa, qt_aa = map(int, sys.argv[1:])
    population = ['AA'] * qt_AA + ['Aa'] * qt_Aa + ['aa'] * qt_aa

    combinations = list(itertools.combinations(population, 2))
    result = sum([PROBABILITIES_MAPPING[combination] for combination in combinations]) / len(combinations)
    print result

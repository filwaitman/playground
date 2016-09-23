# -*- coding: utf-8 -*-

MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


def get_rosalind_dataset_content(filename, only_one=False):
    import re

    with open(filename) as f:
        content = f.read()

    content = re.sub('>Rosalind_.*\n', 'SUPERBREAKLINE\n', content)
    content = content.replace('\n', '')
    content = content.replace('SUPERBREAKLINE', '\n')
    strings = content.split('\n')
    strings = filter(lambda x: x, strings)

    if only_one:
        if len(strings) != 1:
            raise RuntimeError('Lenght should be 1, is {}'.format(len(strings)))
        return strings[0]

    return strings


def possible_chunks(string, return_index=False):
    result = []

    for idx_start in range(len(string)):
        for idx_end in range(idx_start + 2, len(string) + 1):
            chunk = string[idx_start:idx_end]

            if return_index:
                result.append((idx_start, chunk))
            else:
                result.append(chunk)

    return result

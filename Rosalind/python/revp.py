# -*- coding: utf-8 -*-
# http://rosalind.info/problems/revp/
from _helpers import get_rosalind_dataset_content

REVERSE_GENOME = {
    'T': 'A',
    'A': 'T',
    'C': 'G',
    'G': 'C',
}


def is_genome_palindrome(string):
    start_index = 0
    end_index = len(string) - 1

    while start_index <= end_index:
        if string[start_index] != REVERSE_GENOME[string[end_index]]:
            return False

        start_index += 1
        end_index -= 1

    return True


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


def main(string):
    for start_index, chunk in possible_chunks(string, return_index=True):
        if is_genome_palindrome(chunk) and 4 <= len(chunk) <= 12:
            print start_index + 1, len(chunk)


if __name__ == '__main__':
    import os

    filename = 'rosalind_{}.txt'.format(os.path.splitext(__file__)[0])
    string = get_rosalind_dataset_content(filename, only_one=True)

    main(string)

# -*- coding: utf-8 -*-
# http://rosalind.info/problems/revp/
from _helpers import get_rosalind_dataset_content, MONOISOTOPIC_MASS_TABLE


def main(string):
    result = 0

    for char in string:
        result += MONOISOTOPIC_MASS_TABLE[char]

    print result


if __name__ == '__main__':
    from os import path

    filename = path.expanduser(path.join('~', 'Desktop', 'rosalind_{}.txt'.format(path.splitext(__file__)[0])))
    string = get_rosalind_dataset_content(filename, only_one=True)

    main(string)

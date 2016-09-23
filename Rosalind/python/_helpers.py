# -*- coding: utf-8 -*-


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

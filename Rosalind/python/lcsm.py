# -*- coding: utf-8 -*-
# http://rosalind.info/problems/revp/
from _helpers import get_rosalind_dataset_content, possible_chunks


def main(*strings):
    base_string, other_strings = strings[0], strings[1:]
    chunks = possible_chunks(base_string)
    chunks = sorted(chunks, key=len, reverse=True)

    for chunk in chunks:
        chunk_found_on_every_string = True

        for string in other_strings:
            if chunk not in string:
                chunk_found_on_every_string = False
                break

        if not chunk_found_on_every_string:
            continue

        print chunk
        break


if __name__ == '__main__':
    import os

    filename = 'rosalind_{}.txt'.format(os.path.splitext(__file__)[0])
    strings = get_rosalind_dataset_content(filename)

    main(*strings)

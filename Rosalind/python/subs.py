# -*- coding: utf-8 -*-
# http://rosalind.info/problems/subs/
import sys


if __name__ == '__main__':
    string, pattern = sys.argv[1:]

    result = filter(lambda x: string[x-1:].startswith(pattern), range(1, len(string)+1))
    print ' '.join(map(str, result))

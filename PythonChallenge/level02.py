# http://www.pythonchallenge.com/pc/def/ocr.html
import os
import string

curdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(curdir, 'data', 'level02.txt')) as f:
    CONTENT = f.read()

print filter(lambda x: x in string.letters, CONTENT)

# http://www.pythonchallenge.com/pc/def/map.html
import os
import string

curdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(curdir, 'data', 'level01.txt')) as f:
    MESSAGE = f.read()

URL = 'map'


def get_real_content(text):
    real_message = ''
    for char in text:
        if char in string.letters:
            real_char_ord = ord(char) + 2
            if real_char_ord > 122:
                real_char_ord -= 26
            real_message += chr(real_char_ord)

        else:
            real_message += char

    print real_message

get_real_content(MESSAGE)
get_real_content(URL)

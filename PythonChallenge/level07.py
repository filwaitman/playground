# http://www.pythonchallenge.com/pc/def/oxygen.html
import os
import re

from PIL import Image

im = Image.open(os.path.join('data', 'level07.png'))
content = im.tobytes()
secret = re.findall(r'\xff([\w ])\1\1\xff', content)

# By checking and sanitizing secret
next_level = '105 110 116 101 103 114 105 116 121'
print map(chr, map(int, next_level.split()))

# http://www.pythonchallenge.com/pc/def/equality.html
import os
import re

curdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(curdir, 'data', 'level03.txt')) as f:
    CONTENT = f.read()

result = re.findall('[a-z]([A-Z]{3}[a-z][A-Z]{3})[a-z]', CONTENT, re.DOTALL)
print ''.join([x[3] for x in result])

# http://www.pythonchallenge.com/pc/return/good.html
import os

curdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(curdir, 'data', 'level09_1.txt')) as f:
    FIRST = f.read().strip()

curdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(curdir, 'data', 'level09_2.txt')) as f:
    SECOND = f.read().strip()

first_as_list = FIRST.split(',')
second_as_list = SECOND.split(',')

print first_as_list + second_as_list
# Map with first + second
# OK, so I hacked the <map> from previous level to show me the dots connected. Am I a genius, a lazy or a cheater?  =P

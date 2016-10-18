# http://www.pythonchallenge.com/pc/def/peak.html
# from banner.p
import os
import pickle

curdir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(curdir, 'data', 'level05.pickle')) as f:
    CONTENT = f.read()

data = pickle.loads(CONTENT.strip())

for line in data:
    for char, qty in line:
        print char * (qty - 1),
    print

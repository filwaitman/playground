# http://www.pythonchallenge.com/pc/def/channel.html
import os
import zipfile

nothing = '90052'  # from zip's readme

zf = zipfile.ZipFile(os.path.join('data', 'level06.zip'))

message = ''

for i in range(1, 1001):
    print 'Trial #{}'.format(i)

    with zf.open('{}.txt'.format(nothing)) as f:
        content = f.read()

    message += zf.getinfo('{}.txt'.format(nothing)).comment

    nothing = content.split()[-1]
    print content

    if 'comments' in nothing:
        break

print message
# hockey -> oxygen!

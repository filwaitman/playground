# http://www.pythonchallenge.com/pc/def/linkedlist.php
import requests

nothing = '12345'
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

for i in range(1, 401):
    print 'Trial #{}'.format(i)
    response = requests.get('{}?nothing={}'.format(base_url, nothing))
    print response.content

    if 'Yes. Divide by two and keep going.' in response.content:
        nothing = str(int(nothing) / 2)
    else:
        nothing = response.content.split()[-1]

    if 'html' in response.content:
        print response.content
        break

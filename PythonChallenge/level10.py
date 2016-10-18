# http://www.pythonchallenge.com/pc/return/bull.html
a = ['1', '11', '21', '1211', '111221', ]  # from http://www.pythonchallenge.com/pc/return/sequence.txt


def get_chars_counted(x):
    result = ''
    current_char = x[0]
    current_count = 1

    for char in x[1:]:
        if char == current_char:
            current_count += 1
        else:
            result += '{}{}'.format(current_count, current_char)
            current_char = char
            current_count = 1

    result += '{}{}'.format(current_count, current_char)
    return result


result = ['1', ]

for _ in range(30):
    result.append(get_chars_counted(result[-1]))

print result
print result[30]
print 'len(a[30]) = {}'.format(len(result[30]))

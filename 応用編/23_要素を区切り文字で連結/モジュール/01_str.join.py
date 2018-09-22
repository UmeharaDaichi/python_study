


# これを www.python-izm.com としたい
elem = ['www', 'python-izm', 'com']

print('～～～～～～～～～～～～')

# その1

host_name = ''

for val in elem:
	host_name += val + '.'
print(host_name)

# これでは最後にも.が付いてしまう
# if文を付けなければならない

host_name = ''
for val in elem:
	if val != 'com':
		host_name += val + '.'
	else:
		host_name += val

print(host_name)



print('～～～～～～～～～～～～')

# 本番
# pythonなら ↓だけで良い

print('.'.join(elem))


print('\n'.join(elem))
print(','.join(elem))
print(' '.join('1234567890'))

print('+'.join(('1', '2', '3')))

# 数値はエラー。文字列のみ
# print('+'.join((1, 2, 3)))


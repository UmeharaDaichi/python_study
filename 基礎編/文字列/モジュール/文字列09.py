
title = 'よけいなモノ     ◇ 先頭・末尾の削除    ヨケイなモノ'
title = title.lstrip('よけいなモノ').lstrip()
title = title.rstrip('ヨケイなモノ').rstrip()
print(title)



print('----------------------------------')


test_str = '     python-izm.com'
print(test_str)

test_str = test_str.lstrip()
print(test_str)

test_str = test_str.lstrip('python')
print(test_str)


print('----------------------------------')

test_str = 'python-izm.com     '
print(test_str + '/')


test_str = test_str.rstrip()
print(test_str + '/')


test_str = test_str.rstrip("com")
print(test_str)



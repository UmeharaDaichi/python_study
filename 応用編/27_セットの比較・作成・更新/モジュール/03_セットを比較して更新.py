

test_set_1 = {'python', 'izm', 'com'}
test_set_1.intersection_update({'python', 'www'})
print(test_set_1)


test_set_1 = {'python', 'izm', 'com'}
test_set_1.difference_update({'python', 'www'})
print(test_set_1)


test_set_1 = {'python', 'izm', 'com'}
test_set_1.symmetric_difference_update({'python', 'www'})
print(test_set_1)




# 演算子でも同様に
print('\n～～～～～～～～～～～～')

test_set_1 = {'python', 'izm', 'com'}
test_set_1 &= {'python', 'www'}
print(test_set_1)


test_set_1 = {'python', 'izm', 'com'}
test_set_1 -= {'python', 'www'}
print(test_set_1)


test_set_1 = {'python', 'izm', 'com'}
test_set_1 ^= {'python', 'www'}
print(test_set_1)










test_set_1 = {'python', 'izm', 'com'}


print(test_set_1.union({'python', 'www'}))
print(test_set_1.intersection({'python', 'www'}))
print(test_set_1.difference({'python', 'www'}))
print(test_set_1.symmetric_difference({'python', 'www'}))




# 演算子でも、同様の結果を得ることができる
print('～～～～～～～～～～～～')

print(test_set_1 | {'python', 'www'})
print(test_set_1 & {'python', 'www'})
print(test_set_1 - {'python', 'www'})
print(test_set_1 ^ {'python', 'www'})








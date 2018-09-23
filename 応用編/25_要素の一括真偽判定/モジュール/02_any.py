
# any は、いずれかがTrueの時にTrueを返す


test_list_1 = [0, 100, 300, 800, 150, 0, 40]
test_list_2 = ([], [], [])
test_list_3 = (['python', 'izm', 'com'], ['www', 'http'])

print(any(test_list_1))
print(any(test_list_2))
print(any(test_list_3))



# python では、数値の0や空のリストはFalse扱い



# any関数は、以下の処理と同じことを行っています
# 公式ドキュメントより引用らしい

def any(iterable):
	for element in iterable:
		if element:
			return True
	return False



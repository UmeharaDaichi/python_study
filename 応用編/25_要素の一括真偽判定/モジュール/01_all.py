

test_list_1 = [0, 100, 300, 800, 150, 0, 40]
test_list_2 = ([], [], [])
test_list_3 = (['python', 'izm', 'com'], ['www', 'http'])


print(all(test_list_1))
print(all(test_list_2))
print(all(test_list_3))






# all関数は、以下の処理と同じことを行っています
# 「公式ドキュメントより引用」とPython-izm には書いてある
def all(iterable):
	for element in iterable:
		if not element:
			return False
	return True





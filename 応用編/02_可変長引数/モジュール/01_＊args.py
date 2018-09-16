


def test_func(*args):
	print(args)


test_func(1, 2, 3, 4, 5)


print('～～～～～～～～～～～～')


def test_func_2(code, name, *args):
	print(code, name)
	print(args)

test_func_2(100, 'python-izm', 'JP', 'US')





print('～～～～～～～～～～～～')

def test_func_3(code, name, *countries):
	print(code, name)
	print(countries)
	
test_func_3(100, 'python-izm', 'JP', 'US')


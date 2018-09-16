


def test_func(**kwargs):
	print(kwargs)

test_func(code=100, name='python-izm')


print('～～～～～～～～～～～～')


def test_func_2(code, name, kana, *args, **kwargs):
	print(code, name, kana)
	print(args)
	print(kwargs)


test_func_2(
	100, 'python-izm', u'パイソンイズム',
	'JP', 'US',
	email='xxxx', city='Tokyo'
)




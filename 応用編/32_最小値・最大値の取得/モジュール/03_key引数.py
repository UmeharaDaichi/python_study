


def key_func(n):
	return int(n)

l = [2, 3, 4, '111']

print(min(l, key=key_func))
print(max(l, key=key_func))


print('～～～～～～～～～～～～')

def key_func2(n):
	return str(n)


print(min(l, key=key_func2))
print(max(l, key=key_func2))



print('～～～～～～～～～～～～')

# 上記は変換してるだけなので、↓と同じ

print(min(l, key=int))
print(max(l, key=int))

print(min(l, key=str))
print(max(l, key=str))




print('～～～～～～～～～～～～')


def key_func3(n):
	return n[2]

# code / name / score
l = [(1, 'Python', 100), (2, 'Ruby', 80), (3, 'Perl', 40)]

print(min(l, key=key_func3))
print(max(l, key=key_func3))




print('～～～～～～～～～～～～')

def key_func4(n):
	return n.score

class TestClass:
	
	def __init__(self, code, name, score):
		self.code = code
		self.name = name
		self.score = score
	
	def __str__(self):
		return '({}, {}, {})'.format(self.code, self.name, self.score)


l = [
	TestClass(1, 'Python', 100),
	TestClass(2, 'Ruby', 80),
	TestClass(3, 'Perl', 40)
	
]


print(min(l, key=key_func4))
print(max(l, key=key_func4))













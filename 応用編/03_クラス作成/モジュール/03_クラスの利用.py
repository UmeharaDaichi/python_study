
class TestClass:
	
	def __init__(self, code, name):
		self.code = code
		self.name = name
		

classes = []

# __init__を通じて、それぞれの情報を持つインスタンスを作成
classes.append(TestClass(1, 'テスト１'))
classes.append(TestClass(2, 'テスト２'))


for test_cls in classes:
	print('===== Class =====')
	print('code --> ' + str(test_cls.code))
	print('name --> ' + test_cls.name)







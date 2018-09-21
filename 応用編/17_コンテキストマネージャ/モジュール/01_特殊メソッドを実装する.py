

class ContextManagerTest:
	
	def __enter__(self):
		print('__enter__')
	
	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__')


with ContextManagerTest():
	print('with')


print('～～～～～～～～～～～～')

class ContextManagerTest2:
	
	def __enter__(self):
		print('__enter__')
	
	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__')
		print(exc_type)
		print(exc_value)
		print(traceback)
		
		# 戻り値がtrueなら処理続行、falseなら処理がエラー終了
		return True

with ContextManagerTest2():
	val = int('abc')



print('～～～～～～～～～～～～')

class ContextManagerTest3:
	
	def __enter__(self):
		print('__enter__')
		return 'as obj'
		
	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__')

with ContextManagerTest3() as as_obj:
	print(as_obj)







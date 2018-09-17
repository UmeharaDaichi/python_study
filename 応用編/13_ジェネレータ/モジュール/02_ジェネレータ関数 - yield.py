


def func_sample():
	yield('おはよう')
	yield('こんにちは')
	yield('こんばんは')
	
	

# そのままでは何も出力されません
func_sample()

print('～～～～～～～～～～～～')

# yieldが含まれると、ジェネレータ化するので、反復可能なオブジェクトになります
for i in func_sample():
	print(i)

print('～～～～～～～～～～～～')


# 以下のように値を取り出す事も可能です
f = func_sample()
print(next(f))
print(next(f))
print(f.__next__())


# ↑ここ、python-izmの誤り
# 「 print(f.next()) 」と書いてるが、それだとエラーとなる
# Python3系では、ジェネレータのメソッドとしては、「__next__()」が正しい
# ※Python2系だと、next()らしい





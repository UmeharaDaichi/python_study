

class PropertyTest(object):
	
	def __init__(self, url):
		self._url = url
	
	def get_url(self):
		print('-- get_url --')
		return self._url
	
	url = property(get_url)

prop = PropertyTest('htttps://www.python-izm.com/')

# プロパティ「url」を取得
print(prop.url)

# getterのみの定義なので更新しようとするとエラー
# prop.url = 'python-izm'




# どうやら「self._url」のアンダーバーで、getter/setterを使わず取得/代入ができる模様
# なので、setterがなくても、アンダーバー付きでパラメータを指定するとそのまま代入できてしまった(prop._url = '' ←ならエラーにならない)
# 逆に、getterの記述でアンダーバーを抜くと、無限ループする




print('～～～～～～～～～～～～')



class PropertyTest2():
	
	def __init__(self, url):
		self._url =url
	
	def get_url(self):
		print('-- get_url --')
		return self._url
	
	def set_url(self, url):
		print('-- set_url--')
		self._url = url
	
	def del_url(self):
		del self.url
	
	url = property(get_url, set_url, del_url, 'url Property')
	

prop = PropertyTest2('https://www.python-izm.com/')


# setter (set_url) にアクセス
prop.url = 'python-izm'

# getter (get_url) にアクセス
print(prop.url)






print('～～～～～～～～～～～～')

class PropertyTest3():
	
	def __init__(self, scheme, host):
		self.schema = scheme
		self.host = host
		
		# ↑なんか教材が誤字していると思われるが、とりあえずそのまま「self.schema = scheme」
	
	def get_url(self):
		return ('{}://{}/'.format(self.schema, self.host))

	url = property(get_url)


prop = PropertyTest3('https', 'www.python-izm.com')

print(prop.url)















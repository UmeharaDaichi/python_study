





class PropertyTest(object):
	
	def __init__(self, url):
		self._url = url
	
	@property
	def url(self):
		print('-- get_url --')
		return self._url

prop = PropertyTest('https://www.python-izm.com/')

# プロパティ「url」を取得
print(prop.url)

# getterのみの定義なので更新しようとするとエラー
# prop.url = 'python-izm'


print('～～～～～～～～～～～～')

class PropertyTest2(object):
	
	def __init__(self, url):
		self._url = url
	
	@property
	def url(self):
		print('-- get_url--')
		return self._url
	
	@url.setter
	def url(self, url):
		print('-- set_url --')
		self._url = url
	
	@url.deleter
	def url(self):
		del self._url

prop = PropertyTest2('https://www.python-izm.com/')

# setterにアクセス
prop.url = 'python-izm'

# getterにアクセス
print(prop.url)



print('～～～～～～～～～～～～')

class PropertyTest3(object):
	
	def __init__(self, scheme, host):
		self.schema = scheme
		self.host = host
	
	@property
	def url(self):
		return('{}://{}/'.format(self.schema, self.host))

prop = PropertyTest3('https', 'www.python-izm.com')

print(prop.url)













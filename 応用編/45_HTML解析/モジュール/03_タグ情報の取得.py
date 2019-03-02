

import urllib.request
from html.parser import HTMLParser


class TestParser(HTMLParser):

	def handle_starttag(self, tagname, attribute):
		if tagname.lower() == 'a':
			for i in attribute:
				if i[0].lower() == 'href':
					print(i[1])



url = 'http://www.python-izm.com/'

htmldata = urllib.request.urlopen(url)

parser = TestParser()
parser.feed(htmldata.read().decode('UTF-8'))

parser.close()
htmldata.close()








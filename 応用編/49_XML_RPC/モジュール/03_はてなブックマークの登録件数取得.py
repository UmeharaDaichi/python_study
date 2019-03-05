

# 結果は帰って来ないらしいが、参考までに


import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://b.hatena.ne.jp/xmlrpc')

print(server.boolmark.getCount('http://www.python-izm.com/'))
print(server.bookmark.getTotalCount('http://www.python-izm.com/'))









import os

filepath = 'c:/python'


# ↓これは、ファイルもディレクトリもどっちがあってもTrueになる
if os.path.exists(filepath):
	print('指定のファイル、またはディレクトリが存在しています。')

	# ↓これはファイルのみ
	if os.path.isfile(filepath):
		print('指定のパスはファイルです。')
	
	# ↓ これはディレクトリのみ
	if os.path.isdir(filepath):
		print('指定のパスはディレクトリです。')

else:
	print('指定のファイル、またはディレクトリが存在していません。')







import os
import shutil

def show_dir(path):
	print('====================================')
	for dirpath, dirnames, filenames in os.walk(path):
		for dirname in dirnames:
			print(os.path.join(dirpath, dirname))


tmpdir = 'c:/python/tmp'

# 作成
os.mkdir(tmpdir)
os.makedirs('c:/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)


# 1個削除
os.rmdir('c:/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)


# 削除

# os.removedirs(tmpdir)
shutil.rmtree(tmpdir)










import threading
import time
import datetime


# メインが先に終わらないとデーモンスレッド True の意味がなさそう
# なので、待ち時間はpython-izmと逆にしてます


class TestThread(threading.Thread):

	def run(self):
		print('  === start sub thread ===')
		for i in range(5):
			time.sleep(10)
			print('  sub thread : ' + str(datetime.datetime.today()))
		print('  === end sub thread ===')


th = TestThread()
th.daemon = True
# th.daemon = False

th.start()

time.sleep(1)

print('=== start main thread ===')
for i in range(5):
	time.sleep(5)
	print('main thread : ' + str(datetime.datetime.today()))
print('=== end main thread ===')







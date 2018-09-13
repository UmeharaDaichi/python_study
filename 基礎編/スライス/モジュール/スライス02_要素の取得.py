


test_list = ['https', 'www', 'python', 'izm', 'com']



print(test_list[:4])
print(test_list[2:])

print(test_list[::2])
print(test_list[3:5])


print('-----------------負の数編----------------')

print(test_list[-1:])	# 末尾から全ての要素
# ↑後ろから一個戻った所から後ろ全て

print(test_list[:-1])	# 末尾まで全ての要素
# ↑後ろから一つ戻ったところまでを取得

print(test_list[::-1])	# 末尾から全ての逆順要素
# ↑-1ずつ場所が加算


print('-----------------終わり超過編----------------')

print(test_list[:999])





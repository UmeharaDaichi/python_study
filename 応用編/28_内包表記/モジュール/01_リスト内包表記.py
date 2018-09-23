

comp_list = [i for i in range(10)]

print(comp_list)


# 上記は↓と同じ処理内容
comp_list = []
for i in range(10):
	comp_list.append(i)

print(comp_list)



# こういうこともできます
comp_list = [str(i * i) for i in range(10)]

print(comp_list)



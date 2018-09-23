


comp_dict = {str(i): i * i for i in range(10)}

print(comp_dict)


# 上記は↓と同じ
comp_dict = {}
for i in range(10):
	comp_dict[str(i)] = i * i

print(comp_dict)













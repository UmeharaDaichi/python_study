

comp_set = {str(i * i) for i in range(10)}

print(comp_set)



# ↓に同じ

comp_set = set()
for i in range(10):
	comp_set.add(str(i * i))
	
print(comp_set)








import csv

csv_file = open('./python.csv', 'r', newline='')
reader = csv.reader(csv_file)

for row in reader:
	print('-------------------')
	for cell in row:
		print(cell)

csv_file.close()







csv_file = open('./python_1-4.csv', 'r', newline='')
reader = csv.reader(csv_file)

for row in reader:
	print('-------------------')
	for cell in row:
		print(cell)

csv_file.close()









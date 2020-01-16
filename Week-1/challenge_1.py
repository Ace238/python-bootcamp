Input_list = [2.5,6.2,3.14]

if(len(Input_list) == 0):
	print("0")

else:
	sum = 0
	for index in range(0, len(Input_list)):
		sum += Input_list[index]
	print(sum)
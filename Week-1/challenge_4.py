a = [1,2,3]
b = [1,2,3]
Output = []

if(len(a) == 0 and len(b) == 0):
	print(a)
elif(len(a) == 0):
	print(b)
elif(len(b) == 0):
	print(a)
else:
	#Checking values of a
	for num1 in range(0, len(a)):
		same = 0
		for num2 in range(0, len(b)):
			if(a[num1] == b[num2]):
				same = 1
		if(same == 0):
			Output.append(a[num1])

	#Checking values of b
	for num1 in range(0, len(b)):
		same = 0
		for num2 in range(0, len(a)):
			if(b[num1] == a[num2]):
				same = 1
		if(same == 0):
			Output.append(b[num1])

	print(Output)
Output = []
n = int(input("Enter the upper bound: "))

if(n == 0):
	print(Output)
else:
	for odd in range(0, n+1):
		if(odd % 2 != 0):
			Output.append(odd)
	print(Output)
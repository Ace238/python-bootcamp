n = int(input("Enter number greater than or equal to 0: "))

if(n < 0):
	print("Invalid Number")
elif(n == 0):
	ans = 0
	print(ans)
else:
	ans = n * 2
	print(ans)
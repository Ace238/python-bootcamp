# TODO: Write a function that takes N as in an 
# input and print all common multiples of 
# 3 and 7, between 0 and N (inclusive)

def x(N):

	# number = int(input("Number Please: "))

	for num in range(0,N+1):
		if(num % 3 == 0):
			print(num)
		elif(num % 7 == 0):
			print(num)
		else:
			pass

# N = int(input("Number Please: "))
x(49)

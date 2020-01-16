# The goal of this script is to print out the
# odd numbers between 1 and N (inclusive),
# where N is a user input

N = int(input("Enter an upper limit: "))

print("For loop")
for number in range(1,N+1):
	if(number % 2 != 0):
		print(number)

print("While loop")
counter = 1
while counter >= 1 and counter <= N:
	if(counter % 2 != 0):
		print(counter)
	counter += 1
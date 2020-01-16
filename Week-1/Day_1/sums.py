# The goal of this script is to sum up all of
# the numbers between N and M (inclusive),
# where N and M are both user input

N = int(input("Enter first number: "))
M = int(input("Enter second number: "))

if(N > M):
	max = N
	min = M
elif(M > N):
	max = M
	min = N

sum = 0
print("For loop")
for number in range(min, max+1):
	sum += number

print("The total sum is:", sum)
#
#
print("While loop")
sum = 0
num = N

while num <= M:
	sum += num
	num +=1

print("The total sum is:", sum)
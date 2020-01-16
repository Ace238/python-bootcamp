counter = 0
print("counter loop")
while counter <= 10:
	print(counter)
	counter += 1

#"range(start, stop, increment)", increment is 1 by default

print("range of 5, increment of 1")
for number in range(0,5):
	print(number) 

print("range of 5, increment of 2")
for number in range(0,5,2):
	print(number) 
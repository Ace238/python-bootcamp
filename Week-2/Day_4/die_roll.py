import random

def roll_die(dice_max):
	"""

	returns a die roll - random integer between 1 and 6
	0 through 6 are each side of a standard die

	"""

	return random.randint(1,dice_max)

def monte_carlo(n):
	"""

	performs a monte carlo simulation of a die roll
	[PARAM]\t n (int) - number of samples
	[RETURN]\t None - prints out the results of the simulation

	"""

	one_count = 0
	two_count = 0
	three_count = 0
	four_count = 0
	five_count = 0
	six_count = 0
	exp_count = 0

	while exp_count <n:
		result = roll_die()
		if(result == 1):
			one_count += 1
		elif(result == 2):
			two_count += 1
		elif(result == 3):
			three_count += 1
		elif(result == 4):
			four_count += 1
		elif(result == 5):
			five_count += 1
		elif(result == 6):
			six_count += 1

		exp_count += 1

	print(f"There were {n} simulations performed.")
	msg = f"There were {(one_count/n) * 100}% ones"
	print(msg)
	msg = f"There were {(two_count/n) * 100}% twos"
	print(msg)
	msg = f"There were {(three_count/n) * 100}% threes"
	print(msg)
	msg = f"There were {(four_count/n) * 100}% fours"
	print(msg)
	msg = f"There were {(five_count/n) * 100}% fives"
	print(msg)
	msg = f"There were {(six_count/n) * 100}% sixes"
	print(msg)

# monte_carlo(100000)

def monte_carlo_with_lists(N, dice_max = 6):

	results = []

	for exp in range(0,N):
		results.append(roll_die(dice_max))

	print(f"{N} experiments performed")
	for outcome in range(1, dice_max + 1):
		count = results.count(outcome)
		msg = f"The probability of {outcome} = {(count/N)*100}%"
		print(msg)

dice_max = 10
monte_carlo_with_lists(10000, dice_max)
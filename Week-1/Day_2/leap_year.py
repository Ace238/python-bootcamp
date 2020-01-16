leap = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

#conditions
for index in range (0, len(leap)):	
	if(leap[index] % 100 == 0 and leap[index] % 400 != 0):
		print(leap[index],"False")
		# print("False")
	elif(leap[index] % 4 == 0 or leap[index] % 400 == 0):
		print(leap[index],"True")
		# print("True")
	else:
		print(leap[index],"False")
		# print("False")
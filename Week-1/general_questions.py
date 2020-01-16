## Problem 1 ##

x = 14.5
print(type(x))
#  Output: <class 'float'>

My_name = "Bob"
print(My_name);
#  Output: Bob

My_name = "Bob"
print(type(My_name))
#  Output: <class 'string'>

My_name = "Mike" + str(49)
print(type(My_name)) 
#  Output: <class 'string'>

## Problem 2 ##

x, y = 8,2
ans = x^y
# ans = error

x, y = 8,2
ans = x**y
# ans = 64

x, y = “2”, 5
ans = x + y
# ans = error

x, y = 18, 4
ans = x % y
# ans = 2

x, y = 18, 4
ans = (x % y) >= 3
# ans = False
a = input('first: ')
x = raw_input('what to do +-*/: ')
b = input('second: ')

if x == "+":
	print a + b
elif x == "-":
	print a - b
elif x == "*":
	print a * b
elif x == "/":
	float(a) / float(b)
else:
	print "please use +-*/"

'''
The problem of this desigh is that if x is not +-*/ 
then the program will go through all those if elif elif
then to else, and print the warning messege. It is a waste
'''
number = input('number: ')     # after input, the type of input is int
count = 0

while number != 1:
	if number % 2:
		number = number * 3 + 1
	else:
		number = number / 2
	count += 1
	print number
print "count number = %s" % count
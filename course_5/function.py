def f(x):
	return x * 2

def fu():
	print 'hello'

# if argument is less then fd() given

def fd(x, y = 1):
	'''
	y = 1 is default value
	so it will work when fd(10) 
	only have one variable given
	it can be fd(x = 1, y = 1)
	but fd(x = 1, y) is wrong
	'''
	return x * y

# if argument is more than fAll given

def fAll(x, y, z):
	return x + y + z

def fAll2(*z):
	'''
	z is a tuple
	'''
	return sum(z)

def fDict(**d):
	'''
	d is dict 
	'''
	print d

y = f(10)
print y 

z = fu()
print z

print fd(10, 20)
print fd(y = 10, x = 20)

print fAll2(1, 2, 3, 5, 6)  

# globle variable
a = 10
def fGlobal():
	'''
	result = 100
	because 100 is near then fGloble
	'''
	a = 100
	print a
fGlobal()
print a          # a still equal to 10

a = 10
def fGlobal2():
	global a
	a = 100
	print a
fGlobal2()
print a          # a is change to 100, because a is global variable inside the function

# if we want to return more value

def fd2(x, y):
	'''
	return a tuple
	'''
	return (x + y, x * y)
print fd2(10, 20)

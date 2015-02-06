'''
could function be like a variable?
could function have no name?
what is the python specialized code?
'''

# function call function

def f(x):
	return x + 1

def ff(f, z):
	return f(z)

print f(10)
print ff(f, 10)        # ff function called f function\

# return a function

def fff(z):
	def t():
		return "i am new"
	return t()


ft = fff(f)
print ft


# filter(), zip(), map(), reduce()

l = ['bad', 'good', 'very good', 'very bad']
print l

def f(x):
	if 'bad' not in x:
		return True

print filter(f, l)

# generate a dict from two list

l1 = ['name', 'hp', 'attack']
l2 = ['borye', 100, 20]

print dict(zip(l1, l2))

# add two list

l3 = range(1, 6)
l4 = range(6, 11)

# method 1

for x, y in zip(l3, l4):
	print x + y

# method 2

def f(x, y):
	return x + y

print map(f, l3, l4)

# calculate 5!

def f(x, y):
	return x * y

print reduce(f, range(1, 6))

# we only need f in the reduce function
# maybe only once, so we could use a no-name funcion
# for example, filter function
# use lambda instead

l = ['bad', 'good', 'very good', 'very bad']
print l

print filter(lambda x: 'bad' not in x, l)

print reduce(lambda x, y: x * y, range(1, 6))


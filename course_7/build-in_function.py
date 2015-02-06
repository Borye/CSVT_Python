'''
len()
divmod()
pow()
round()
abs()
max()
min()

callable()
isinstance()
cmp()
range()
xrange()

type()
int()
long()
float()
complex()

str()
list()
tuple()
hex()
oct()
chr()    ASCII to string
ord()   

python help function: help()

pow(x, y[, z]) ---------- don't need to add z which in []

'''

help(round)

# callable to see if the value been called

s = 'abc'
def f():
	return 1

print callable(s)
print callable(f)

# isinstance 

s = 'abc'

print isinstance(s, str)

# cmp() compare strings

a = 'abc'
b = 'abcd'

print cmp(a, b)
print cmp(b, a)

# print "hello world" 10 times

for i in range(1, 11):
	print "hello world"

for i in xrange(1, 11):
	print "hello world"

# xrange() is that don't need obtain RAM

print range(10)
print xrange(10)

# transform dict

t = [('x', 123), ('y', 456)]
print dict(t)

import string
'''
string

str.capitalize()
str.replace()
str.split()
str.strip()
str.join

help(string)
help(str) to find other method
'''

# change "hello world" to "good world"

s = 'hello world'
print s.replace('hello', 'good')

# capitalize

print s.capitalize()

# split

ips = ['192.168.1.23', '10.1.1.1']
print ips[0].split('.')
print ips[0].split('.')[-1]

# strip

s = "  \thello \t   "
print '##',s,'##'
print '##', s.strip(), '##'

# join

l = ['10', '1', '1', '1']
print '.'.join(l)

# form ascii_letters

string.ascii_letters

# list

'''
add:
L.append(object)
L.insert(index, object)

delete:
L.remove(value)
L.pop(index)

find:
L.index()

L.sort()
'''

info = ['borye', 100, 50]

info.append("hello")
info.append(88)
print info

info.remove("hello")
print info

info.pop(-1)
print info

info.insert(2, 100000)    # add 100000 before 50
print info

print info.index(100000)

info.sort()
print info

# dict

'''
d.keys()
d.values()
d.items()
d.get('x')
'''

d = {'x': 123, 'y': 456}

print d.keys()
print d.values()
print d.items()
print d.get('x')

for i in d.items():
	a, b  = i
	print a, b


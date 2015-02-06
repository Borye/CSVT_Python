import math, pylab

x = []
y = []
num = 0.0

while num < math.pi * 4:
	y.append(math.sin(num))
	x.append(num) 
	num += 0.1
pylab.plot(x, y, 'ro')
pylab.show()


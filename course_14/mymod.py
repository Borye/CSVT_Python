#coding:utf8
def jia(a, b):
	return a + b

def jian(a, b):
	return a - b

def cheng(a, b):
	return a * b

print __name__

if __name__ == "__main__":
	'''
	这句话的作用是：
	当别的程序调用这个脚本的时候
	__name__等于mymod，不等于__main__
	所以在被调用的时候，以下的语句不会被运行到
	只会运行以上的函数部分
	'''
	print "!!!!!!!!!!!!!!"



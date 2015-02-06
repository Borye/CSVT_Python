#coding:utf8
'''
OOP三大特性：

1 封装性，通过接口方法访问
2 继承性，基于类创建新类
3 动态性，运算符或方法可根据对象调用不同方法

公有私有：

设计者和程序员，
设计者控制和保护类的内部结构
程序员使用方法

特殊方法：

__init__  构造函数
__del__  析构函数
__add__  +
__or__  |
__repr__  打印转换
__str__  打印转换
__call__  调用函数

__getattr__  限制
__setattr__  取值
__len__  长度
__cmp__  比较
__lt__  小于
__eq__  等于
__radd__
__iadd__  +=
__iter__  迭代

'''

class MyClass(object):
	name = "test class"    # 公有属性
	__money = "500"        # 私有属性

	def myMethod(self):
		print self.name

	def say(self):
		'''
		方法访问私有属性
		'''
		print "i have %s yuan" % self.__money

	def __Yuan(self):
		'''
		私有方法
		'''
		print "i have %s yuan" % self.__money

inst1 = MyClass()

print inst1.name   # 公有属性，外部可以访问
# print inst1.__money  # 私有属性，外部访问不到

inst1.say()    # 内部方法访问私有属性  

print inst1._MyClass__money   # 特殊方法访问私有属性

# inst1.__Yuan() 私有方法

# __add__

class Tadd(object):
	
	def __init__(self, x):
		print "in init...."
		self.x = x
	
	def __add__(self, other):
		'''
		for + 
		''' 
		sum = self.x + other.x
		return Tadd(sum)

	def __str__(self):
		print "in str..."
		return "self + other = %s" % self.x


a = Tadd(2)
b = Tadd(3)
print a.x 
print b.x

# a + b   # 不支持对象加法

print (a + b).x 



# 分数运算

def gcd(a, b):
	if not a > b:
		a, b = b, a
	while b != 0:
		r = a % b
		a, b = b, r
	return a

def lcm(a, b):
	return a * b / gcd(a, b)

class Fadd(object):
	
	def __init__(self, x, y = 1):
		self.x = x
		self.y = y

	def __add__(self, other):
		thelcm = lcm(self.y, other.y)
		n = (thelcm / self.y * self.x) + \
		    (thelcm / other.y * other.x)
		return Fadd(n, thelcm)

	def __repr__(self):
		'''
		return a value
		'''
		return str(self.x) + "/" + str(self.y)

a = Fadd(1, 5)
b = Fadd(1, 3)
print a + b





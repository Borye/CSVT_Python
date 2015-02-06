#coding:utf8
'''
类的继承
模块化编程

子类可以继承父类的属性和方法
但是父类不能用子类的属性和方法
'''

class Father(object):
	eyes = "big"
	__money = "10000"

	@classmethod         # 装饰器，使Father.pay()可用
	def pay(self):
		print "give %s" % self.__money


class SonOne(Father):
	eyes = "small"        # 子类可以重写属性
	def myPay(self):
		print "give %s" % self.__money

class SonTwo(Father):
	pass


print SonOne.__bases__   # print 父类, 父类为 Father
print Father.__bases__   # 父类为object
print object.__bases__   # 没有父类

f = Father()
tom = SonOne()
jerry = SonTwo()

print f.eyes
print tom.eyes          # eyes(big) 继承于父类
print jerry.eyes

f.pay()
# jerry.__money     # 私有属性 子类不能继承

jerry.pay()     # 子类可以继承父类的方法 (pay)

# 双继承

class Uncle(object):
	eyes = "small"
	money = "1000000"

class SonThree(Father, Uncle):
	pass

ron = SonThree()
print ron.eyes      # 结果是big, 一个子类可以继承多个父类，如果重复则继承第一个
print ron.money

# 通过类直接访问属性

print Father.eyes
print SonThree.eyes

Father.pay()


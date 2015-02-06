#coding:utf8
'''
异常基本处理：
1 保持对特定代码块的监视
2 在被监视代码中出现错误或异常，停止代码
3 引发遇到的特定异常
4 寻找捕获器捕获或处理此异常
5 如找到捕获器，则跳转到异常处理代码，如没有则转交python处理

try:
	code
except exceptionName[, msg]:
	code

AttributeError  试图访问一个对象没有的属性
IOError         输入输出异常，无法打开文件
importError     无法引入包
IndentationError 代码没有正确对齐
IndexError       下表所以超序列边界
KeyError         试图访问你字典里不存在的键
KeyboardInterrupt Ctrl + C 被按下
NameError        使用一个还未赋予对象的变量
SyntaxError      python代码逻辑语法出错，不能执行
TypeError        传入对象类型与要求不符
UnboundLocalError  试图访问一个还未设置的全局变量
ValueError       传入一个不被期望的值，即使类型正确

异常处理的哲学:
三思而后行
宽恕比获得许可更容易

应用场景
检查输入
检查文件打开
while内反复输入文件名

引发异常 

'''

# 忽略异常

try:
	print int('abc')
except Exception, msg:
	print msg
finally:
	print "end....."

# 打开文件
'''
while True:  # 创造死循环
	filepath = raw_input('input a file path: ')
	try:
		f = open(filepath)
		contents = f.read()
		print contents
	except IOError:
		print "no such directory"
	finally:
		try:
			f.close()
		except NameError:
			pass
'''
# 自定义异常类
# 做一个 Exception 的子类

class MyInputError(Exception):
	def __init__(self, length, least):
		Exception.__init__(self)    # 初始化父类
		self.length = length
		self.least = least

try:
	s = raw_input('input a string: ')
	if len(s) < 10:
		raise MyInputError(len(s), 10)
except MyInputError, x:
	print "your length of string is %d, it at least need length of %d" % (x.length, x.least)
except EOFError:
	print "Ctrl + d Error"
except Exception:
	print "Unknown Error"
finally:
	print "The End"

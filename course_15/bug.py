#coding:utf8
'''
寻找BUG方法：
1 print输出
2 logging模块
3 bpython编写代码
4 python -i执行代码
5 pdb调试
'''

# print 

def f(x):
	print x             
	return ('hello', x)

f(123)

# logging 
# it could replace print

import logging
'''
logging.basicConfig(filename = 'example.log', level = logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
'''

def f(x):
	logging.warning('i am warn') 
	return ('hello', x)

f(123)

# bpython

# python -i

# pdb
# 长代码时候适用


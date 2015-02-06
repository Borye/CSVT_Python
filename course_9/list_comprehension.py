#coding:utf8
'''
this is a test code for function
'''

# 求10以内的3或5的倍数

def f(num):
	'''
	return 1
	'''
	l = []
	for i in range(1, num):
		if i % 3 == 0 or i % 5 == 0:
			l.append(i)
	return l

print sum(f(1000))

# 用python的方法 
# list comprehension [expr for iter_var in iterable if cond_expr]
# 返回一个新的列表的时候后才能用

print [i for i in range(1, 10)]
print [i + 10 for i in range(1, 10)]

print sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])

l = ['good', 'bad']
print l
print [i for i in l if 'bad' not in i]

# list comprehension always return list

print type([i for i in tuple(range(1, 10))])

# using generator object [] change tp ()

print type((i for i in range(1, 10) if i % 3 == 0 or i % 5 == 0))

g = (i for i in range(1, 10) if i % 3 == 0 or i % 5 == 0)
print g.next()

# so to save time, we could write it as 

print sum((i for i in xrange(1, 1000) if i % 3 == 0 or i % 5 == 0))

'''
列表解析建议：

1 当需要执行只是一个循环的时候尽量使用循环不用解析
2 当有内置操作或者类型能够更直接的方式实现的 不用使用
3 如果需要对每个元素都调用并且返回结果是，应使用map 不用解析
'''

# main function
# __variable__ is build-in variable

print __name__   # result will be __main__
print __doc__    # result is the line 3 note
print f.__doc__  # result is note of f()


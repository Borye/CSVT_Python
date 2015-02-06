#coding:utf8
from django.shortcuts import render

class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def get_name(self):
		return 'My name is %s' % self.name


def index(req):
	'''
	# in index1.html
	c = {'username': 'Borye', 'age': 23, 'marry': False}
	c['books'] = ('python', 'web', 'django')
	c['another'] = {'a': 'app', 'b': 'binary'}
	p = Person('Borye', 26, 'male')
	c['person'] = p
	return render(req, 'index.html', c)
	'''

	navs = ['首页', '新闻', '经济', '文化']

	person = {'姓名': '李博', '年龄': 23, '性别': '男'}

	return render(req, 'index.html', {'navs': navs, 'person': person})

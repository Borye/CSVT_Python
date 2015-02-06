#coding:utf8
from django.shortcuts import render

def index(req):
	c = {}
	navs = [u'首页', u'经济', u'文化', u'娱乐']
	new = {'title': 'title test', 'content': 'content of news !'}
	person = {'name': 'Borye', 'sex': 'male', 'marry': True}
	c['navs'] = navs
	c['new'] = new
	c['person'] = person
	c['title'] = u'首页'
	return render(req, 'index.html', c)

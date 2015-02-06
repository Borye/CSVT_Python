from django.shortcuts import render
from django.http import HttpResponse

def disp(req, id, name):
	print id
	print name
	return render(req, 'disp.html', {'id': id, 'name': name})

def regist(req):
	username = req.GET.get('username', None)
	return HttpResponse("user: %s regist success!!" % username) 

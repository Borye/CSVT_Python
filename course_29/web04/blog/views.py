from django.shortcuts import render

def index(req):
	return render(req, 'index.html', {'mycode': '<script>alert("hello!!");</script>', 
		                              'mylink1': '<a href="http://www.baidu.com">baidu</a>'})

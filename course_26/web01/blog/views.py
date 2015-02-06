from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def index(req):
	t = loader.get_template('index.html')
	c = Context({'title': 'Django', 'username': 'Borye'})
	return HttpResponse(t.render(c))
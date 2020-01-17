from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	a=100
	b=200
	c=a+b
	return HttpResponse("result is "+str(c))

from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	s=[]
	for i in range(1,6):
		for j in range(1,i+1):
			s.append(str(j)+' ')
		s.append("")
	return render(request,"patternapp/index.html",{'res':s})
def addition(request):
	return render(request,"patternapp/addition.html")
def addlogic(request):
	a=request.GET["txtnum1"]
	b=request.GET["txtnum2"]
	c=int(a)+int(b)
	return render(request,"patternapp/addition.html",{'res':c})


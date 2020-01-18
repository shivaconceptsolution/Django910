from django.shortcuts import render
def index(request):
	return render(request,"helloapp/index.html")
def sqlogic(request):
	a = request.POST['txtnum1']
	s=int(a)*int(a)
	return render(request,"helloapp/index1.html",{'res1':a,'res':s})


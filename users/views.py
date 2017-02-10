#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def login(request):
	return render(request, 'login.html',  {'userName': 'jayz'})

def loginCheck(request):
	if request.POST.has_key('username'):
		username = request.POST['username']
	else:
		raise Http404('错误的访问方式')
	if request.POST.has_key('password'):
		password = request.POST['password']
	else:
		raise Http404('错误的访问方式')
	return render(request, 'loginCheck.html')
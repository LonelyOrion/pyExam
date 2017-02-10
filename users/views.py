#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import Users

# Create your views here.
def login(request):
	return render(request, 'login.html')

def loginCheck(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
	except:
		return render(request, 'errorInfo.html', {'errorInfo': '错误的访问方式'})

	user = Users.objects(username=username)
	if len(user) == 0:
		return render(request, 'errorInfo.html', {'errorInfo': '用户不存在'})

	user = user[0]
	if password != user.password:
		return render(request, 'errorInfo.html', {'errorInfo': '密码错误'})

	return render(request, 'loginCheck.html', {'user': user})

def register(request):
	return render(request, 'register.html')

def registerCheck(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		nickname = request.POST['nickname']
	except:
		return render(request, 'errorInfo.html', {'errorInfo': '错误的访问方式'})

	user = Users.objects(username=username)
	if len(user) == 0:
		user = Users(username = username, password = password, nickname = nickname)
		user.save()
	else:
		return render(request, 'errorInfo.html', {'errorInfo': '用户已存在'})
	return render(request, 'registerCheck.html')
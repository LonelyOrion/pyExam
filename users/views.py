#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import Users

# Create your views here.
def login(request):
	return render(request, 'login.html')

def logout(request):
	try:
		del request.session['username']
		del request.session['nickname']
	except:
		pass
	return render(request, 'info.html', {'info': '登出成功', 'link':'/login/'})

def loginCheck(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
	except:
		return render(request, 'info.html', {'info': '错误的访问方式', 'link':'/login/'})

	user = Users.objects(username=username)
	if len(user) == 0:
		return render(request, 'info.html', {'info': '用户不存在', 'link':'/login/'})

	user = user[0]
	if password != user.password:
		return render(request, 'info.html', {'info': '密码错误', 'link':'/login/'})

	request.session['username'] = user.username
	request.session['nickname'] = user.nickname

	return render(request, 'loginCheck.html', {'user': user})

def register(request):
	return render(request, 'register.html')

def registerCheck(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		nickname = request.POST['nickname']
	except:
		return render(request, 'info.html', {'info': '错误的访问方式', 'link':'/login/'})

	user = Users.objects(username = username)
	if len(user) == 0:
		user = Users(username = username, password = password, nickname = nickname)
		user.save()
	else:
		return render(request, 'info.html', {'info': '用户已存在', 'link':'/login/'})
	return render(request, 'registerCheck.html')
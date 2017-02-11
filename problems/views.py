#coding: utf-8
from django.shortcuts import render

# Create your views here.

def showProblems(request):
	nickname = request.session['nickname']
	return render(request, 'showProblems.html', locals())

def addProblems(request):
	return render(request, 'addProblems.html')

def addProblemsCheck(request):
	try:
		problem = request.POST['problem']
		options = request.POST['options']
		answer = request.POST['answer']
	except:
		return render(request, 'info.html', {'info': '提交内容不完整'})